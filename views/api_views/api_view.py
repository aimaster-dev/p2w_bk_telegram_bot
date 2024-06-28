# -*- coding: utf-8 -*-
import datetime
import json
import random
import string
import time
import os
import shortuuid
from flask import views, request, abort, current_app
from common_utils import xtjson
from common_utils.utils_funcs import encry_md5, is_valid_url, get_ip
from models.pay_table import CollectionOrderTable, MerchantTable, BankTable, ApiRequestLogTable, BankCardBillTable, BankCardTable
from modules.view_helpres.view_func import pay_api_control_func, payBehalf_deduct, behalfPayCallbackOrderFunc, payBehalf_goback, getBehalfPayOrderId, getAvailableBankcard, getBankPayQrcode
from constants import PAY_METHOD, CallbackState, BANK_CODE, taskStatus, ROlE_ALL, REQUEST_METHOD, CHECK_ANAME_STATES
from site_exts import mc
from models.behalfPay import behalfPayOrderTable, behalfPayScriptTable, behalfPayTaskTable, behalfPayOrderProcessTable, behalfPayCallbackLogTable, CnBankCardTable
from models.cms_user import CmsUserTable
from models.cms_table import SiteConfigTable
from common_utils.lqredis import SiteRedis
from modules.bank_module.checkcardName.CHACK_ACB import ACB_CLS



class payApi(views.MethodView):
    '''
    代收订单接口
    '''
    add_url_rules = [['/pay', 'pay_api']]

    def add_api_log(self, text='', log_data={}, code=200):
        _data = {}
        _data.update(log_data)
        _data['response_code'] = code
        _data['response_text'] = text
        ApiRequestLogTable.insert_one(_data)

    def getOrderId(self, mdl):
        while True:
            fff = list('ABCDEFGHJKLMNPQRSTUVWXYZABCDEFGHJKLMNPQRSTUVWXYZ')
            text = 'R'
            crr_Date = datetime.datetime.now()
            crr_day = crr_Date.day
            text += fff[crr_day]
            text += str(mdl)
            for i in range(7):
                ssd = list(string.digits)
                random.shuffle(ssd)
                text += random.choice(ssd)
            if CollectionOrderTable.find_one({'order_id': text}):
                continue
            return text

    def other_api_func(self, orderId, log_dict):
        orderdata = CollectionOrderTable.find_one({'order_id': orderId})
        if not orderdata:
            self.add_api_log(text='订单创建失败', log_data=log_dict, code=413)
            return xtjson.json_params_error('订单创建失败')

        merchant_data = MerchantTable.find_one({'merchant_id': orderdata.get('merchant_id')}) or {}
        agentadmin_uuid = merchant_data.get('agentadmin_uuid')
        agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid, 'role_code': ROlE_ALL.AGENTADMIN})
        if not agentadmin_data:
            self.add_api_log(text='订单创建失败', log_data=log_dict, code=415)
            return xtjson.json_params_error('订单创建失败')

        usable_bankcard_datas = orderdata.get('usable_bankcard_datas') or []
        if not usable_bankcard_datas:
            self.add_api_log(text='无可用收款方式！', log_data=log_dict, code=400)
            return xtjson.json_params_error('无可用收款方式')

        bankcard_datas = []
        for dad in usable_bankcard_datas:
            bank_data = BankTable.find_one({'uuid': dad.get('bank_uid')})
            if not bank_data:
                continue
            _data = {
                'bankName': bank_data.get('shortName'),
                'bankLogo': f'https://{current_app.config.get("MAIN_DOMAIN")}' + bank_data.get('local_logo'),
                'bankcard_data': dad,
                'bank_data': bank_data,
            }
            if _data not in bankcard_datas:
             bankcard_datas.append(_data)
        t_bankcard_data = random.choice(bankcard_datas)

        CollectionOrderTable.update_one({'uuid': orderdata.get('uuid')}, {'$set': {
            'bankcard_id': t_bankcard_data.get('bankcard_data').get('uuid'), 'bank_code': t_bankcard_data.get('bank_data').get('code'),
            'payee_bankcard': t_bankcard_data.get('bankcard_data').get('account'), 'payee_username': t_bankcard_data.get('bankcard_data').get('account_username'),
        }})

        payqrcode_url = orderdata.get('payqrcode_url') or ''
        project_static_folder = os.path.join(current_app.static_folder, current_app.config.get('PROJECT_NAME'))
        _state, payQrcode = getBankPayQrcode(
            orderdata.get('uuid'),
            orderdata.get('order_amount'),
            orderdata.get('bank_memo'),
            t_bankcard_data.get('bank_data'),
            payqrcode_url=payqrcode_url,
            project_static_folder=project_static_folder,
            receive_account=t_bankcard_data.get('bankcard_data').get('account'),
            is_base=False
        )
        if not _state:
            self.add_api_log(text='支付码创建失败！', log_data=log_dict, code=400)
            return xtjson.json_params_error('支付码创建失败！')

        payUrl = ''
        if orderdata.get('pay_method') == PAY_METHOD.VNBANKQR2:
            payUrl = f'https://{current_app.config.get("MAIN_DOMAIN")}/pay/{ t_bankcard_data.get("bank_data").get("code") }/{ orderId }'
        if orderdata.get('pay_method') in [PAY_METHOD.VNMO2MO,PAY_METHOD.VNVT2PAY,PAY_METHOD.VNZA2LO]:
            payUrl = f'https://{current_app.config.get("MAIN_DOMAIN")}/pay/order/' + orderId
        _restule = {
            "bankName": t_bankcard_data.get('bankName'),
            "bankLogo": t_bankcard_data.get('bankLogo'),
            "bankAccount": t_bankcard_data.get('bankcard_data').get('account'),
            "bankOwner": t_bankcard_data.get('bankcard_data').get('account_username'),
            "payQrcode": f'https://{current_app.config.get("MAIN_DOMAIN")}' + payQrcode,
            "bankMemo": orderId,
            "payUrl": payUrl,
        }
        log_dict['response_text'] = json.dumps(_restule)
        self.add_api_log(text=payUrl, log_data=log_dict)
        return xtjson.json_result(data=_restule)

    def get(self):
        return '请使用POST请求！'

    def post(self):
        log_dict = {
            "request_method": REQUEST_METHOD.POST,
            "url_path": str(request.path),
            'ip': str(get_ip()),
        }
        request_data = {}
        try:
            if request.form:
                for k, v in request.form.items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
            if request.data:
                for k, v in json.loads(request.data.decode()).items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
            if request.json:
                for k, v in request.json.items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
        except Exception as e:
            log_dict['response_code'] = 400
            log_dict['response_text'] = '数据解析失败!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('数据解析失败！')
        log_dict['request_data'] = json.dumps(request_data)

        mchId = request_data.get('mchId') or ''
        mchOrderId = request_data.get('mchOrderId') or ''
        amount = request_data.get('amount') or 0
        payMethod = request_data.get('payMethod') or ''
        notifyUrl = request_data.get('notifyUrl') or ''
        backUrl = request_data.get('backUrl') or ''
        bankCode = request_data.get('bankCode') or ''
        bankAccountName = request_data.get('bankAccountName') or ''
        bankMemo = request_data.get('bankMemo') or ''
        is_revise_wrong_amount = request_data.get('is_revise_wrong_amount') or ''
        is_return_qr = request_data.get('is_return_qr') or ''
        sign = request_data.get('sign') or ''
        bt = ['mchId', 'mchOrderId', 'amount', 'payMethod', 'notifyUrl', 'sign']
        for btt in bt:
            _v = str(request_data.get(btt) or '')
            if not _v or not _v.strip():
                _text = f'{btt}: 不可为空！'
                self.add_api_log(text=_text, log_data=log_dict, code=400)
                return xtjson.json_params_error(_text)
        mchId = str(mchId or '')

        _state, msg = is_valid_url(notifyUrl)
        if not _state:
            _text = 'notifyUrl：参数错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)
        
        if backUrl:
            _state, msg = is_valid_url(backUrl.strip())
            if not _state:
                _text = 'notifyUrl：参数错误！'
                self.add_api_log(text=_text, log_data=log_dict, code=400)
                return xtjson.json_params_error(_text)
        
        if bankCode and bankCode.strip() and not bankCode.strip().isalpha():
            _text = 'bankCode: 数据错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if bankCode and bankCode not in BANK_CODE:
            _text = 'BANK_CODE：银行代码错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if is_revise_wrong_amount and is_revise_wrong_amount not in ['0', '1']:
            _text = 'is_revise_wrong_amount: 参数错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if is_return_qr and is_return_qr not in ['0', '1']:
            _text = 'is_return_qr: 参数错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        merchant_data = MerchantTable.find_one({'merchant_id': str(mchId)})
        if not merchant_data:
            _text = 'mchId：数据错误03！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if not merchant_data.get('collect_money_switch'):
            _text = '业务暂不可用！'
            self.add_api_log(text=_text, log_data=log_dict, code=421)
            return xtjson.json_params_error(_text)

        if CollectionOrderTable.find_one({'merchant_order_id': mchOrderId.strip()}):
            _text = 'mchOrderId：不可重复！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        reqks = list(request_data.keys())
        reqks.sort()
        dataStr = ''
        for k in reqks:
            if k == 'sign':
                continue
            _v = request_data.get(k) or ''
            dataStr += f'&{k}={_v}'
        dataStr += '&sign='+merchant_data.get('secret_key')
        mtext = encry_md5(dataStr.strip('&'))
        print('mtext:', mtext)
        print('sign:', sign)
        if mtext != sign:
            _text = '解签验证失败！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if bankMemo and bankMemo.strip():
            try:
                bankMemo = str(bankMemo).strip().replace(' ', '')
            except:
                _text = 'bankMemo: 数据错误01！'
                self.add_api_log(text=_text, log_data=log_dict, code=400)
                return xtjson.json_params_error(_text)
            if not bankMemo.isalnum():
                _text = 'bankMemo: 数据错误01！'
                self.add_api_log(text=_text, log_data=log_dict, code=400)
                return xtjson.json_params_error(_text)
            if CollectionOrderTable.find_one({'bank_memo': bankMemo.strip()}):
                _text = 'bankMemo: 数据错误01！'
                self.add_api_log(text=_text, log_data=log_dict, code=400)
                return xtjson.json_params_error(_text)

        if payMethod not in PAY_METHOD.name_arr:
            _text = 'payMethod: 参数错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if not str(amount).isdigit():
            _text = 'amount: 参数错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        try:
            amount = int(amount)
        except:
            _text = 'amount: 数据错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        state, result = pay_api_control_func(merchant_data, amount, payMethod, bankCode)
        if not state:
            self.add_api_log(text=str(result), log_data=log_dict, code=400)
            return xtjson.json_params_error(result)

        merchantTunnle_data = result.get('merchantTunnle_data') or {}
        usable_bankcard_datas = result.get('bankcard_datas') or []
        rate = merchantTunnle_data.get('rate') or 0
        repay_amount = round(amount * rate, 2)

        with mc.lock('insert_order'):
            _md = mchId[-3:]
            order_id = self.getOrderId(_md)
            # bank_memo = bankMemo or order_id
            bank_memo = order_id

            _order_daat = {
                'merchant_id': mchId,
                'merchant_order_id': mchOrderId,
                'order_id': order_id,
                'order_amount': amount,
                'bankcard_id': '',
                'repay_amount': repay_amount,
                'actual_amount': 0,
                'order_time': datetime.datetime.now(),
                'pay_statu': False,
                'force_ispay': False,
                'callback_statu': CallbackState.NOT_CALLEDBACK,
                'callback_url': notifyUrl,
                'back_url': backUrl or '',
                'bank_account_name': bankAccountName or '',
                'bank_memo': bank_memo,
                'sign': sign,
                'ip': get_ip(),
                'is_lose': False,
                'lose_reason': '',

                'pay_method': payMethod,
                'bankCode': bankCode or '',
                'bank_code': bankCode or '',
                'is_revise_wrong_amount': is_revise_wrong_amount or '',
                'is_return_qr': is_return_qr or '',
                'request_data': request_data,
                'agentadmin_uuid': merchant_data.get('agentadmin_uuid'),
                'usable_bankcard_datas': usable_bankcard_datas,
            }
            CollectionOrderTable.insert_one(_order_daat)
        payUrl = ''
        if payMethod == PAY_METHOD.VNBANKQR:
            payUrl = f'https://{current_app.config.get("MAIN_DOMAIN")}/pay/bankSelect/' + order_id
        if payMethod in [PAY_METHOD.VNZALO, PAY_METHOD.VNMOMO, PAY_METHOD.VNVTPAY]:
            payUrl = f'https://{current_app.config.get("MAIN_DOMAIN")}/pay/order/' + order_id
        if payMethod in [PAY_METHOD.VNMO2MO,PAY_METHOD.VNVT2PAY,PAY_METHOD.VNZA2LO, PAY_METHOD.VNBANKQR2]:
            return self.other_api_func(order_id, log_dict)

        self.add_api_log(text=payUrl, log_data=log_dict)
        return xtjson.json_result(data={'payUrl': payUrl})



class payOrderQuery(views.MethodView):
    '''
    代收订单查询接口
    '''
    add_url_rules = [['/pay/order/Query', 'pay_order_query']]

    def add_api_log(self, text='', log_data={}, code=200):
        _data = {}
        _data.update(log_data)
        _data['response_code'] = code
        _data['response_text'] = text
        ApiRequestLogTable.insert_one(_data)

    def get(self):
        return abort(404)

    def post(self):
        log_dict = {
            "request_method": REQUEST_METHOD.POST,
            "url_path": str(request.path),
            'ip': str(get_ip()),
        }
        request_data = {}
        try:
            if request.form:
                for k, v in request.form.items():
                    request_data[k] = v
            if request.data:
                for k, v in json.loads(request.data).items():
                    request_data[k] = v
            if request.json:
                for k, v in request.json.items():
                    request_data[k] = v
        except:
            log_dict['response_code'] = 400
            log_dict['response_text'] = '数据解析失败!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('数据解析失败！')
        log_dict['request_data'] = json.dumps(request_data)

        mchId = request_data.get('mchId') or ''
        orderId = request_data.get('orderId') or ''
        mchOrderId = request_data.get('mchOrderId') or ''
        is_bot = request_data.get('is_bot') or ''
        sign = request_data.get('sign') or ''
        if not mchId or not mchId.strip() or not sign or not sign.strip():
            _text = '数据参数错误！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        if not orderId and not mchOrderId:
            _text = '数据错误-1！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        merchant_data = MerchantTable.find_one({'merchant_id': mchId})
        if not merchant_data:
            _text = '数据错误-2！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error(_text)

        fff1 = {
            'merchant_id': mchId,
            '$or': [{'merchant_order_id': mchOrderId}, {'order_id': orderId}]
        }
        order_data = CollectionOrderTable.find_one(fff1)
        if not order_data:
            _text = '订单查询失败！'
            self.add_api_log(text=_text, log_data=log_dict, code=400)
            return xtjson.json_params_error('订单查询失败！')

        data = {
            'isPaid': '1' if order_data.get('pay_statu') else '0',
            'isGotReceipt': '1' if order_data.get('callback_statu') == CallbackState.SUCCESS else '0',
            'amount': order_data.get('order_amount'),
            'payAmount': order_data.get('actual_amount') or 0,
            'costFee': order_data.get('repay_amount') or 0,
            'createdAt': order_data.get('order_time') or 0,
            'paidAt': order_data.get('pay_time') or 0,
        }
        if is_bot:
            data['orderId'] = order_data.get('order_id')
            data['merchantOrderId'] = order_data.get('merchant_order_id')
        message = ''
        if order_data.get('is_lose'):
            message = order_data.get('lose_reason') or ''
        self.add_api_log(text='', log_data=log_dict)
        return xtjson.json_result(data=data, message=message)



class OrderPayTask(views.MethodView):
    '''
    订单验证任务
    '''
    add_url_rules = [['/pay/order/task', 'pay_order_task']]

    def get(self):
        return abort(404)

    def post(self):
        action = request.form.get('action')
        if action == 'getTaskList':
            datas = CollectionOrderTable.find_many({
                'pay_statu': False,
            }, sort=[['order_time', 1]], limit=100)
            if not datas:
                return xtjson.json_result(message='暂无可执行任务！')
            all_datas = []
            for d in datas:
                _d = {
                    'data_uuid': d.get('uuid'),
                    'bank_memo': d.get('bank_memo'),
                }
                all_datas.append(_d)
            return xtjson.json_result(data={'datas': datas})



class OrderQueryApi(views.MethodView):
    '''
    订单查询
    '''
    add_url_rules = [['/order/Query/', 'order_query_api']]

    def get(self):
        return abort(404)

    def post(self):
        action = request.form.get('action')
        if action == 'queryStatu':
            orderUid = request.form.get('orderUid')
            qtime = request.form.get('time')
            if not orderUid or not qtime:
                return xtjson.json_params_error()

            if int(time.time()) - int(qtime) > 60*30:
                return xtjson.json_result(data={'is_state': False, 'finish': True})

            order_data = CollectionOrderTable.find_one({'uuid': orderUid})
            if not order_data:
                return xtjson.json_params_error()

            if order_data.get('pay_statu'):
                return xtjson.json_result(data={'is_state': True, 'finish': True})

            return xtjson.json_result(data={'is_state': False})
        return xtjson.json_params_error()



class behalfPayApi(views.MethodView):
    '''
    代付订单接口
    '''
    add_url_rules = [['/behalfPay/bill', 'behalfPay_bill']]

    def add_request_log(self, request_data={}, request_method=REQUEST_METHOD.POST, response_code=200, response_text=''):
        log_dict = {
            "request_method": request_method,
            "request_data": json.dumps(request_data),
            "url_path": str(request.path),
            'ip': str(get_ip()),
            'response_code': response_code,
            'response_text': response_text,
        }
        ApiRequestLogTable.insert_one(log_dict)

    def selcet_outm_user(self, amount, agentadmin_data):
        sys_payorder = True
        if agentadmin_data.get('system_paybehalf'):
            udatas = CmsUserTable.find_many({'role_code': ROlE_ALL.SYS_OUT_MONEY_USER, 'statu': True, 'is_online': True}) or []
        else:
            sys_payorder = False
            udatas = CmsUserTable.find_many({'role_code': ROlE_ALL.OUT_MONEY_USER, 'agentadmin_uuid': agentadmin_data.get('uuid'), 'statu': True, 'is_online': True}) or []
        _datas = []
        for ud in udatas:
            outm_min_money = ud.get('outm_min_money') or 0
            outm_max_money = ud.get('outm_max_money') or 0
            if not outm_max_money and not outm_min_money:
                _datas.append(ud)
                continue
            if outm_min_money and not outm_max_money and outm_min_money <= amount:
                _datas.append(ud)
                continue
            if outm_max_money and not outm_min_money and outm_max_money >= amount:
                _datas.append(ud)
                continue
            if outm_min_money and outm_max_money and outm_min_money <= amount and outm_max_money >= amount:
                wcl_count = behalfPayOrderTable.count({'out_money_userid': ud.get('uuid'), 'callback_statu': CallbackState.NOT_CALLEDBACK}) or 0
                ud['wcl_count'] = wcl_count
                _datas.append(ud)
        if not _datas:
            return
        _datas = sorted(_datas, key=lambda x: x['wcl_count'])
        _udd = _datas[0]
        return _udd.get('uuid'), sys_payorder

    def post(self):
        request_data = {}
        try:
            if request.form:
                request_data = request.form.to_dict()
            if request.data:
                for k, v in json.loads(request.data.decode()).items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
            if request.json:
                for k, v in request.json.items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
        except Exception as e:
            self.add_request_log(response_code=401, response_text='数据解析错误!')
            return xtjson.json_params_error('数据解析错误！', code=401)

        print('*-' *60)
        print('request_data:', request_data)
        print('*-' *60)
        mchId = request_data.get('mchId') or ''
        mchOrderId = request_data.get('mchOrderId') or ''
        amount = request_data.get('amount') or 0
        notifyUrl = request_data.get('notifyUrl') or ''
        bankCode = request_data.get('bankCode') or ''
        bankAccount = request_data.get('bankAccount') or ''
        bankOwner = request_data.get('bankOwner') or ''
        sign = request_data.get('sign') or ''
        bt = ['mchId', 'mchOrderId', 'amount', 'notifyUrl', 'bankCode', 'bankAccount', 'bankOwner', 'sign']
        for btt in bt:
            _v = str(request_data.get(btt) or '')
            if not _v or not _v.strip():
                self.add_request_log(request_data=request_data, response_code=402, response_text=f'{btt}: 不可为空！')
                return xtjson.json_params_error(f'{btt}: 不可为空！',code=402)

        _state, msg = is_valid_url(notifyUrl)
        if not _state:
            self.add_request_log(request_data=request_data, response_code=403, response_text='notifyUrl：参数错误！')
            return xtjson.json_params_error('notifyUrl：参数错误！',code=403)

        if not bankCode or not bankCode.strip() or not bankCode.strip().isalpha():
            self.add_request_log(request_data=request_data, response_code=403, response_text='bankCode：参数错误！')
            return xtjson.json_params_error('bankCode: 参数错误！',code=403)

        if not str(amount).isdigit():
            self.add_request_log(request_data=request_data, response_code=403, response_text='totalAmount: 参数错误！')
            return xtjson.json_params_error('totalAmount: 参数错误！',code=403)

        try:
            amount = int(amount)
        except:
            self.add_request_log(request_data=request_data, response_code=403, response_text='totalAmount: 参数错误！')
            return xtjson.json_params_error('totalAmount: 参数错误！',code=403)

        bank_data = BankTable.find_one({'code': bankCode.strip()})
        if not bank_data:
            self.add_request_log(request_data=request_data, response_code=403, response_text='bankCode：参数错误！')
            return xtjson.json_params_error('bankCode: 参数错误！',code=403)

        merchant_data = MerchantTable.find_one({'merchant_id': str(mchId)})
        if not merchant_data:
            self.add_request_log(request_data=request_data, response_code=403, response_text='mchId：参数错误！')
            return xtjson.json_params_error('mchId：参数错误！', code=403)
        mchId = str(mchId)

        # 检测商户代付功能是否开启
        if not merchant_data.get('paybehalf_switch'):
            _text = '业务暂不可用！'
            self.add_request_log(request_data=request_data, response_code=421, response_text=_text)
            return xtjson.json_params_error(_text)

        paybehalf_min_money = merchant_data.get('paybehalf_min_money') or 10000
        paybehalf_max_money = merchant_data.get('paybehalf_max_money') or 300000000
        if amount < paybehalf_min_money:
            self.add_request_log(request_data=request_data, response_code=410, response_text='金额过小！')
            return xtjson.json_params_error('金额过小！', code=410)
        if amount > paybehalf_max_money:
            self.add_request_log(request_data=request_data, response_code=411, response_text='金额过大！')
            return xtjson.json_params_error('金额过大！', code=411)

        cf_ip = get_ip() or ''
        ip_whitelist = merchant_data.get('ip_whitelist')
        ip_check = False
        if ip_whitelist:
            for pp in cf_ip.split(','):
                if pp in ip_whitelist:
                    ip_check = True
        if ip_whitelist and not ip_check:
            self.add_request_log(request_data=request_data, response_code=406, response_text='异常IP！')
            return xtjson.json_params_error('异常IP！', code=406)

        if behalfPayOrderTable.find_one({'merchant_order_id': mchOrderId.strip()}):
            self.add_request_log(request_data=request_data, response_code=403, response_text='mchOrderId:不可重复！')
            return xtjson.json_params_error('mchOrderId：不可重复！', code=403)

        # 获取商户代理
        agentadmin_data = CmsUserTable.find_one({'uuid': merchant_data.get('agentadmin_uuid'), 'role_code': ROlE_ALL.AGENTADMIN}) or {}
        if not agentadmin_data:
            self.add_request_log(request_data=request_data, response_code=4011, response_text='数据错误！')
            return xtjson.json_params_error()

        # 代付配置检测
        _site_data = SiteConfigTable.find_one({}) or {}
        if agentadmin_data.get('system_paybehalf'):
            maintain_switch = _site_data.get('maintain_switch') or False
            maintain_bankcodes = _site_data.get('maintain_bankcodes') or ''
            maintain_bankcodes = maintain_bankcodes.split(',')
        else:
            maintain_switch = agentadmin_data.get('maintain_switch') or False
            maintain_bankcodes = agentadmin_data.get('maintain_bankcodes') or ''
            maintain_bankcodes = maintain_bankcodes.split(',')
        if not maintain_switch:
            self.add_request_log(request_data=request_data, response_code=407, response_text='当前业务维护中，暂不可用！')
            return xtjson.json_params_error('当前业务维护中，暂不可用！', code=407)
        if bankCode in maintain_bankcodes:
            self.add_request_log(request_data=request_data, response_code=407, response_text=f'{bankCode}：该银行维护中，暂不可用！')
            return xtjson.json_params_error(f'{bankCode}：该银行维护中，暂不可用！', code=407)

        reqks = list(request_data.keys())
        reqks.sort()
        dataStr = ''
        for k in reqks:
            if k == 'sign':
                continue
            _v = request_data.get(k) or ''
            dataStr += f'&{k}={_v}'
        dataStr += '&sign=' + merchant_data.get('secret_key')
        mtext = encry_md5(dataStr.strip('&'))
        if mtext != sign:
            self.add_request_log(request_data=request_data, response_code=409, response_text='解签验证失败！')
            return xtjson.json_params_error('解签验证失败！', code=409)

        rate = merchant_data.get('payment_rate') or 0
        repay_amount = round(amount * rate, 2)

        balance_amount = merchant_data.get('balance_amount') or 0
        if balance_amount < (repay_amount+amount):
            self.add_request_log(request_data=request_data, response_code=408, response_text='商户余额不足！')
            return xtjson.json_params_error('商户余额不足！', code=408)

        check_aname_state = CHECK_ANAME_STATES.C1
        if _site_data.get('check_aname_switch'):
            bbks = CnBankCardTable.find_many({'statu': True})
            if bbks:
                bbk = random.choice(bbks)
                __ccccstate, __Res = False, False
                try:
                    __ccccstate, __Res = ACB_CLS(bbk.get('username'), bbk.get('password'), bbk.get('account')).check_bank_name(bankAccount, bankOwner.strip(), bank_data.get('bin'))
                except:
                    pass
                if __ccccstate:
                    check_aname_state = CHECK_ANAME_STATES.C2
                else:
                    check_aname_state = CHECK_ANAME_STATES.C3
                if __ccccstate and not __Res:
                    self.add_request_log(request_data=request_data, response_code=412, response_text='账户姓名不符！')
                    return xtjson.json_params_error('账户姓名不符！', code=412)

        paybehalf_rate = agentadmin_data.get('paybehalf_rate') or 0
        a_balance_amount = agentadmin_data.get('balance_amount') or 0
        _b_repay_amount = round(repay_amount * paybehalf_rate, 2) + amount
        if a_balance_amount < _b_repay_amount:
            self.add_request_log(request_data=request_data, response_code=4012, response_text='数据错误！')
            return xtjson.json_params_error()
        out_money_userid, sys_payorder = self.selcet_outm_user(amount, agentadmin_data) or ''

        ouuid = shortuuid.uuid()
        with mc.lock('insert_y_order'):
            _md = mchId[-3:]
            order_id = getBehalfPayOrderId(_md)

            _order_daat = {
                'uuid': ouuid,
                'merchant_id': mchId,
                'merchant_order_id': mchOrderId,
                'order_id': order_id,
                'order_amount': amount,
                'actual_amount': 0,
                'repay_amount': repay_amount,
                'order_time': datetime.datetime.now(),
                'pay_statu': False,
                'reject_pay': False,
                'is_task': False,
                'callback_statu': CallbackState.NOT_CALLEDBACK,
                'callback_url': notifyUrl,
                'sign': sign,
                'bank_memo': order_id,
                'out_money_userid': out_money_userid,
                'sys_payorder': sys_payorder,
                'ip': get_ip(),

                'receive_bank_code': bankCode or '',
                'receive_account': bankAccount or '',
                'receive_owner': bankOwner or '',
                'request_data': request_data,
                'agentadmin_uuid': merchant_data.get('agentadmin_uuid'),
                'check_aname_state': check_aname_state,
            }
            behalfPayOrderTable.insert_one(_order_daat)

        behalfPayOrderProcessTable.insert_one({'order_id': order_id, 'text': '创建订单！'})
        payBehalf_deduct(order_uuid=ouuid, merchant_data=merchant_data)
        self.add_request_log(request_data=request_data, response_code=200)
        return xtjson.json_result()



class behalfPayQueryApi(views.MethodView):
    '''
    代付订单接口
    '''
    add_url_rules = [['/behalfPay/Query/<string:reqType>', 'behalfPay_billQuery']]

    def add_request_log(self, request_data={}, request_method=REQUEST_METHOD.POST, response_code=200, response_text=''):
        log_dict = {
            "request_method": request_method,
            "request_data": json.dumps(request_data),
            "url_path": str(request.path),
            'ip': str(get_ip()),
            'response_code': response_code,
            'response_text': response_text,
        }
        ApiRequestLogTable.insert_one(log_dict)

    def post(self, reqType):
        request_data = {}
        try:
            if request.form:
                request_data = request.form.to_dict()
            if request.data:
                for k, v in json.loads(request.data.decode()).items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
        except Exception as e:
            self.add_request_log(response_code=401, response_text='数据解析失败!')
            return xtjson.json_params_error('数据解析失败！', code=401)

        if reqType == 'bill':
            mchId = request_data.get('mchId') or ''
            orderId = request_data.get('orderId') or ''
            mchOrderId = request_data.get('mchOrderId') or ''
            is_bot = request_data.get('is_bot') or ''
            sign = request_data.get('sign') or ''

            if not mchId or not mchId.strip() or not sign or not sign.strip():
                self.add_request_log(request_data=request_data, response_code=402, response_text='缺少参数!')
                return xtjson.json_params_error('缺少参数！', code=402)

            if not orderId and not mchOrderId:
                self.add_request_log(request_data=request_data, response_code=402, response_text='缺少参数!')
                return xtjson.json_params_error('缺少参数！', code=402)

            merchant_data = MerchantTable.find_one({'merchant_id': mchId})
            if not merchant_data:
                self.add_request_log(request_data=request_data, response_code=403, response_text='参数错误!')
                return xtjson.json_params_error('参数错误！', code=403)

            fff1 = {
                'merchant_id': mchId,
                '$or': [{'merchant_order_id': mchOrderId}, {'order_id': orderId}]
            }
            order_data = behalfPayOrderTable.find_one(fff1)
            if not order_data:
                self.add_request_log(request_data=request_data, response_code=405, response_text='无效订单!')
                return xtjson.json_params_error('无效订单！', code=405)
            out_money_user_data = CmsUserTable.find_one({'uuid': order_data.get('out_money_userid')}) or {}

            if order_data.get('reject_pay'):
                isPaid = 2
            elif order_data.get('pay_statu'):
                isPaid = 1
            else:
                isPaid = 0

            testdata = {
                'isPaid': isPaid,
                'isGotReceipt': '1' if order_data.get('callback_statu') == CallbackState.SUCCESS else '0',
                'amount': order_data.get('order_amount') or 0,
                'costFee': order_data.get('repay_amount') or 0,
                'createdAt': order_data.get('order_time').strftime('%Y-%m-%d %H:%M:%S') or '',
                'paidAt': order_data.get('pay_time').strftime('%Y-%m-%d %H:%M:%S') if order_data.get('pay_time') else '',
            }
            if is_bot:
                testdata['orderId'] = order_data.get('order_id')
                testdata['merchantOrderId'] = order_data.get('merchant_order_id')
                testdata['outMoneyUserAccount'] = out_money_user_data.get('account')
            message = ''
            if order_data.get('reject_pay'):
                datcc = behalfPayCallbackLogTable.find_one({'order_uuid': order_data.get('uuid')}, sort=[['create_time', -1]]) or {}
                message = datcc.get('note') or ''

            self.add_request_log(request_data=request_data, response_code=200)
            return xtjson.json_result(data=testdata,message=message)
        if reqType == 'balance':
            mchId = request_data.get('mchId') or ''
            sign = request_data.get('sign') or ''
            if not mchId or not mchId.strip() or not sign or not sign.strip():
                self.add_request_log(request_data=request_data, response_code=402, response_text='缺少参数!')
                return xtjson.json_params_error('缺少参数！', code=402)

            merchant_data = MerchantTable.find_one({'merchant_id': mchId})
            if not merchant_data:
                self.add_request_log(request_data=request_data, response_code=403, response_text='merchant_data: 参数错误!')
                return xtjson.json_params_error('参数错误！', code=403)

            data = {
                'balance': merchant_data.get('balance_amount') or 0,
                'mchId': mchId
            }
            self.add_request_log(request_data=request_data, response_code=200)
            return xtjson.json_result(data=data)


# 代付脚本接口
class behalfPayTaskApi(views.MethodView):

    add_url_rules = [['/behalfPay/task/<string:reqType>', 'behalfPay_task']]

    def getPayTask_func(self, script_Data, log_dict):
        skk = 'pay_get_paytask'
        while True:
            _vv = SiteRedis.incrby(skk)
            if _vv > 1:
                time.sleep(0.5)
                continue
            SiteRedis.expire(skk, time=30)
            break
        end_time = datetime.datetime.now()
        start_time = end_time - datetime.timedelta(minutes=30)
        order_data = behalfPayOrderTable.find_one({'pay_statu': False, 'is_task':False, 'reject_pay':False, 'order_time': {'$gte': start_time, '$lte': end_time}}) or {}
        if not order_data:
            log_dict['response_code']=200
            log_dict['response_text']='暂无可执行订单任务'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_result(message='暂无可执行订单任务', data={'task':{}})

        behalfPayOrderTable.update_one({'uuid': order_data.get('uuid')}, {'$set': {'is_task': True}})
        _task_data = {
            'statu': taskStatus.processing,
            'order_id': order_data.get('order_id'),
            'script_id': script_Data.get('uuid'),
        }
        task_id = behalfPayTaskTable.insert_one(_task_data)
        _update_order = {
            'is_task': True,
            'task_id': task_id,
            'script_id': script_Data.get('uuid'),
        }
        behalfPayOrderTable.update_one({'uuid': script_Data.get('uuid')}, {'$set': _update_order})
        data = {
            'bankCode': order_data.get('receive_bank_code'),
            'bankOwner': order_data.get('receive_owner'),
            'bankAccount': order_data.get('receive_account'),
            'amount': order_data.get('order_amount'),
            'task_id': task_id,
        }
        SiteRedis.dele(skk)
        log_dict['response_code'] = 200
        log_dict['response_text'] = json.dumps(data)
        ApiRequestLogTable.insert_one(log_dict)
        return xtjson.json_result(data=data)

    def payOrderFunc(self, order_data, pay_success=True):
        data_from = {}
        merchant_data = MerchantTable.find_one({'merchant_id': order_data.get('merchant_id')})
        if not merchant_data:
            return xtjson.json_params_error('商户不存在！')

        # 支付成功处理
        if pay_success:
            order_amount = order_data.get('order_amount')
            repay_amount = order_data.get('repay_amount')
            _amount = order_amount + repay_amount

            data_from['actual_amount'] = order_amount
            data_from['force_ispay'] = True
            data_from['pay_statu'] = True
            data_from['pay_time'] = datetime.datetime.now()
            behalfPayOrderTable.update_one({'uuid': order_data.get('uuid')}, {'$set': data_from})

            # 添加订单流程
            behalfPayOrderProcessTable.insert_one({'order_id': order_data.get('order_id'), 'text': '付款成功，处理方式：自动'})

            # 代付回调
            ptext = '手动回调，回调结果：'
            _state, _res = behalfPayCallbackOrderFunc(order_data.get('uuid'))
            if _state:
                ptext += '成功'
            else:
                ptext += '失败'
            behalfPayOrderProcessTable.insert_one({'order_id': order_data.get('order_id'), 'text': ptext})
        else:
            # 支付失败处理
            data_from['reject_pay'] = True
            data_from['dealwith_time'] = datetime.datetime.now()
            behalfPayOrderTable.update_one({'uuid': order_data.get('uuid')},{'$set': data_from})

            # 添加订单流程
            behalfPayOrderProcessTable.insert_one({'order_id': order_data.get('order_id'), 'text': f'支付失败，处理方式：自动'})

            ptext = '自动回调，回调结果：'
            _state,_res = behalfPayCallbackOrderFunc(order_data.get('uuid'), note='c', msg='支付失败！')
            if not _state:
                ptext += '失败'
                behalfPayOrderProcessTable.insert_one({'order_id': order_data.get('order_id'), 'text': ptext})
                return xtjson.json_params_error('回调失败！')

            ptext += '成功'
            behalfPayOrderProcessTable.insert_one({'order_id': order_data.get('order_id'), 'text': ptext})
            payBehalf_goback(order_uuid=order_data.get('uuid'), merchant_data=merchant_data)

    def subTask_func(self, data_json, script_Data, log_dict):
        task_id = data_json.get('task_id')
        state = data_json.get('state')
        balance_amount = data_json.get('balanceAmount') or 0
        msg = data_json.get('msg')
        if not task_id:
            log_dict['response_code'] = 400
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error()

        task_data = behalfPayTaskTable.find_one({'uuid': task_id}) or {}
        if not task_data:
            log_dict['response_code'] = 400
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error()

        if task_data.get('statu') in [taskStatus.successed, taskStatus.failed]:
            log_dict['response_code'] = 409
            log_dict['response_text'] = '任务已结束!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('任务已结束！')

        order_data = behalfPayOrderTable.find_one({'order_id': task_data.get('order_id')})
        if not order_data:
            log_dict['response_code'] = 409
            log_dict['response_text'] = '订单不存在!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('订单不存在！')

        merchant_data = MerchantTable.find_one({'merchant_id': order_data.get('merchant_id')})
        if not merchant_data:
            log_dict['response_code'] = 409
            log_dict['response_text'] = '商户不存在!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('商户不存在！')

        if order_data.get('pay_statu'):
            log_dict['response_code'] = 409
            log_dict['response_text'] = '该订单已支付!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('该订单已支付！')
        if order_data.get('reject_pay'):
            log_dict['response_code'] = 409
            log_dict['response_text'] = '该订单已处理!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('该订单已处理！')

        if state not in ['1', '0']:
            log_dict['response_code'] = 409
            log_dict['response_text'] = '参数错误!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('参数错误！')

        _update_data = {
            'note': msg or ''
        }
        if state == '0':
            _update_data['statu'] = taskStatus.failed
        if state == '1':
            _update_data['statu'] = taskStatus.successed
        behalfPayTaskTable.update_one({'uuid': task_id}, {'$set': _update_data})

        _update_s = {
            'balance_amount': balance_amount,
        }
        behalfPayScriptTable.update_one({'uuid': script_Data.get('uuid')}, {'$set': _update_s})

        if state == '0':
            self.payOrderFunc(order_data, pay_success=False)
        if state == '1':
            self.payOrderFunc(order_data)

        log_dict['response_code'] = 200
        ApiRequestLogTable.insert_one(log_dict)
        return xtjson.json_result()

    def updateBalance_func(self, data_json, script_Data, log_dict):
        updatedata = {}
        device_state = data_json.get('deviceState')
        bankcard_account = data_json.get('bankcardAccount')
        balance_amount = data_json.get('balanceAmount')
        bankcard_state = data_json.get('bankcardState')
        msg = data_json.get('msg')
        # if str(device_state) not in ['0', '1']:
        #     log_dict['response_code'] = 400
        #     log_dict['response_text'] = 'deviceState：数据错误！'
        #     ApiRequestLogTable.insert_one(log_dict)
        #     return xtjson.json_params_error('deviceState：数据错误！')
        if bankcard_account != script_Data.get('bankcard_account'):
            log_dict['response_code'] = 400
            log_dict['response_text'] = '数据错误!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('数据错误！')
        if not str(balance_amount).isdigit():
            log_dict['response_code'] = 400
            log_dict['response_text'] = 'balanceAmount: 参数错误!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('balanceAmount: 参数错误！')
        if str(bankcard_state) not in ['0', '1']:
            log_dict['response_code'] = 400
            log_dict['response_text'] = 'bankcardState：数据错误！'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('bankcardState：数据错误！')
        try:
            balance_amount = int(balance_amount)
        except:
            log_dict['response_code'] = 400
            log_dict['response_text'] = 'balanceAmount: 数据错误!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('balanceAmount: 数据错误！')

        if str(bankcard_state) == '0':
            updatedata['statu'] = False
        updatedata['balance_amount'] = balance_amount
        behalfPayScriptTable.update_one({'uuid': script_Data.get('uuid')}, {'$set': updatedata})

        log_dict['response_code'] = 200
        ApiRequestLogTable.insert_one(log_dict)
        return xtjson.json_result()

    def post(self, reqType):
        try:
            data_json = request.form.to_dict()
            if not data_json:
                data_json = request.json
        except:
            return xtjson.json_params_error()

        desktop_id = data_json.get('desktop_id')
        device_id = data_json.get('device_id')
        sign = data_json.get('sign')

        log_dict = {
            "request_method": REQUEST_METHOD.POST,
            "request_data": json.dumps(request.form.to_dict()),
            "url_path": str(request.path),
            'ip': str(get_ip()),
        }
        if not desktop_id or not device_id or not sign:
            log_dict['response_code']=400
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error()

        script_Data = behalfPayScriptTable.find_one({'desktop_id': desktop_id, 'device_id': device_id})
        if not script_Data:
            log_dict['response_code']=400
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error()

        dataStr = f'desktop_id={desktop_id}&device_id={device_id}&sign={script_Data.get("secret_key")}'
        mtext = encry_md5(dataStr)
        if mtext != sign:
            log_dict['response_code']=409
            log_dict['response_text']='解签验证失败!'
            ApiRequestLogTable.insert_one(log_dict)
            return xtjson.json_params_error('解签验证失败！')

        if not script_Data.get('statu'):
            return xtjson.json_params_error('设备异常！')

        if reqType == 'getTask':
            return self.getPayTask_func(script_Data, log_dict)
        if reqType == 'subTask':
            return self.subTask_func(data_json, script_Data, log_dict)
        if reqType == 'updateBalance':
            return self.updateBalance_func(data_json, script_Data, log_dict)

        log_dict['response_code']=400
        log_dict['response_text']='访问错误!'
        ApiRequestLogTable.insert_one(log_dict)
        return xtjson.json_params_error()



class BankBillLogApi(views.MethodView):
    '''
    代付订单接口
    '''
    add_url_rules = [['/BankBillLog/Query/', 'BankBillLogApi']]

    def post(self):
        request_data = {}
        try:
            if request.form:
                request_data = request.form.to_dict()
            if request.data:
                for k, v in json.loads(request.data.decode()).items():
                    if isinstance(v, str):
                        request_data[k] = str(v).strip()
                    else:
                        request_data[k] = v or ''
        except Exception as e:
            return xtjson.json_params_error('数据解析失败！', code=401)

        mchId = request_data.get('mchId') or ''
        describe = request_data.get('describe') or ''
        dayc = request_data.get('dayc') or 0
        sign = request_data.get('sign') or ''
        if not mchId or not mchId.strip() or not sign or not sign.strip() or not describe or not describe.strip():
            return xtjson.json_params_error('缺少参数！', code=402)

        merchant_data = MerchantTable.find_one({'merchant_id': mchId})
        if not merchant_data:
            return xtjson.json_params_error('参数错误！', code=403)

        reqks = list(request_data.keys())
        reqks.sort()
        dataStr = ''
        for k in reqks:
            if k == 'sign':
                continue
            _v = request_data.get(k) or ''
            dataStr += f'&{k}={_v}'
        dataStr += '&sign=' + merchant_data.get('secret_key')
        mtext = encry_md5(dataStr.strip('&'))
        print('mtext:', mtext)
        print('sign:', sign)
        # if mtext != sign:
        #     return xtjson.json_params_error('解签验证失败！', code=409)
        try:
            dayc = int(str(dayc).strip())
        except:
            pass
        crrtime = datetime.datetime.now()
        end_time = datetime.datetime(crrtime.year, crrtime.month, crrtime.day, 23, 59, 59)
        if not dayc:
            start_time = datetime.datetime(crrtime.year, crrtime.month, crrtime.day, 0, 0, 0)
        else:
            start_time = end_time - datetime.timedelta(days=dayc)

        description1 = describe.lower()
        mtt = description1[:2]
        for t in description1[2:]:
            mtt += '\s*' + t

        description1 = description1.upper()
        mtt2 = description1[:2]
        for t in description1[2:]:
            mtt2 += '\s*' + t
        cbill_datas = BankCardBillTable.find_many({'$or': [{'description': {'$regex': mtt}}, {'description': {'$regex': mtt2}}], 'bill_time': {'$gt': start_time, '$lt': end_time}}) or []
        datas = []
        for cbll in cbill_datas:
            bankacrd_uuid = cbll.get('bankacrd_uuid') or ''
            bankacrd_data = BankCardTable.find_one({'uuid': bankacrd_uuid}) or {}
            if not bankacrd_data:
                continue
            bank_data = BankTable.find_one({'uuid': bankacrd_data.get('bank_uid')}) or {}
            if not bank_data:
                continue
            ordertime = ''
            if cbll.get('bill_time'):
                try:
                    ordertime = cbll.get('bill_time').strftime('%Y-%m-%d %H:%M:%S')
                except:
                    pass
            _data = {
                'account_username': bankacrd_data.get('account_username'),
                'account': bankacrd_data.get('account'),
                'bankname': bank_data.get('shortName'),
                'amount': cbll.get('amount'),
                'ordertime': ordertime,
            }
            datas.append(_data)

        return xtjson.json_result(data=datas)

class BankCardListApi(views.MethodView):
    '''
    代付订单接口
    '''
    add_url_rules = [['/listSysCard', 'ListSysCard']]
    def get(self):
        cards = BankCardTable.find_many({"statu":True, "bankcard_type":"system_card"})
        datas = []
                
        for card in cards:
            _dd = {}
            _bacnk_data = BankTable.find_one({'uuid': card.get("bank_uid")}) or {}
            # _dd["name"] = card.get("name")
            # _dd["account"] = card.get("account")
            # _dd["note"] = card.get("name")
            # _dd["method_type"] = card.get("method_type")
            # _dd["account_username"] = card.get("account_username")
            # _dd["balance_amount"] = card.get("balance_amount")
            _dd["bank_code"] = _bacnk_data.get("code")
            _dd["bank_short_name"] = _bacnk_data.get("short_name")
            datas.append(_dd)

        log_dict = {
            "request_method": REQUEST_METHOD.GET,
            "request_data": json.dumps(request.form.to_dict()),
            "url_path": str(request.path),
            'ip': str(get_ip()),
            'response_code':200,
            'response_text':datas
        }

        ApiRequestLogTable.insert_one(log_dict)

        return xtjson.json_result(msg="List System Bank Card", data=datas)

    
