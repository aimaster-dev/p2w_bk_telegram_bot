# -*- coding: utf-8 -*-
import datetime, shortuuid, random
from flask import views, render_template, request, session, redirect, url_for, abort
from common_utils import xtjson
from models.pay_table import MerchantTable, MerchantLogTable, TunnelTable, MerchantTunnleTable
from constants import MERCHANT_USER_SESSION_KEY, TUNNLE_METHOD, ROlE_ALL, MERCHANT_ROLES
from common_utils.lqredis import SiteRedis
from modules.google_module.google_verify import GooleVerifyCls
from modules.view_helpres.merchant_func import current_user_data_dict
from common_utils.utils_funcs import get_ip, graph_captcha, checkcap, encry_md5
from models.cms_user import CmsUserTable



class MerchantLoginOut(views.MethodView):
    add_url_rules = [['/login_out', 'merchant_login_out']]

    def get(self):
        merchant_data = current_user_data_dict()
        try:
            session.pop(MERCHANT_USER_SESSION_KEY)
        except:
            pass
        if merchant_data.get('role_code') == MERCHANT_ROLES.MERCHANT:
            muid = merchant_data.get('uuid')
        else:
            muid = merchant_data.get('upper_mid')
        return redirect(url_for('merchant.merchant_login', merchant_uid=muid))



class MerchantLogin(views.MethodView):
    add_url_rules = [['/login/<string:merchant_uid>', 'merchant_login']]

    def get_data_id(self):
        while True:
            id_str = '16' +str(random.random() * 100000).split('.')[0]
            if MerchantTable.find_one({'account': id_str}):
                continue
            return id_str

    def login_limit(self, account):
        key = 'MERCHANT_ADMIN_LOGIN_LIMIT_NUM_%s' % account
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

    def regist_limit(self):
        ip = get_ip()
        if not ip:
            return
        key = 'MERCHANT_ADMIN_REGIST_LIMIT_NUM_%s' % ip
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

    def get(self, merchant_uid):
        dd = current_user_data_dict()
        if dd:
            return redirect(url_for('merchant.merchant_index'))
        merchant_data = MerchantTable.find_one({'uuid': merchant_uid})
        if not merchant_data:
            return abort(404)
        context = {
            # 'img_cap': graph_captcha(),
        }
        return render_template('merchant/login.html', **context)

    def post(self, merchant_uid):
        merchant_data = MerchantTable.find_one({'uuid': merchant_uid})
        if not merchant_data:
            return abort(404)
        action = request.form.get('action')
        if action == 'pwdLogin':
            account = request.form.get('account')
            password = request.form.get('password')
            verify_code = request.form.get('verify_code')
            if not account or not password or not account.strip() or not password.strip():
                return xtjson.json_params_error('登录失败!')
            if self.login_limit(account):
                return xtjson.json_params_error('尝试次数过多！请稍后再试...')

            f1 = {'account': account.strip(), '$or': [{'uuid': merchant_uid}, {'upper_mid': merchant_uid}]}
            user_data = MerchantTable.find_one(f1)
            if not user_data:
                return xtjson.json_params_error('该账户不存在!')

            if not MerchantTable.check_password(user_data.get('password'), password.strip()):
                return xtjson.json_params_error('登录失败!')

            if not user_data.get('statu'):
                return xtjson.json_params_error('当前账户不可用!')

            if user_data.get('role_code') == MERCHANT_ROLES.MERCHANT:
                if not user_data.get('is_review'):
                    return xtjson.json_params_error('当前账户不可用！')

            is_activate = None
            # googleObj = GooleVerifyCls(pwd=user_data.get('uuid'), s_label='pay2wold', account=user_data.get('account'))
            # if user_data.get('is_activate'):
            #     if not verify_code:
            #         return xtjson.json_result(code=401, message='请输入GOOGLE验证码！', data={'is_show_qrcode': False})
            #     if not googleObj.check_goole_code(verify_code):
            #         return xtjson.json_result(code=401, message='GOOGLE验证码输入错误！', data={'is_show_qrcode': False})
            # else:
            #     is_activate = True
            #     generate_qrcode = googleObj.secret_generate_qrcode()
            #     if not verify_code:
            #         return xtjson.json_result(code=401, message='请输入GOOGLE验证码！', data={'is_show_qrcode': True, 'generate_qrcode': generate_qrcode})
            #     if not googleObj.check_goole_code(verify_code):
            #         return xtjson.json_result(code=401, message='GOOGLE验证码输入错误！', data={'is_show_qrcode': True, 'generate_qrcode': generate_qrcode})

            upda_dict = {
                'last_login_time': user_data.get('current_login'),
                'last_login_ip': user_data.get('current_login_ip'),
                'current_login': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'current_login_ip': get_ip(),
            }
            if is_activate is not None:
                upda_dict['is_activate'] = is_activate
            MerchantTable.update_one({'account': account.strip()},{'$set': upda_dict})
            session[MERCHANT_USER_SESSION_KEY] = user_data.get('uuid')
            session.permanent = True
            _log_data = {
                'merchant_uuid': user_data.get('uuid'),
                'ip': get_ip(),
                'ua': str(request.user_agent),
                'address': '',
            }
            MerchantLogTable.insert_one(_log_data)
            return xtjson.json_result()
        if action == 'regist_data':
            username = request.form.get('username')
            reg_account = request.form.get('reg_account')
            reg_password = request.form.get('reg_password')
            reg_graph_captcha = request.form.get('reg_graph_captcha')

            if not username or not reg_account or not reg_password or not reg_graph_captcha:
                return xtjson.json_params_error('注册失败！')

            if not checkcap(reg_graph_captcha.strip()):
                return xtjson.json_params_error('验证码输入错误！')

            if self.regist_limit():
                return xtjson.json_params_error('尝试次数过多，请稍后再试！')

            user_data = MerchantTable.find_one({'merchant_name': username.strip(), 'role_code': MERCHANT_ROLES.MERCHANT})
            if user_data:
                return xtjson.json_params_error('该商户名称已存在!')

            user_data = MerchantTable.find_one({'account': reg_account.strip(), 'role_code': MERCHANT_ROLES.MERCHANT})
            if user_data:
                return xtjson.json_params_error('该商户账号已存在!')

            Merchant_uuid = shortuuid.uuid()
            secret_key = encry_md5(Merchant_uuid)
            _data = {
                'merchant_name': username.strip(),
                'account': reg_account.strip(),
                'password': MerchantTable.encry_password(reg_password.strip()),
                'balance_money': 0,
                'statu': True,
                'note': '',
                '_current_login': datetime.datetime.now(),
                'is_activate': False,

                'uuid': Merchant_uuid,
                'secret_key': secret_key,
                'merchant_id': self.get_data_id(),
                'balance_amount': 0,
                'total_balance': 0,
                'is_review': False,
                'payment_rate': 0,
                'issued_money_rate': 0,
                'recharge_money_rate': 0,
                'agentadmin_uuid': agentadmin_id,
                'collect_money_switch': True,
                'paybehalf_switch': True,
                'role_code': MERCHANT_ROLES.MERCHANT,
            }
            MerchantTable.insert_one(_data)

            for tt in TunnelTable.find_many({}):
                _data = {
                    'tunnle_id': tt.get('uuid'),
                    'statu': False,
                    'single_amount_max': 999999999999999,
                    'single_amount_min': 0,
                    'merchant_uuid': Merchant_uuid,
                    'rate': 0,
                    'tunnle_method': TUNNLE_METHOD.collection,
                }
                MerchantTunnleTable.insert_one(_data)

            return xtjson.json_result(message='注册成功!')

        return xtjson.json_params_error('操作失败!')

