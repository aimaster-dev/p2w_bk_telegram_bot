# -*- coding: utf-8 -*-
import os
import datetime
import time

from flask import views, request, session, redirect, url_for, abort, current_app, render_template, g
from . import bp
from common_utils import xtjson
from common_utils.upload import UploadCls
from models.cms_user import CmsUserTable
from modules.view_helpres.tool_func import cms_risk_control, site_config_cache
from constants import CMS_USER_SESSION_KEY, ASSETS_FOLDER, IMAGES_EXTENSIONS, FIEL_EXTENSIONS, ROlE_ALL, CallbackState, WITHDRAW_STATUS, LANGUAGE, LANGUAGE_HINT_ALL
from common_utils.utils_funcs import PagingCLS, get_ip
from models.cms_table import SystemLogTable
from models.pay_table import unknownIncomeTable, CollectionOrderTable, WithdrawTable
from models.behalfPay import behalfPayOrderTable
from common_utils.lqredis import SiteRedis
from common_utils.utils_funcs import update_language


@bp.before_request
def site_cms_before_request():
    g.site_config_cache = site_config_cache()
    res = cms_risk_control()
    if res:
        return res


class CmsViewBase(views.MethodView):
    title = ''
    template = ''
    xtjson = xtjson
    permission_map = {}
    MCLS = None
    add_url_rules = [[]]

    def __init_data(self):
        self.user_uuid = session.get(CMS_USER_SESSION_KEY)
        self.current_admin_user = CmsUserTable.query_one({'uuid': self.user_uuid})
        self.current_admin_dict = CmsUserTable.find_one({'uuid': self.user_uuid}) or {}
        res = self.check_login()
        if res:
            return res
        self.is_superdamin = False
        self.is_agentadmin = False
        if self.current_admin_user:
            self.is_superdamin = self.current_admin_user.is_superadmin
        if self.current_admin_dict.get('role_code') in [ROlE_ALL.SYSTEMUSER, ROlE_ALL.OUT_MONEY_USER]:
            agentadmin_data = CmsUserTable.find_one({'uuid': self.current_admin_dict.get('agentadmin_uuid')}) or {}
            self.current_admin_dict['agentadmin_data'] = agentadmin_data
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            self.is_agentadmin = True
        self.current_admin_roleCode = self.current_admin_dict.get('role_code')
        self.data_from = {}
        self.filter_dict = {}
        self.context = {}
        self.search_dict = {}
        self.project_name = current_app.config.get('PROJECT_NAME')
        self.MAIN_DOMAIN = current_app.config.get('MAIN_DOMAIN')
        self.project_static_folder = os.path.join(current_app.static_folder, self.project_name)
        self.context['current_admin_user'] = self.current_admin_user
        self.context['current_admin_dict'] = self.current_admin_dict
        self.context['project_name'] = self.project_name
        self.context['site_data'] = g.site_config_cache
        self.context['format_time_func'] = self.format_time_func
        self.context['format_money'] = self.format_money
        self.context['ROlE_ALL'] = ROlE_ALL
        self.context['LANGUAGE'] = LANGUAGE
        self.context['LANGUAGE_HINT_ALL'] = LANGUAGE_HINT_ALL

        _fff22 = {}
        if self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            _fff22['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            _fff22['agentadmin_uuid'] = self.current_admin_dict.get('uuid')

        crrdate = datetime.datetime.now()
        start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0, 0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23, 59, 59)

        kkk1 = 'pay1_dfwcl_count_'+self.current_admin_dict.get('uuid')
        dfwcl_count = SiteRedis.get(kkk1)
        if not dfwcl_count:
            _f11 = {'pay_statu': False, 'reject_pay': False, 'order_time': {'$gte': start_time, '$lte': end_time}}
            _f11.update(_fff22)
            dfwcl_count = behalfPayOrderTable.count(_f11) or 0
            SiteRedis.set(kkk1, dfwcl_count, expire=10)
        else:
            dfwcl_count = int(dfwcl_count.decode())

        kkk2 = 'pay1_bmsr_count_'+self.current_admin_dict.get('uuid')
        bmsr_count = SiteRedis.get(kkk2)
        if not bmsr_count:
            _f11 = {'state': False, 'create_time': {'$gte': start_time, '$lte': end_time}}
            _f11.update(_fff22)
            bmsr_count = unknownIncomeTable.count(_f11) or 0
            SiteRedis.set(kkk2, bmsr_count, expire=10)
        else:
            bmsr_count = int(bmsr_count.decode())

        kkk3 = 'pay1_ddan_count_'+self.current_admin_dict.get('uuid')
        ddan_count = SiteRedis.get(kkk3)
        if not ddan_count:
            _f11 = {'callback_statu': CallbackState.NOT_CALLEDBACK, 'is_lose': True, 'order_time': {'$gte': start_time, '$lte': end_time}}
            _f11.update(_fff22)
            ddan_count = CollectionOrderTable.count(_f11) or 0
            SiteRedis.set(kkk3, ddan_count, expire=10)
        else:
            ddan_count = int(ddan_count.decode())

        kkk4 = 'pay1_tixian_count_'+self.current_admin_dict.get('uuid')
        txianCount = SiteRedis.get(kkk4)
        if not txianCount:
            _f11 = {'statu': WITHDRAW_STATUS.review, 'create_time': {'$gte': start_time, '$lte': end_time}}
            _f11.update(_fff22)
            txianCount = WithdrawTable.count(_f11) or 0
            SiteRedis.set(kkk4, txianCount, expire=10)
        else:
            txianCount = int(txianCount.decode())
        self.context['dfwcl_count'] = dfwcl_count
        self.context['bmsr_count'] = bmsr_count
        self.context['ddan_count'] = ddan_count
        self.context['txianCount'] = txianCount

    def formatted_to2(self, number):
        '''
        获取两位小数
        '''
        if isinstance(number, int):
            return number
        try:
            formatted = "{:.2f}".format(number)
            return float(formatted)
        except:
            return number

    # 添加系统操作日志
    def add_SystemLog(self, note='', code=200, method='GET'):
        if not self.current_admin_dict:
            return
        ips = get_ip()
        if isinstance(ips, list):
            ips = ','.join(ips)
        _data = {
            'user_uuid': self.current_admin_dict.get('uuid'),
            'state_code': code,
            'ip': ips,
            'url_path': str(request.path),
            'note': note,
            'method': method,
        }
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            _data['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            _data['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        SystemLogTable.insert_one(_data)

    def format_time_func(self, data, formatStr=None):
        try:
            if not isinstance(data, datetime.datetime):
                return data
            if not formatStr:
                return data.strftime('%Y-%m-%d %H:%M:%S')
            return data.strftime(formatStr)
        except:
            return data

    def format_money(self, data):
        try:
            if '.' in str(data):
                _V = round(float(data), 2)
                return format(float(_V), ",")
            return format(int(data), ",")
        except:
            return data

    def check_login(self):
        if not self.current_admin_user:
            return redirect(url_for('admin.cms_login'))
        if not self.current_admin_user.statu:
            session.pop(CMS_USER_SESSION_KEY)
            return abort(404)

    def check_permission(self, code):
        if self.is_superdamin:
            return True
        if not self.current_admin_user or not code:
            return False
        return self.current_admin_user.has_permission(code)

    def by_silce(self,startendstr):
        if startendstr and '|' not in startendstr:
            raise ValueError(u'区间搜索必须以“|”分割')
        start_str, end_str = startendstr.split("|")
        if start_str.isdigit() or end_str.isdigit():
            if start_str and end_str:
                return int(start_str),int(end_str)
            if start_str and not end_str:
                return int(start_str),None
            return None,int(end_str)
        else:
            if start_str:
                try:
                    start_time = datetime.datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
                except:
                    try:
                        start_time = datetime.datetime.strptime(start_str, '%Y-%m-%d')
                    except Exception as e:
                        raise ValueError(u'起始时间转换出错: %s' % str(e))
            else:
                start_time = None
            if end_str:
                try:
                    end_time = datetime.datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
                except:
                    try:
                        end_time = datetime.datetime.strptime(end_str, '%Y-%m-%d')
                        timedelay = datetime.timedelta(days=1)
                        end_time += timedelay
                    except Exception as e:
                        raise ValueError(u'结束时间转换出错: %s' % str(e))
            else:
                end_time = None
            return start_time, end_time

    def search_func(self, FIELDS):
        """get数据搜索处理"""
        s_filter_dict, s_context_res = {}, {}
        if hasattr(self.MCLS, 'field_search'):
            field_search = getattr(self.MCLS, 'field_search')()
            for db_field in field_search:
                col_value = request.args.get(db_field)
                if col_value is None:
                    continue
                s_context_res[db_field] = col_value
                if col_value and col_value.strip():
                    col_value = col_value.strip()

                    if db_field == 'create_time':
                        start_time, end_time = self.by_silce(col_value)
                        s_filter_dict[db_field] = {'$gte': start_time, '$lte': end_time}
                        continue
                    field_cls = FIELDS.get(db_field)
                    if not field_cls:
                        return  False, '%s: 无处理属性!' % db_field
                    if field_cls.field_type == 'UUIDField':
                        s_filter_dict[db_field] = col_value
                    elif field_cls.field_type == 'IDField':
                        s_filter_dict[db_field] = int(col_value)
                    else:
                        statu, res = field_cls.search_validate(col_value)
                        if not statu:
                            return False, res
                        s_filter_dict[db_field] = res
        return True, [s_filter_dict, s_context_res]

    def editorUploadFile(self, foldername='article/images'):
        """编辑器上传文件处理"""
        upload = UploadCls()
        upload.static_folder = self.project_static_folder
        upload.uploaddir = ASSETS_FOLDER
        upload.foldername = foldername
        statu, msg = upload.upload_file_func()
        if statu:
            filename = msg.rsplit('/', 1)[-1]
            result_dict = {"uploaded": 1, "fileName": filename, "url": msg}
        else:
            result_dict = {"uploaded": 0, "error": { "message": msg}}
        return xtjson.json_result(**result_dict)

    def post_upload_picture(self, picture_name='', foldername='article/images', limit_types=IMAGES_EXTENSIONS):
        """
        图片上传处理
        :param picture_name: 图片名称
        :param uploaddir: 上传到的文件夹名称(1级)
        :param foldername:  上传到的文件父级文件夹名称(2级)
        :param limit_size: 文件大小限制(KB)
        :param limit_types:
        :return:
        """
        upload = UploadCls()
        upload.static_folder = self.project_static_folder
        upload.uploaddir = ASSETS_FOLDER
        upload.foldername = foldername
        upload.limit_types = limit_types
        upload.filename = picture_name
        statu, msg = upload.upload_file_func()
        return statu, msg

    def post_file_upload(self, filename='', foldername='', limit_types=FIEL_EXTENSIONS):
        """
        文件上传处理
        :param filename: 文件名
        :param uploaddir: 上传到的文件夹名称(1级)
        :param foldername:  上传到的文件父级文件夹名称(2级)
        :param limmit_types:  文件类型限制
        """
        upload = UploadCls()
        upload.static_folder = self.project_static_folder
        upload.uploaddir = ASSETS_FOLDER
        upload.foldername = foldername
        upload.limit_types = limit_types
        upload.filename = filename
        return upload.upload_file_func()

    def no_permission(self):
        return self.xtjson.json_params_error('无操作权限!')

    def get_other_way(self):
        return

    def get_context(self):
        """获取context内容"""
        return {}

    def get_filter_dict(self):
        """获取搜索参数"""
        return {}

    def post_data_other_way(self):
        return

    def post_other_way(self):
        return

    def view_get(self, *args, **kwargs):
        return self.xtjson.json_result()

    def view_post(self, *args, **kwargs):
        return self.xtjson.json_result()

    def get(self, *args, **kwargs):
        res = self.__init_data()
        if res:
            return res
        self.add_SystemLog(note='访问页面')
        return self.view_get(*args, **kwargs)

    def post(self, *args, **kwargs):
        res = self.__init_data()
        if res:
            return res
        return self.view_post(*args, **kwargs)



class CmsFormViewBase(CmsViewBase):
    title = ''
    template = ''
    MCLS = CmsUserTable

    def post_edit_data(self, data_form):
        self.data_dict.update(data_form)
        self.MCLS.save(self.data_dict)
        return xtjson.json_result()

    def checkPermission(self, code):
        if code in self.current_admin_user.permissions or self.current_admin_user.is_superadmin:
            return
        return xtjson.json_params_error('无权限！')

    def view_post(self, *args, **kwargs):
        self.kwargs = kwargs or {}
        self.request_data = request.form
        self.action = self.request_data.get('action')
        self.data_uuid = self.request_data.get('data_uuid')
        self.data_value = self.request_data.get('data_value')
        if request.args.get('CKEditorFuncNum'):
            return self.editorUploadFile()
        res = self.post_other_way()
        if res:
            return res
        self.data_dict = self.MCLS.find_one({'uuid': self.data_uuid})
        if not self.data_dict:
            return xtjson.json_params_error('数据不存在!')
        if self.action == '_edit_form_data':
            for db_field in self.MCLS.edit_field_sort():
                field_cls = self.MCLS.fields().get(db_field)
                v = self.request_data.get(db_field)
                statu, res = field_cls.validate(v)
                if not statu:
                    return xtjson.json_params_error(res)
                self.data_from[db_field] = res
            return self.post_edit_data(self.data_from)
        res = self.post_data_other_way()
        if res:
            return res
        return xtjson.json_params_error('操作错误!')



class CmsTableViewBase(CmsViewBase):
    title = ''
    template = ''
    MCLS = CmsUserTable
    per_page = 30
    sort = [['create_time', -1]]

    def dealwith_main_context(self):
        pass

    def view_get(self, *args, **kwargs):
        self.kwargs = kwargs or {}
        res = self.get_other_way()
        if res:
            return res
        self.context['title'] = self.title
        page = request.args.get('page', 1, int)
        self.per_page = request.args.get('per_page', self.per_page, int)
        skip = (page - 1) * self.per_page
        self.context['title'] = self.title
        context_res = {}
        fields = self.MCLS.fields()
        statu, res = self.search_func(fields)
        if not statu:
            return res
        self.filter_dict.update(res[0])
        context_res.update(res[1])
        self.context.update(self.get_context())
        filter_dict = {}
        filter_dict.update(self.get_filter_dict())

        start_time = time.time()
        total = self.MCLS.count(filter_dict)
        all_datas = self.MCLS.find_many(filter_dict, limit=self.per_page, skip=skip, sort=self.sort)
        print('total time:', time.time() - start_time)
        pagination = PagingCLS.pagination(page, self.per_page, total)
        self.context['total'] = total
        self.context['all_datas'] = all_datas
        self.context['pagination'] = pagination
        context_res.update(self.search_dict)
        self.context['search_res'] = context_res
        self.context['per_page'] = self.per_page
        self.dealwith_main_context()

        html = render_template(self.template, **self.context)
        return update_language(self.current_admin_dict.get("language"), html)

    def view_post(self, *args, **kwargs):
        self.kwargs = kwargs or {}
        self.request_data = request.form
        self.action = self.request_data.get('action')
        self.data_uuid = self.request_data.get('data_uuid')
        self.data_value = self.request_data.get('data_value')

        if request.args.get('CKEditorFuncNum'):
            return self.editorUploadFile()
        res = self.post_other_way()
        if res:
            return res
        if self.data_uuid:
            self.data_dict = self.MCLS.find_one({'uuid': self.data_uuid})
            if not self.data_dict:
                return xtjson.json_params_error('数据不存在!')
            res = self.post_data_other_way()
            if res:
                return res
        return xtjson.json_params_error('操作错误!')
