# -*- coding: utf-8 -*-
import os
import time
import random
import datetime
import shortuuid
from flask import views, render_template, abort, request, current_app, redirect
from . import bp
from modules.view_helpres.tool_func import front_risk_control
from models.pay_table import BankTable, CollectionOrderTable, MerchantTable, BankCardBillTable, BankCardTable, order_bankcard_bind_table
from modules.view_helpres.view_func import getAvailableBankcard, getBankPayQrcode
from models.cms_user import CmsUserTable
from constants import ROlE_ALL, PAY_METHOD
from common_utils.lqredis import SiteRedis
from common_utils.utils_funcs import img_base4_save, img_to_base64


@bp.before_request
def site_before_request():
    statu, res = front_risk_control()
    if not statu:
        return res



class FrontIndex(views.MethodView):
    add_url_rules = [['/', 'front_index']]

    def get(self):
        return redirect('https://www.pay2world.vip/')



class PayBankSelectView(views.MethodView):
    add_url_rules = [['/pay/bankSelect/<string:orderId>', 'pay_view']]

    def get(self, orderId):
        context = {}
        orderdata = CollectionOrderTable.find_one({'order_id': orderId})
        if not orderdata:
            return abort(404)

        if orderdata.get('bankcard_id'):
            return abort(404)

        merchant_data = MerchantTable.find_one({'merchant_id': orderdata.get('merchant_id')}) or {}
        agentadmin_uuid = merchant_data.get('agentadmin_uuid')
        agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid, 'role_code': ROlE_ALL.AGENTADMIN})
        if not agentadmin_data:
            return abort(404)

        usable_bankcard_datas = orderdata.get('usable_bankcard_datas') or []
        if not usable_bankcard_datas:
            return abort(404)

        bank_datas = []
        for dad in usable_bankcard_datas:
            bank_data = BankTable.find_one({'uuid': dad.get('bank_uid')})
            if not bank_data:
                continue

            _data = {
                'url': f'/pay/{ bank_data.get("code") }/{ orderId }',
                'local_logo': bank_data.get('local_logo'),
            }
            if _data not in bank_datas:
             bank_datas.append(_data)

        if not bank_datas:
            return abort(404)

        logoUrl = merchant_data.get('logoUrl') or ''
        random.shuffle(bank_datas)
        context['bank_datas'] = bank_datas
        context['logoUrl'] = logoUrl or '/assets/world/images/PAY2WORLD2.png'
        return render_template('front/bankSelect.html', **context)



class PayBankView(views.MethodView):
    add_url_rules = [['/pay/<string:bank>/<string:orderId>', 'PayBank_view']]

    def format_money(self, data):
        try:
            if '.' in str(data):
                _V = round(float(data), 2)
                return format(float(_V), ",")
            return format(int(data), ",")
        except:
            return data

    def get(self, bank, orderId):
        cck = 'pay2w_pay_orderid_' + orderId
        kvv = SiteRedis.get(cck)
        if not kvv:
            SiteRedis.set(cck, 1, expire=60)
        else:
            kvv = kvv.decode()
            if int(kvv) >= 30:
                return abort(404)
            SiteRedis.set(cck, int(kvv)+1, expire=60)

        order_data = CollectionOrderTable.find_one({'order_id': orderId})
        if not order_data:
            return abort(404)

        crr_bankcard_id = order_data.get('bankcard_id')
        skk = 'pay_bindbankcard_' + orderId
        if not crr_bankcard_id:
            _vv = SiteRedis.incrby(skk)
            SiteRedis.expire(skk, time=30)
            if _vv > 1:
                return abort(404)

        merchant_data = MerchantTable.find_one({'merchant_id': order_data.get('merchant_id')}) or {}
        order_time = order_data.get('order_time')
        orderend_time = order_time + datetime.timedelta(minutes=15)
        if datetime.datetime.now() >= orderend_time:
            return '订单已失效！'

        if order_data.get('pay_statu'):
            return '订单已失效！'

        bank_data = BankTable.find_one({'code': bank})
        if not bank_data:
            return abort(404)
        agentadmin_uuid = merchant_data.get('agentadmin_uuid')
        agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid, 'role_code': ROlE_ALL.AGENTADMIN})
        if not agentadmin_data:
            return abort(404)

        pay_method = order_data.get('pay_method')
        if not crr_bankcard_id:
            bank_ids = []
            bank_ids.append(bank_data.get('uuid'))
            usable_bankcard_datas = order_data.get('usable_bankcard_datas') or []
            if not usable_bankcard_datas:
                return abort(404)
            bankcard_datas = []
            for bd in usable_bankcard_datas:
                if bd.get('bank_uid') in bank_ids:
                    bankcard_datas.append(bd)

            bankcard_data = random.choice(bankcard_datas)
            CollectionOrderTable.update_one({'uuid': order_data.get('uuid')}, {'$set': {
                'bankcard_id': bankcard_data.get('uuid'), 'bank_code': bank_data.get('code'),
                'payee_bankcard': bankcard_data.get('account'), 'payee_username': bankcard_data.get('account_username'), 'usable_bankcard_datas': []
            }})
            obbt = {
                'order_id': orderId,
                'merchant_order_id': order_data.get('merchant_order_id'),
                'payee_bankcard': bankcard_data.get('account'),
            }
            order_bankcard_bind_table.insert_one(obbt)
        else:
            bankcard_data = BankCardTable.find_one({'uuid': crr_bankcard_id}) or {}
            if not bankcard_data:
                return abort(404)

        payqrcode_url = order_data.get('payqrcode_url') or ''
        project_static_folder = os.path.join(current_app.static_folder, current_app.config.get('PROJECT_NAME'))
        _state, payQrcode = getBankPayQrcode(
            order_data.get('uuid'),
            order_data.get('order_amount'),
            order_data.get('bank_memo'),
            bank_data,
            payqrcode_url=payqrcode_url,
            project_static_folder=project_static_folder,
            receive_account=bankcard_data.get('account'),
        )
        if not _state:
            return 'pay error!'

        context = {
            'is_back': order_data.get('back_url') or '',
            'orderUuid': order_data.get('uuid'),
            'time': int(time.time()),
            'payQrcode': payQrcode,
            'bank_data': bank_data,
            'order_data': order_data,
            'bankcard_data': bankcard_data,
            'orderId': orderId,
            'orderend_time': orderend_time.strftime('%Y-%m-%d %H:%M:%S'),
            'crr_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'format_money': self.format_money,
        }
        if pay_method == PAY_METHOD.VNBANKQR or pay_method == PAY_METHOD.VNBANKQR2:
            template = 'front/pay2.html'
        else:
            return 'pay error!'
        SiteRedis.dele(skk)
        
        return render_template(template, **context)



class PayOrderView(views.MethodView):
    add_url_rules = [['/pay/order/<string:orderId>', 'PayOrder_View']]

    def get(self, orderId):
        cck = 'pay2w_pay_orderid_' + orderId
        kvv = SiteRedis.get(cck)
        if not kvv:
            SiteRedis.set(cck, 1, expire=60)
        else:
            kvv = kvv.decode()
            if int(kvv) >= 30:
                return abort(404)
            SiteRedis.set(cck, int(kvv)+1, expire=60)

        order_data = CollectionOrderTable.find_one({'order_id': orderId})
        if not order_data:
            return abort(404)

        crr_bankcard_id = order_data.get('bankcard_id')
        skk = 'pay_bindbankcard_' + orderId
        if not crr_bankcard_id:
            _vv = SiteRedis.incrby(skk)
            SiteRedis.expire(skk, time=30)
            if _vv > 1:
                return abort(404)

        merchant_data = MerchantTable.find_one({'merchant_id': order_data.get('merchant_id')}) or {}
        order_time = order_data.get('order_time')
        orderend_time = order_time + datetime.timedelta(minutes=15)
        if datetime.datetime.now() >= orderend_time:
            return '订单已失效！'

        if order_data.get('pay_statu'):
            return '订单已失效！'

        bank_datas = BankTable.find_many({'statu': True})
        if not bank_datas:
            return abort(404)

        agentadmin_uuid = merchant_data.get('agentadmin_uuid')
        agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid, 'role_code': ROlE_ALL.AGENTADMIN})
        if not agentadmin_data:
            return abort(404)

        pay_method = order_data.get('pay_method')
        if not crr_bankcard_id:
            bank_ids = []
            for bb in bank_datas:
                bank_ids.append(bb.get('uuid'))

            # state, bankcard_datas = getAvailableBankcard(order_data.get('order_amount'), agentadmin_data, bank_ids=bank_ids, is_merchant_uid=merchant_data.get('uuid'), payMethod=order_data.get('pay_method'))
            # if not state:
            #     return abort(404)
            usable_bankcard_datas = order_data.get('usable_bankcard_datas') or []
            if not usable_bankcard_datas:
                return abort(404)
            bankcard_datas = []
            for bd in usable_bankcard_datas:
                if bd.get('bank_uid') in bank_ids:
                    bankcard_datas.append(bd)

            bankcard_data = random.choice(bankcard_datas)
            bank_data = BankTable.find_one({'uuid': bankcard_data.get('bank_uid')}) or {}
            if not bank_data:
                return abort(404)

            CollectionOrderTable.update_one({'uuid': order_data.get('uuid')}, {'$set': {
                'bankcard_id': bankcard_data.get('uuid'), 'bank_code': bank_data.get('code'),
                'payee_bankcard': bankcard_data.get('account'), 'payee_username': bankcard_data.get('account_username'), 'usable_bankcard_datas': []
            }})
            obbt = {
                'order_id': orderId,
                'merchant_order_id': order_data.get('merchant_order_id'),
                'payee_bankcard': bankcard_data.get('account'),
            }
            order_bankcard_bind_table.insert_one(obbt)
        else:
            bankcard_data = BankCardTable.find_one({'uuid': crr_bankcard_id}) or {}
            if not bankcard_data:
                return abort(404)
            bank_data = BankTable.find_one({'uuid': bankcard_data.get('bank_uid')}) or {}
            if not bank_data:
                return abort(404)

        payqrcode_url = order_data.get('payqrcode_url') or ''
        project_static_folder = os.path.join(current_app.static_folder, current_app.config.get('PROJECT_NAME'))
        _state, payQrcode = getBankPayQrcode(
            order_data.get('uuid'),
            order_data.get('order_amount'),
            order_data.get('bank_memo'),
            bank_data,
            payqrcode_url=payqrcode_url,
            project_static_folder=project_static_folder,
            receive_account=bankcard_data.get('account'),
        )
        if not _state:
            return 'pay error!'

        context = {
            'is_back': order_data.get('back_url') or '',
            'orderUuid': order_data.get('uuid'),
            'merchant_order_id': order_data.get('merchant_order_id'),
            'time': int(time.time()),
            'payQrcode': payQrcode,
            'bank_data': bank_data,
            'order_data': order_data,
            'bankcard_data': bankcard_data,
            'orderId': orderId,
            'orderend_time': orderend_time.strftime('%Y-%m-%d %H:%M:%S'),
            'crr_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        if pay_method in [PAY_METHOD.VNZALO, PAY_METHOD.VNZA2LO]:
            template = 'front/zaloPay.html'
        elif pay_method in [PAY_METHOD.VNVTPAY, PAY_METHOD.VNVT2PAY]:
            template = 'front/ViettelPay.html'
        elif pay_method in [PAY_METHOD.VNMOMO, PAY_METHOD.VNMO2MO]:
            template = 'front/MoMo.html'
        else:
            return 'pay error!'
        SiteRedis.dele(skk)
        return render_template(template, **context)



class DocView(views.MethodView):
    add_url_rules = [['/doc/<string:payType>.html', 'doc_view']]

    def get(self, payType):
        context = {}
        if payType == 'payDoc':
            template = '/front/pay_doc.html'
        elif payType == 'behalfPay':
            template = '/front/behalfPay_doc.html'
        else:
            return abort(404)

        return render_template(template, **context)



class PaySuccessView(views.MethodView):
    add_url_rules = [['/pay/sucess/<string:order_id>', 'pay_success_view']]

    def get(self, order_id):
        order_data = CollectionOrderTable.find_one({'order_id': order_id})
        if not order_data:
            return abort(404)
        context = {
            'callback_url': order_data.get('callback_url'),
            'amount': order_data.get('actual_amount'),
        }
        return render_template('front/pay_success.html', **context)

