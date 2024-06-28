# -*- coding: UTF-8 -*-
import datetime, requests, json, random, string, pymongo, os, shortuuid
from flask import request
from models.pay_table import BankCardTable, CollectionOrderTable, TunnelTable, MerchantTunnleTable, BankTable, MerchantTable, callbackLogTable, MerchantBillStatementTable, VpnTable, AgentadminBillLogTable
from constants import TUNNLE_METHOD, PAY_METHOD, CallbackState, CallbankType, BILL_STATEMEN_TYPES, ROlE_ALL, BankCardType
from common_utils.utils_funcs import encry_md5, img_base4_save, img_to_base64
from models.cms_table import SystemLogTable
from .tool_func import current_admin_data_dict
from common_utils.utils_funcs import get_ip
from models.cms_user import CmsUserTable
from common_utils.lqredis import SiteRedis
from models.behalfPay import behalfPayCallbackLogTable, behalfPayOrderProcessTable, behalfPayOrderTable
from models.pay_table import WithdrawalOrderLogTable
from modules.pay_qrcode.qrcode2.payQrcode import generate_qrcode


def getAvailableBankcard(totalAmount, agentadmin_data, bank_ids=[], bank_code='', is_merchant_uid='', payMethod=''):
    '''
    获取可用银行卡
    '''
    bankcard_datas = []
    fff = {'statu': True}
    if payMethod:
        if payMethod == PAY_METHOD.VNVT2PAY:
            fff['method_type'] = PAY_METHOD.VNVTPAY
        elif payMethod == PAY_METHOD.VNZA2LO:
            fff['method_type'] = PAY_METHOD.VNZALO
        elif payMethod == PAY_METHOD.VNMO2MO:
            fff['method_type'] = PAY_METHOD.VNMOMO
        elif payMethod == PAY_METHOD.VNBANKQR2:
            fff['method_type'] = PAY_METHOD.VNBANKQR
        else:
            fff['method_type'] = payMethod

    if bank_ids:
        fff.update({'bank_uid': {'$in': bank_ids}})

    if agentadmin_data.get('is_syscard'):
        fff['$or'] = [{'bankcard_type': BankCardType.SYSTEM_CARD}, {'agentadmin_uuid': agentadmin_data.get('uuid')}]
    else:
        fff['agentadmin_uuid'] = agentadmin_data.get('uuid')

    datas = BankCardTable.find_many(fff)
    if not datas:
        return False, '无可用收款方式！'

    crr_time = datetime.datetime.now()
    day_date_start = datetime.datetime(crr_time.year, crr_time.month, crr_time.day, 0, 0, 0)
    day_date_end = datetime.datetime(crr_time.year, crr_time.month, crr_time.day, 23, 59, 59)

    for da in datas:
        collection_money_min = da.get('collection_money_min') or 0
        collection_money_max = da.get('collection_money_max') or 0
        if collection_money_min and collection_money_min > totalAmount:
            continue
        if collection_money_max and collection_money_max < totalAmount:
            continue

        # 检测今日收款笔数
        orderCount = CollectionOrderTable.count({'bankcard_id': da.get('uuid'), 'order_time': {'$gte': day_date_start, '$lte': day_date_end}})
        day_collection_pencount_limit = da.get('day_collection_pencount_limit') or 0
        if day_collection_pencount_limit and day_collection_pencount_limit <= orderCount:
            continue

        if is_merchant_uid:
            if da.get('merchant_uid') and da.get('merchant_uid') != is_merchant_uid:
                continue

        # 检测银行类型
        if bank_code:
            bank_data = BankTable.find_one({'uuid': da.get('bank_uid')})
            if not bank_data:
                continue
            if bank_data.get('code') != bank_code.upper():
                continue

        bankcard_datas.append(da)

    if not bankcard_datas:
        return False, '无可用收款方式！'

    return True, bankcard_datas



def pay_api_control_func(merchant_data, totalAmount, payMethod, bank_code=''):
    '''
    风控函数
    '''

    tunnel_data = TunnelTable.find_one({'code': payMethod})
    if not tunnel_data:
        return False, '当前支付通道不可用!'
    if not tunnel_data.get('tunnel_statu'):
        return False, '当前支付通道状态不可用!'

    agentadmin_uuid = merchant_data.get('agentadmin_uuid')
    if not agentadmin_uuid:
        return False, '数据错误！'

    agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid})
    if not agentadmin_data:
        return False, '数据错误！'

    balance_amount = agentadmin_data.get('balance_amount') or 0
    if balance_amount <= 0:
        return False, '406，通道暂不可用！'

    ddsls = BankTable.collection().aggregate([
        {"$match": {'statu': True}},
        {"$group": {"_id": '$uuid'}},
        {'$project': {"uuid": 1}}
    ])
    bank_ids = []
    for d in ddsls:
        bank_ids.append(d.get('_id'))

    if not bank_ids:
        return False, '银行不可用！'

    merchantTunnle_data = MerchantTunnleTable.find_one({'merchant_uuid': merchant_data.get('uuid'), 'tunnle_method': TUNNLE_METHOD.collection, 'tunnle_id': tunnel_data.get('uuid')})
    if not merchantTunnle_data:
        return False, '当前商户支付通道不可用!'
    if not merchantTunnle_data.get('statu'):
        return False, '当前商户支付通道状态不可用!'

    single_amount_min = merchantTunnle_data.get('single_amount_min') or 0
    single_amount_max = merchantTunnle_data.get('single_amount_max') or 0
    if single_amount_min and single_amount_min > totalAmount:
        return False, '无可用支付通道！'
    if single_amount_max and single_amount_max < totalAmount:
        return False, '无可用支付通道！'

    agentadmin_uuid = merchant_data.get('agentadmin_uuid')
    agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid, 'role_code': ROlE_ALL.AGENTADMIN})
    if not agentadmin_data:
        return False, '数据异常！'

    state, res = getAvailableBankcard(totalAmount, agentadmin_data, bank_ids, bank_code=bank_code, is_merchant_uid=merchant_data.get('uuid'), payMethod=payMethod)
    if not state:
        return False, res

    result= {
        'bankcard_datas': res,
        'merchantTunnle_data': merchantTunnle_data,
    }
    return True, result


def getPayQrcode_func2(accountNo, bank_code, shortName, bank_name, bank_bin, amount, addInfo):
    try:
        base64_string = generate_qrcode(bank_bin, accountNo, bank_name, amount, addInfo)
        return base64_string
    except:
        pass

    url = 'http://103.56.163.161/api/pay/getQrcode'
    url2 = 'http://103.56.160.92/api/pay/getQrcode'
    url3 = 'http://103.57.223.111/api/pay/getQrcode'
    url4 = 'http://103.56.163.65/api/pay/getQrcode'
    _url = random.choice([url, url2, url3, url4])
    headers = {'Content-Type': 'application/json'}
    data = {
        'action': 'getQrcode',
        "accountNo": accountNo,
        "bank_code": bank_code,
        "shortName": shortName,
        "bank_name": bank_name,
        "bank_bin": bank_bin,
        "amount": amount,
        "addInfo": addInfo,
    }
    try:
        res = requests.post(url=url, data=data, timeout=15)
        data_json = res.json()

    except:
        return False, '支付页面创建失败！'
    if data_json.get('code') != 200:
        return False, '支付页面创建失败！'
    try:
        payQrcode = data_json.get('data').get('payQrcode')
        return True, payQrcode
    except:
        return False, '支付页面创建失败！'


# 获取支付二维码
def getPayQrcode_func(accountNo, bank_code, shortName, bank_name, bank_bin, amount, addInfo):
    '''
    获取支付二维码
    '''
    url = 'c'
    header = {
        'x-client-id': '2b500bc7-ec20-44c1-807e-6f2a6213d9c4',
        'x-api-key': '04a0e117-c330-4baa-8814-639e49689b98',
    }
    if bank_code in ['VBA']:
        _name = shortName
    elif bank_code in ['TIMO']:
        _name = bank_name
        if '(' in bank_name:
            _name = str(bank_name).split('(', 1)[0].strip()
    elif bank_code == 'KBank':
        _name = 'Ngân hàng Đại chúng'
    elif bank_code == 'VRB':
        _name = 'Ngân hàng Liên doanh Việt'
    else:
        _name = bank_name or ''
        if '-' in _name:
            _name = _name.split('-')[-1].strip()
    data = {
        "accountNo": accountNo, # 银行账户
        "accountName": _name, # 银行名称
        "acqId": bank_bin, # 银行Id
        # "acqId": bank_data.get('bin'), # 银行Id
        "amount": int(amount), # 支付金额
        "addInfo": addInfo, # 附言
        "format": "text",
        "template": "qr_only"
    }
    try:
        res = requests.post(url, data=data, headers=header, timeout=25)
    except:
        return False, '支付页面创建失败！'
    if res.status_code != 200:
        return False, '支付页面创建失败！'
    d = res.json()
    if d.get('code') != '00':
        return False, d.get('desc')
    
    print(d, "-----------------------------------------")

    return True, d.get('data').get('qrDataURL')



def getBankPayQrcode(data_uuid, amount, bank_memo, bank_data, payqrcode_url='', project_static_folder='', receive_account='', is_behalfPay=False, is_base=True):
    if not payqrcode_url or not os.path.exists(project_static_folder + payqrcode_url):
        satte, payQrcode = getPayQrcode_func2(
            accountNo=receive_account,
            bank_code=bank_data.get('code'),
            shortName=bank_data.get('shortName'),
            bank_name=bank_data.get('name'),
            bank_bin=bank_data.get('bin'),
            amount=amount,
            addInfo=bank_memo
        )
        if not satte:
            satte, payQrcode = getPayQrcode_func(
                accountNo=receive_account,
                bank_code=bank_data.get('code'),
                shortName=bank_data.get('shortName'),
                bank_name=bank_data.get('name'),
                bank_bin=bank_data.get('bin'),
                amount=amount,
                addInfo=bank_memo
            )
            if not satte:
                return False, '支付码获取失败！'

        relatively_path = f'/assets/payimg/'
        import_folder = project_static_folder + relatively_path
        if not os.path.exists(import_folder):
            os.makedirs(import_folder)
        new_filename = datetime.datetime.now().strftime('%Y%m%d') + '_' + str(shortuuid.uuid())
        img_base4_save(payQrcode, import_folder + new_filename + '.jpg')
        payqrcode_url = relatively_path + new_filename + '.jpg'
        if is_behalfPay:
            behalfPayOrderTable.update_one({'uuid': data_uuid}, {'$set': {'payqrcode_url': payqrcode_url}})
        else:
            CollectionOrderTable.update_one({'uuid': data_uuid}, {'$set': {'payqrcode_url': payqrcode_url}})
    else:
        payQrcode = img_to_base64(project_static_folder + payqrcode_url)
    if not is_base:
        return True, payqrcode_url
    return True, payQrcode

def getWithdrawalBankPayQrcode(data_uuid, amount, bank_memo, bank_data, payqrcode_url='', project_static_folder='', receive_account='', is_base=True):
    # if not payqrcode_url or not os.path.exists(project_static_folder + payqrcode_url):
    #     satte, payQrcode = getPayQrcode_func2(
    #         accountNo=receive_account,
    #         bank_code=bank_data.get('code'),
    #         shortName=bank_data.get('shortName'),
    #         bank_name=bank_data.get('name'),
    #         bank_bin=bank_data.get('bin'),
    #         amount=amount,
    #         addInfo=bank_memo
    #     )
    #     if not satte:
    #         satte, payQrcode = getPayQrcode_func(
    #             accountNo=receive_account,
    #             bank_code=bank_data.get('code'),
    #             shortName=bank_data.get('shortName'),
    #             bank_name=bank_data.get('name'),
    #             bank_bin=bank_data.get('bin'),
    #             amount=amount,
    #             addInfo=bank_memo
    #         )
    #         if not satte:
    #             return False, '支付码获取失败！'

    #     relatively_path = f'/assets/payimg/'
    #     import_folder = project_static_folder + relatively_path
    #     if not os.path.exists(import_folder):
    #         os.makedirs(import_folder)
    #     new_filename = datetime.datetime.now().strftime('%Y%m%d') + '_' + str(shortuuid.uuid())
    #     img_base4_save(payQrcode, import_folder + new_filename + '.jpg')
    #     payqrcode_url = relatively_path + new_filename + '.jpg'
    #     WithdrawalOrderLogTable.update_one({'uuid': data_uuid}, {'$set': {'payqrcode_url': payqrcode_url}})
    # else:
    #     payQrcode = img_to_base64(project_static_folder + payqrcode_url)
    # if not is_base:
    #     return True, payqrcode_url
    # if bank_data.get("code") == 'SHB':
    #     bank_memo = bank_memo[:25]
    payQrcode = f'https://img.vietqr.io/image/{bank_data.get("shortName")}-{receive_account}-q9WMF1G.jpg?amount={amount}&addInfo={bank_memo}&accountName={bank_data.get("name")}'
    return True, payQrcode



# 代收订单回调
def CallbackPayOrderFunc(order_uuid, order_dict={}, is_manual=False, admin_uuid='', note=''):
    '''
    代收订单回调
    '''
    if not order_dict:
        order_dict = CollectionOrderTable.find_one({'uuid': order_uuid})
        if not order_dict:
            return False, '订单数据不存在！'

    callback_url = order_dict.get('callback_url')
    req_data = {
        'mchId': order_dict.get('merchant_id') or '',
        'mchOrderId': order_dict.get('merchant_order_id') or '',
        'amount': order_dict.get('order_amount') or 0,
        'payAmount': int(order_dict.get('actual_amount') or 0),
        'isPaid': 1 if order_dict.get('pay_statu') else 0,
        'payMethod': 7,
    }
    payMethod = order_dict.get('pay_method')
    if payMethod == PAY_METHOD.VNBANKQR:
        req_data['payMethod'] = 7
    elif payMethod == PAY_METHOD.VNZALO:
        req_data['payMethod'] = 8
    elif payMethod == PAY_METHOD.VNMOMO:
        req_data['payMethod'] = 9
    elif payMethod == PAY_METHOD.VNVTPAY:
        req_data['payMethod'] = 10

    merchant_data = MerchantTable.find_one({'merchant_id': order_dict.get('merchant_id')})
    if not merchant_data:
        return False, '数据错误!'

    kls = list(req_data)
    kls.sort()
    dataStr = ''
    for k in kls:
        _v = req_data.get(k)
        dataStr += f'&{k}={_v}'

    dataStr += '&sign=' + merchant_data.get('secret_key')
    dataStr = dataStr.strip('&')
    sign = encry_md5(dataStr)
    req_data['sign'] = sign

    callbackLog = {
        'order_uuid': order_uuid,
        'order_id': order_dict.get('order_id'),
        'merchant_uuid': merchant_data.get('uuid'),
        'request_text': req_data,
        'affidavit_text': dataStr,
        'callback_url': callback_url,
    }
    if is_manual:
        callbank_type = CallbankType.MANUAL
    else:
        callbank_type = CallbankType.AUTOMATIC
    callbackLog['callbank_type'] = callbank_type
    if admin_uuid:
        callbackLog['admin_uuid'] = admin_uuid

    crrtime = datetime.datetime.now()
    try:
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url=callback_url, data=json.dumps(req_data), headers=headers, timeout=20)
        callbackLog['response_code'] = res.status_code or 501
        if res.status_code == 200 and res.text in ['success', 'SUCCESS']:
            callbackLog['statu'] = True
            callbackLog['response_text'] = str(res.text)[:300]
        else:
            callbackLog['statu'] = False
            callbackLog['response_text'] = str(res.text)[:300]
        callbackLog['note'] = note
    except Exception as e:
        callbackLog['response_code'] = 500
        callbackLog['statu'] = False
        callbackLog['note'] = str(e)
        callbackLog['response_text'] = ''
    callbackLog['create_time'] = crrtime
    callbackLog['agentadmin_uuid'] = merchant_data.get('agentadmin_uuid')
    callbackLogTable.insert_one(callbackLog)

    if callbackLog.get('statu'):
        if order_dict.get('callback_statu') != CallbackState.SUCCESS:
            update_dict = {
                'callback_statu': CallbackState.SUCCESS,
                'callback_time': crrtime,
                'callbank_type': callbank_type,
            }
            order_time = order_dict.get('order_time')
            if order_time:
                success_seconds = int((crrtime - order_time).seconds)
                update_dict['success_seconds'] = success_seconds
            if order_dict.get('is_lose'):
                update_dict['lose_note'] = '已处理'
            CollectionOrderTable.update_one({'uuid': order_uuid}, {'$set': update_dict})

        return True, ''
    if order_dict.get('callback_statu') == CallbackState.NOT_CALLEDBACK:
        update_dict = {
            'callback_statu': CallbackState.FAILED,
            'callbank_type': callbank_type,
            'callbank_try': 3,
        }
        CollectionOrderTable.update_one({'uuid': order_uuid}, {'$set': update_dict})
    return False, '回调失败！'


# 代付订单回调
def behalfPayCallbackOrderFunc(order_uuid, order_dict={}, is_manual=False, admin_uuid='', msg='', note=''):
    if not order_dict:
        order_dict = behalfPayOrderTable.find_one({'uuid': order_uuid})
        if not order_dict:
            return False, '订单数据不存在！'

    if order_dict.get('reject_pay'):
        isPaid = 2
    elif order_dict.get('pay_statu'):
        isPaid = 1
    else:
        isPaid = 0

    callback_url = order_dict.get('callback_url')
    req_data = {
        'mchId': order_dict.get('merchant_id') or '',
        'mchOrderId': order_dict.get('merchant_order_id') or '',
        'amount': order_dict.get('order_amount') or 0,
        'costFee': float(order_dict.get('repay_amount') or 0),
        'isPaid': isPaid,
        'msg': msg or '',
    }
    merchant_data = MerchantTable.find_one({'merchant_id': order_dict.get('merchant_id')})
    if not merchant_data:
        return False, '数据错误!'

    kls = list(req_data)
    kls.sort()
    dataStr = ''
    for k in kls:
        _v = req_data.get(k)
        dataStr += f'&{k}={_v}'

    dataStr += '&sign=' + merchant_data.get('secret_key')
    dataStr = dataStr.strip('&')
    sign = encry_md5(dataStr)
    req_data['sign'] = sign
    callbackLog = {
        'order_uuid': order_uuid,
        'order_id': order_dict.get('order_id'),
        'merchant_uuid': merchant_data.get('uuid'),
        'request_text': req_data,
        'affidavit_text': dataStr,
        'callback_url': callback_url,
    }
    if is_manual:
        callbank_type = CallbankType.MANUAL
    else:
        callbank_type = CallbankType.AUTOMATIC
    callbackLog['callbank_type'] = callbank_type
    if admin_uuid:
        callbackLog['admin_uuid'] = admin_uuid

    crrtime = datetime.datetime.now()
    try:
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url=callback_url, data=json.dumps(req_data), headers=headers, timeout=300)
        callbackLog['response_code'] = res.status_code or 501
        if res.status_code == 200 and res.text in ['success', 'SUCCESS']:
            callbackLog['statu'] = True
            callbackLog['note'] = ''
            callbackLog['response_text'] = str(res.text)[:300]
        else:
            callbackLog['statu'] = False
            callbackLog['response_text'] = str(res.text)[:300]
            callbackLog['note'] = ''
        callbackLog['note'] = note
    except Exception as e:
        callbackLog['response_code'] = 500
        callbackLog['statu'] = False
        callbackLog['note'] = str(e)
        callbackLog['response_text'] = ''
    callbackLog['create_time'] = crrtime
    callbackLog['agentadmin_uuid'] = merchant_data.get('agentadmin_uuid')
    behalfPayCallbackLogTable.insert_one(callbackLog)

    if callbackLog.get('statu'):
        if order_dict.get('callback_statu') != CallbackState.SUCCESS:
            update_dict = {
                'callback_statu': CallbackState.SUCCESS,
                'callback_time': crrtime,
                'callbank_type': callbank_type,
            }
            order_time = order_dict.get('order_time')
            if order_time:
                success_seconds = int((crrtime - order_time).seconds)
                update_dict['success_seconds'] = success_seconds
            behalfPayOrderTable.update_one({'uuid': order_uuid}, {'$set': update_dict})

        return True, ''

    if order_dict.get('callback_statu') == CallbackState.NOT_CALLEDBACK:
        update_dict = {
            'callback_statu': CallbackState.FAILED,
            'callbank_type': callbank_type,
            'callbank_try': 3,
        }
        behalfPayOrderTable.update_one({'uuid': order_uuid}, {'$set': update_dict})
    else:
        callbank_try = order_dict.get('callbank_try')
        if not callbank_try:
            callbank_try = 3
        else:
            callbank_try += 1
        update_dict = {'callbank_try': callbank_try,}
        behalfPayOrderTable.update_one({'uuid': order_uuid}, {'$set': update_dict})
    return False, '回调失败！'


# 添加系统操作日志
def add_SystemLog(note='', code=200, method='GET'):
    user_data = current_admin_data_dict()
    if not user_data:
        return
    ips = get_ip()
    if isinstance(ips, list):
        ips = ','.join(ips)
    _data = {
        'user_uuid': user_data.get('uuid'),
        'state_code': code,
        'ip': ips,
        'url_path': str(request.path),
        'note': note,
        'method': method,
    }
    if user_data.get('role_code') == ROlE_ALL.AGENTADMIN:
        _data['agentadmin_uuid'] = user_data.get('uuid')
    elif user_data.get('role_code') == ROlE_ALL.SYSTEMUSER:
        _data['agentadmin_uuid'] = user_data.get('agentadmin_uuid')

    SystemLogTable.insert_one(_data)


# 商户金额变动
def MerchantUpdateAmout_func(amount, merchant_uuid, is_add=True):
    merchant_data = MerchantTable.find_one({'uuid': merchant_uuid}) or {}
    if not merchant_data:
        return False, '商户不存在！'

    if not is_add:
        amount = -1 * amount

    new_merchant_data = MerchantTable.collection().find_one_and_update(
        {'uuid': merchant_uuid},
        {'$inc': {'balance_amount': amount}},
        upsert=False,
        return_document=pymongo.ReturnDocument.AFTER  # 返回更新后的文档
    ) or {}
    balance_amount = new_merchant_data.get('balance_amount')
    return True, balance_amount or 0


# 代理资金变动
def agentadminUpateAmout_func(amount, agentadmin_uuid, is_add=False):
    agentadmin_data = CmsUserTable.find_one({'uuid': agentadmin_uuid, 'role_code': ROlE_ALL.AGENTADMIN}) or {}
    if not agentadmin_data:
        return False, '代理用户不存在！'

    # in_vnbankqr_rate = agentadmin_data.get('in_vnbankqr_rate') or 0
    # if not in_vnbankqr_rate:
    #     return False, '未配置代付利率！'

    if not is_add:
        amount = -1 * amount

    CmsUserTable.collection().find_one_and_update(
        {'uuid': agentadmin_uuid},
        {'$inc': {'balance_amount': amount}},
        upsert=False,
        return_document=pymongo.ReturnDocument.AFTER  # 返回更新后的文档
    )
    return True, ''


# 代付金额扣除
def payBehalf_deduct(order_uuid='', order_data={}, merchant_data={}):
    if not order_data:
        order_data = behalfPayOrderTable.find_one({'uuid': order_uuid}) or {}
    if not order_data:
        return
    order_amount = order_data.get('order_amount')
    repay_amount = order_data.get('repay_amount')
    _amount = order_amount + repay_amount

    if MerchantBillStatementTable.find_one({'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF, 'order_id': order_data.get('order_id')}):
        return True
    
    mstate, balance_amount = MerchantUpdateAmout_func(_amount, merchant_data.get('uuid'), is_add=False)
    if not mstate:
        return
    _biil = {
        'merchant_uuid': merchant_data.get('uuid'),
        'amount': int(order_amount),
        'balance_amount': balance_amount,
        'repay_amount': repay_amount,
        'note': '',
        'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF,
        'agentadmin_uuid': order_data.get('agentadmin_uuid'),
        'order_id': order_data.get('order_id'),
        'merchant_order_id': order_data.get('merchant_order_id'),
    }
    MerchantBillStatementTable.insert_one(_biil)

    if AgentadminBillLogTable.find_one({'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF, 'order_id': order_data.get('order_id')}):
        return True

    agentadmin_data = CmsUserTable.find_one({'uuid': merchant_data.get('agentadmin_uuid'), 'role_code': ROlE_ALL.AGENTADMIN}) or {}
    paybehalf_rate = agentadmin_data.get('paybehalf_rate') or 0
    if agentadmin_data:
        _b_repay_amount = round(order_amount * paybehalf_rate, 2) + order_amount
        _state, balance_amount_1 = agentadminUpateAmout_func(_b_repay_amount, merchant_data.get('agentadmin_uuid'))
        if not _state:
            return
        _alog = {
            'agentadmin_uuid': agentadmin_data.get('uuid'),
            'amount': _b_repay_amount,
            'balance_amount': balance_amount_1,
            'repay_amount': 0,
            'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF,
            'note': '',
            'order_id': order_data.get('order_id'),
            'merchant_order_id': order_data.get('merchant_order_id'),
            'merchant_id': merchant_data.get('merchant_id'),
        }
        AgentadminBillLogTable.insert_one(_alog)
    return True


# 代付金额退回
def payBehalf_goback(order_uuid='', order_data={}, merchant_data={}):
    if not order_data:
        order_data = behalfPayOrderTable.find_one({'uuid': order_uuid}) or {}
    if not order_data:
        return
    order_amount = order_data.get('order_amount')
    repay_amount = order_data.get('repay_amount')
    _amount = order_amount + repay_amount

    if MerchantBillStatementTable.find_one({'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF_GOBACK, 'order_id': order_data.get('order_id')}):
        return True
    mstate, balance_amount = MerchantUpdateAmout_func(_amount, merchant_data.get('uuid'))
    if not mstate:
        return

    _biil = {
        'merchant_uuid': merchant_data.get('uuid'),
        'amount': int(order_amount),
        'balance_amount': balance_amount,
        'repay_amount': repay_amount,
        'note': '',
        'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF_GOBACK,
        'agentadmin_uuid': order_data.get('agentadmin_uuid'),
        'order_id': order_data.get('order_id'),
        'merchant_order_id': order_data.get('merchant_order_id'),
    }
    MerchantBillStatementTable.insert_one(_biil)

    if AgentadminBillLogTable.find_one({'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF_GOBACK, 'order_id': order_data.get('order_id')}):
        return True

    agentadmin_data = CmsUserTable.find_one({'uuid': merchant_data.get('agentadmin_uuid'), 'role_code': ROlE_ALL.AGENTADMIN}) or {}
    agentadminBillLog_data = AgentadminBillLogTable.find_one({'order_id': order_data.get('order_id'), 'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF, 'agentadmin_uuid': agentadmin_data.get('uuid')}) or {}
    if agentadminBillLog_data and agentadmin_data:
        _b_repay_amount = agentadminBillLog_data.get('amount') or 0
        _state, balance_amount_1 = agentadminUpateAmout_func(_b_repay_amount, merchant_data.get('agentadmin_uuid'), is_add=True)
        if not _state:
            return
        _alog = {
            'agentadmin_uuid': agentadmin_data.get('uuid'),
            'amount': _b_repay_amount,
            'balance_amount': balance_amount,
            'repay_amount': 0,
            'bill_type': BILL_STATEMEN_TYPES.PAY_BEHALF_GOBACK,
            'note': '',
            'order_id': order_data.get('order_id'),
            'merchant_order_id': order_data.get('merchant_order_id'),
            'merchant_id': merchant_data.get('merchant_id'),
        }
        AgentadminBillLogTable.insert_one(_alog)

    return True


# 代收金额添加
def payIncome_addto(order_uuid='', order_data={}, merchant_data={}):
    if not order_data:
        order_data = CollectionOrderTable.find_one({'uuid': order_uuid}) or {}
    if not order_data:
        return
    actual_amount = order_data.get('actual_amount') or 0
    if not actual_amount:
        return

    order_id = order_data.get('order_id') or ''
    merchant_order_id = order_data.get('merchant_order_id') or ''
    if MerchantBillStatementTable.find_one({'bill_type': BILL_STATEMEN_TYPES.INCOME_ORDER, 'order_id': order_id}):
        return

    repay_amount = order_data.get('repay_amount') or 0
    _amount = actual_amount - repay_amount
    _state, balance_amount = MerchantUpdateAmout_func(_amount, merchant_data.get('uuid'))
    if not _state:
        return

    _biil = {
        'merchant_uuid': merchant_data.get('uuid'),
        'amount': int(actual_amount),
        'balance_amount': balance_amount,
        'repay_amount': repay_amount,
        'note': '',
        'bill_type': BILL_STATEMEN_TYPES.INCOME_ORDER,
        'order_id': order_id,
        'merchant_order_id': merchant_order_id,
        'create_time': order_data.get('callback_time') or datetime.datetime.now(),
    }
    MerchantBillStatementTable.insert_one(_biil)

    if AgentadminBillLogTable.find_one({'bill_type': BILL_STATEMEN_TYPES.INCOME_ORDER, 'order_id': order_id}):
        return True

    agentadmin_data = CmsUserTable.find_one({'uuid': merchant_data.get('agentadmin_uuid'), 'role_code': ROlE_ALL.AGENTADMIN}) or {}
    in_vnbankqr_rate = agentadmin_data.get('in_vnbankqr_rate') or 0
    if agentadmin_data and in_vnbankqr_rate:
        _b_repay_amount = round(actual_amount * in_vnbankqr_rate, 2)
        _state, balance_amount_1 = agentadminUpateAmout_func(_b_repay_amount, merchant_data.get('agentadmin_uuid'))
        if not _state:
            return
        _alog = {
            'agentadmin_uuid': agentadmin_data.get('uuid'),
            'amount': _b_repay_amount,
            'balance_amount': balance_amount,
            'repay_amount': 0,
            'bill_type': BILL_STATEMEN_TYPES.INCOME_ORDER,
            'note': PAY_METHOD.name_dict.get(order_data.get('pay_method') or ''),
            'order_id': order_id,
            'merchant_order_id': merchant_order_id,
            'merchant_id': merchant_data.get('merchant_id'),
            'create_time': order_data.get('callback_time') or datetime.datetime.now(),
        }
        AgentadminBillLogTable.insert_one(_alog)
    return True


# 代收订单处理
def createPayBehalfOrder():
    pass


# 生成代付订单号
def getBehalfPayOrderId(mdl):
    while True:
        fff = list('ABCDEFGHJKLMNPQRSTUVWXYZABCDEFGHJKLMNPQRSTUVWXYZ')
        text = 'Y'
        crr_Date = datetime.datetime.now()
        crr_day = crr_Date.day
        text += fff[crr_day]
        text += str(mdl)
        for i in range(7):
            ssd = list(string.digits)
            random.shuffle(ssd)
            text += random.choice(ssd)
        if behalfPayOrderTable.find_one({'order_id': text}):
            continue
        return text


# 获取VPN url
def get_vpnurl(bank_data, bankcard_uuid='', vpn_uuid=''):
    vkkk = 'sf_bankcard_vpn_' + bankcard_uuid
    if bank_data.get('is_ip_pool'):
        vpn_url = SiteRedis.get(vkkk) or b''
        if vpn_url:
            vpn_url = vpn_url.decode()
        if not vpn_url:
            ips = bank_data.get('ips') or ''
            for i in range(20):
                vvp = random.choice(ips.split('\n'))
                SiteRedis.dele('vpn_'+vvp)
                if not vvp or not vvp.strip():
                    continue
                if SiteRedis.get('vpn_'+vvp):
                    continue
                vpn_url = vvp
                SiteRedis.set(vkkk, vvp, expire=60 * 30)
                break
    else:
        vpn_url = ''
        if vpn_uuid:
            vpn_data = VpnTable.find_one({'uuid': vpn_uuid, 'statu': True}) or {}
            vpn_url = vpn_data.get('vpn_url')
    if isinstance(vpn_url, bytes):
        vpn_url = vpn_url.decode()
    return vpn_url

