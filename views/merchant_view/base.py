# -*- coding: utf-8 -*-
import os
import datetime
from flask import views, request, session, abort, current_app, render_template
from . import bp
from common_utils import xtjson
from models.pay_table import MerchantTable
from constants import MERCHANT_USER_SESSION_KEY, MERCHANT_ROLES
from common_utils.utils_funcs import PagingCLS


@bp.before_request
def site_merchant_before_request():
    res = ''
    if res:
        return res


class ViewBase(views.MethodView):
    title = ''
    template = ''
    xtjson = xtjson
    MCLS = None
    add_url_rules = [[]]

    def __init_data(self):
        self.user_uuid = session.get(MERCHANT_USER_SESSION_KEY)
        self.current_user_dict = MerchantTable.find_one({'uuid': self.user_uuid}) or {}
        self.data_from = {}
        self.filter_dict = {}
        self.context = {}
        self.project_name = current_app.config.get('PROJECT_NAME')
        self.project_static_folder = os.path.join(current_app.static_folder, self.project_name)
        self.context['current_admin_dict'] = self.current_user_dict
        self.context['project_name'] = self.project_name
        self.context['format_time_func'] = self.format_time_func
        self.context['format_money'] = self.format_money
        self.is_merchant = False
        self.is_submerchant = False
        if self.current_user_dict:
            if self.current_user_dict.get('role_code') == MERCHANT_ROLES.MERCHANT:
                self.is_merchant = True
            if self.current_user_dict.get('role_code') == MERCHANT_ROLES.SUBMERCHANT:
                self.is_submerchant = True
                upper_data = MerchantTable.find_one({'uuid': self.current_user_dict.get('upper_mid')}) or {}
                self.current_user_dict['upper_data'] = upper_data
        endd_time, crr_time = '', ''
        if self.current_user_dict:
            try:
                crr_time = datetime.datetime.now()
                endd_time = crr_time + datetime.timedelta(hours=12)
            except:
                pass
        self.context['is_merchant'] = self.is_merchant
        self.context['is_submerchant'] = self.is_submerchant
        self.context['crr_time'] = crr_time
        self.context['endd_time'] = endd_time
        self.context['MERCHANT_ROLES'] = MERCHANT_ROLES

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
                return format(float(data), ",")
            return format(int(data), ",")
        except:
            return data

    def check_login(self):
        if not self.current_user_dict:
            # return redirect(url_for('merchant.merchant_login'))
            abort(404)
        if not self.current_user_dict.get('statu'):
            session.pop(MERCHANT_USER_SESSION_KEY)
            return abort(404)

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
        self.__init_data()
        res = self.check_login()
        if res:
            return res
        return self.view_get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.__init_data()
        res = self.check_login()
        if res:
            return res
        return self.view_post(*args, **kwargs)



class FormViewBase(ViewBase):
    title = ''
    template = ''
    MCLS = MerchantTable

    def post_edit_data(self, data_form):
        self.data_dict.update(data_form)
        self.MCLS.save(self.data_dict)
        return xtjson.json_result()

    def view_post(self, *args, **kwargs):
        self.kwargs = kwargs or {}
        self.request_data = request.form
        self.action = self.request_data.get('action')
        self.data_uuid = self.request_data.get('data_uuid')
        self.data_value = self.request_data.get('data_value')
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



class TableViewBase(ViewBase):
    title = ''
    template = ''
    MCLS = MerchantTable
    per_page = ''
    sort = [['create_time', -1]]

    def dealwith_main_context(self):
        pass

    def view_get(self, *args, **kwargs):
        self.context['title'] = self.title
        page = request.args.get('page', 1, int)
        skip = (page - 1) * self.per_page
        self.context['title'] = self.title
        filter_dict, context_res = {}, {}
        fields = self.MCLS.fields()
        statu, res = self.search_func(fields)
        if not statu:
            return res
        filter_dict.update(res[0])
        context_res.update(res[1])
        self.context.update(self.get_context())
        filter_dict.update(self.get_filter_dict())
        total = self.MCLS.count(filter_dict)
        all_datas = self.MCLS.find_many(filter_dict, limit=self.per_page, skip=skip, sort=self.sort)

        pagination = PagingCLS.pagination(page, self.per_page, total)
        self.context['total'] = total
        self.context['all_datas'] = all_datas
        self.context['pagination'] = pagination
        self.context['search_res'] = context_res
        self.dealwith_main_context()
        return render_template(self.template, **self.context)

    def view_post(self, *args, **kwargs):
        self.kwargs = kwargs or {}
        self.request_data = request.form
        self.action = self.request_data.get('action')
        self.data_uuid = self.request_data.get('data_uuid')
        self.data_value = self.request_data.get('data_value')
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
            if self.action == 'del':
                self.MCLS.delete_one({'uuid': self.data_uuid})
                return xtjson.json_result()
        return xtjson.json_params_error('操作错误!')
