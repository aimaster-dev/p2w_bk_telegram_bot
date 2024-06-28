# -*- coding: utf-8 -*-
import datetime
from flask import views, render_template, request, session, redirect, url_for, g
from common_utils import xtjson
from common_utils.utils_funcs import get_ip
from models.cms_user import CmsUserTable
from constants import CMS_USER_SESSION_KEY, ROlE_ALL
from modules.view_helpres.tool_func import current_admin_data_dict
from common_utils.lqredis import SiteRedis
from modules.google_module.google_verify import GooleVerifyCls
from modules.view_helpres.view_func import add_SystemLog



class CmsLoginOut(views.MethodView):
    add_url_rules = [['/login_out/', 'cms_login_out']]

    def get(self):
        add_SystemLog(note='退出登录')
        session.pop(CMS_USER_SESSION_KEY)
        return redirect(url_for('admin.cms_login'))



class CmsLogin(views.MethodView):
    add_url_rules = [['/admin/login/', 'cms_login']]

    def login_limit(self, account):
        key = 'ADMIN_LOGIN_LIMIT_NUM_%s' % account
        _crr_num = SiteRedis.get(key)
        if not _crr_num:
            return
        if int(_crr_num.decode()) >= 5:
            return True
        if not _crr_num:
            SiteRedis.set(key, 1, expire=5 * 10)
        else:
            SiteRedis.incrby(key, 1)
            SiteRedis.expire(key, 500)
        return

    def get(self):
        dd = current_admin_data_dict()
        if dd:
            return redirect(url_for('admin.cms_index'))
        context = {}
        return render_template('cms/login.html')

    def post(self):
        action = request.form.get('action')
        if action == 'pwdLogin':
            account = request.form.get('account')
            password = request.form.get('password')
            verify_code = request.form.get('verify_code')
            if not account or not password or not account.strip() or not password.strip():
                return xtjson.json_params_error('登录失败!')
            if self.login_limit(account):
                return xtjson.json_params_error('尝试次数过多！请稍后再试...')
            user_data = CmsUserTable.find_one({'account': account.strip()})
            if not user_data:
                return xtjson.json_params_error('该用户不存在!')
            if not CmsUserTable.check_password(user_data.get('password'), password.strip()):
                return xtjson.json_params_error('密码输入错误!')
            if not user_data.get('statu'):
                return xtjson.json_params_error('该账户已被锁定!')

            is_activate = None
            if user_data.get('role_code') == ROlE_ALL.SUPERADMIN or user_data.get('role_code') == ROlE_ALL.ADMINISTRATOR or user_data.get('role_code') == ROlE_ALL.OUT_MONEY_USER or user_data.get('role_code') == ROlE_ALL.SYS_OUT_MONEY_USER:
                SITE_CONFIG_CACHE = g.site_config_cache
                login_google_verify_statu = SITE_CONFIG_CACHE.get('login_google_verify_statu')

                if login_google_verify_statu:
                    googleObj = GooleVerifyCls(pwd=user_data.get('uuid'), s_label='pay2wold', account=user_data.get('account'))
                    if user_data.get('is_activate'):
                        if not verify_code:
                            return xtjson.json_result(code=401, message='请输入GOOGLE验证码！', data={'is_show_qrcode': False})
                        if not googleObj.check_goole_code(verify_code):
                            return xtjson.json_result(code=401, message='GOOGLE验证码输入错误！', data={'is_show_qrcode': False})
                    else:
                        is_activate = True
                        generate_qrcode = googleObj.secret_generate_qrcode()
                        if not verify_code:
                            return xtjson.json_result(code=401, message='请输入GOOGLE验证码！', data={'is_show_qrcode': True, 'generate_qrcode': generate_qrcode})
                        if not googleObj.check_goole_code(verify_code):
                            return xtjson.json_result(code=401, message='GOOGLE验证码输入错误！', data={'is_show_qrcode': True, 'generate_qrcode': generate_qrcode})

                if hasattr(SITE_CONFIG_CACHE, 'cms_ip_whitelist'):
                    cms_ip_whitelist = getattr(SITE_CONFIG_CACHE, 'cms_ip_whitelist')
                    if cms_ip_whitelist or cms_ip_whitelist.strip():
                        crr_ip = get_ip()
                        _ip_statu = False
                        for _ip in crr_ip.split(','):
                            if _ip in cms_ip_whitelist:
                                _ip_statu = True
                        if not _ip_statu:
                            return xtjson.json_params_error('登录失败！')
            else:
                if user_data.get('role_code') == ROlE_ALL.AGENTADMIN:
                    cms_ip_whitelist = user_data.get('cms_ip_whitelist')
                    login_google_verify_statu = user_data.get('login_google_verify_statu')
                elif user_data.get('role_code') == ROlE_ALL.SYSTEMUSER:
                    agent_data = CmsUserTable.find_one({'uuid': user_data.get('agentadmin_uuid')}) or {}
                    if not agent_data:
                        return xtjson.json_params_error('操作失败！')
                    if not agent_data.get('statu'):
                        return xtjson.json_params_error('操作失败！')
                    cms_ip_whitelist = agent_data.get('cms_ip_whitelist')
                    login_google_verify_statu = agent_data.get('login_google_verify_statu')
                else:
                    return xtjson.json_params_error()

                if login_google_verify_statu:
                    googleObj = GooleVerifyCls(pwd=user_data.get('uuid'), s_label='pay2wold', account=user_data.get('account'))
                    if user_data.get('is_activate'):
                        if not verify_code:
                            return xtjson.json_result(code=401, message='请输入GOOGLE验证码！', data={'is_show_qrcode': False})
                        if not googleObj.check_goole_code(verify_code):
                            return xtjson.json_result(code=401, message='GOOGLE验证码输入错误！', data={'is_show_qrcode': False})
                    else:
                        is_activate = True
                        generate_qrcode = googleObj.secret_generate_qrcode()
                        if not verify_code:
                            return xtjson.json_result(code=401, message='请输入GOOGLE验证码！', data={'is_show_qrcode': True, 'generate_qrcode': generate_qrcode})
                        if not googleObj.check_goole_code(verify_code):
                            return xtjson.json_result(code=401, message='GOOGLE验证码输入错误！', data={'is_show_qrcode': True, 'generate_qrcode': generate_qrcode})

                if cms_ip_whitelist and cms_ip_whitelist.strip():
                    crr_ip = get_ip()
                    _ip_statu = False
                    for _ip in crr_ip.strip().split(','):
                        if _ip in cms_ip_whitelist:
                            _ip_statu = True
                    if not _ip_statu:
                        return xtjson.json_params_error('登录失败！')

            _ccu = CmsUserTable.find_one({'account': account.strip()})
            upda_dict = {
                'last_login_time': _ccu.get('current_login'),
                'last_login_ip': _ccu.get('current_login_ip'),
                'current_login': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'current_login_ip': get_ip(),
            }
            if is_activate is not None:
                upda_dict['is_activate'] = is_activate
            CmsUserTable.update_one({'account': account.strip()},{'$set': upda_dict})
            session[CMS_USER_SESSION_KEY] = user_data.get('uuid')
            session.permanent = True
            add_SystemLog(note='登录成功！')
            return xtjson.json_result()
        return xtjson.json_params_error('操作失败!')

