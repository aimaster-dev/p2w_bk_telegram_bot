# -*- coding: UTF-8 -*-
import datetime, time, re, threading, os
from models.pay_table import BankCardTable, CollectionOrderTable,  BankTable, MerchantTable, BankScriptLogTable, VpnTable, messageWarnTable, BankCardBillTable, unknownIncomeTable
from constants import unusualTypes, BankBillTypes
# from modules.bank_module.ACB import BANK_ACB
# from modules.bank_module.TPB import BANK_TPB
# from modules.bank_module.SEAB import BANK_SEAB
from modules.bank_module.ICB import BANK_ICB
# from modules.bank_module.MB import BANK_MB
# from modules.bank_module.NAB import BANK_NAB
# from modules.bank_module.MSB import BNAK_MSB
from modules.bank_module.VAB import BANK_VAB
# from modules.bank_module.BAB import BANK_BAB
# from modules.bank_module.VPB import BANK_VPB
# from modules.bank_module.VIETBANK import BANK_VIETBANK
from modules.bank_module.VCB import BANK_VCB
from common_utils.utils_funcs import getDayDateSilce
from common_utils.lqredis import SiteRedis
from .view_func import CallbackPayOrderFunc, payIncome_addto, get_vpnurl

ACB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'ACB.so')
TPB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'TPB.so')
SEAB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'SEAB.so')
MB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'MB.so')
NAB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'NAB.so')
MSB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'MSB.so')
BAB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'BAB.so')
VIETBANK = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'VIETBANK.so')
VPB = os.path.join(os.path.dirname(__file__), 'modules\\bank_module', 'VPB.so')


# 获取任务订单
def getTaskOrder(bankCode, bankacrd_uuid='', is_manual=False):
    if is_manual:
        bank_data = BankTable.find_one({'code': bankCode})
    else:
        bank_data = BankTable.find_one({'code': bankCode, 'statu': True})
    if not bank_data:
        return
    fff1 = {}
    if not is_manual:
        fff1['script_statu'] = True
    if bankacrd_uuid:
        fff1['uuid'] = bankacrd_uuid
    else:
        fff1['bank_uid'] = bank_data.get('uuid')
    bankcard_datas = BankCardTable.find_many(fff1) or []
    if not bankcard_datas:
        return

    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(minutes=20)
    order_datas = CollectionOrderTable.find_many({'pay_statu': False, 'bank_code': bankCode, 'order_time': {'$gte': start_time, '$lte': end_time}}) or []

    order_dict = {}
    for ord in order_datas:
        order_dict[ord.get('order_id')] = ord

    result = {
        'bank_data': bank_data,
        'order_dict': order_dict,
        'bankcard_datas': bankcard_datas,
    }
    return result


# 银行余额监控
def balanceData_func(bankcard_data):
    bank_data = BankTable.find_one({'uuid': bankcard_data.get('bank_uid')}) or {}
    if not bank_data:
        return

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard_data.get('uuid'), vpn_uuid=bankcard_data.get('vpn_uuid'))
    bcode = bank_data.get('code')
    if bcode == 'ACB':
        bank_cls = ACB.BANK_ACB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                            is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'TPB':
        bank_cls = TPB.BANK_TPB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                            is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'SEAB':
        bank_cls = SEAB.BANK_SEAB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                             is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'ICB':
        bank_cls = BANK_ICB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                            is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'MB':
        bank_cls = MB.BANK_MB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                           is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'NAB':
        bank_cls = NAB.BANK_NAB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'))
        state, result = bank_cls.getBalance()
    elif bcode == 'MSB':
        bank_cls = MSB.BNAK_MSB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                            is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'VAB':
        bank_cls = BANK_VAB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                            is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'BAB':
        bank_cls = BAB.BANK_BAB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'),
                            is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'VIETBANK':
        bank_cls = VIETBANK.BANK_VIETBANK(bankcard_data.get('username'), bankcard_data.get('password'),
                                 bankcard_data.get('account'), is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'VPB':
        bank_cls = VPB.BANK_VPB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'), is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    elif bcode == 'VCB':
        bank_cls = BANK_VCB(bankcard_data.get('username'), bankcard_data.get('password'), bankcard_data.get('account'), is_proxy=vpn_url)
        state, result = bank_cls.getBalance()
    else:
        return
    if not state:
        vkkk = 'sf_bankcard_vpn_' + bankcard_data.get('uuid')
        SiteRedis.dele(vkkk)
        fkkk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fkkk, '1', expire=60 * 25)
        return

    balance = result.get('balance') or 0
    totalBalance = result.get('totalBalance') or 0
    stint_money = bankcard_data.get('stint_money') or 0
    update_form = {
        'balance_amount': balance, 'total_balance': totalBalance, 'update_balance_amount_time': datetime.datetime.now(),
    }
    if bankcard_data.get('balance_amount') != balance:
        update_form['update_newbalance_amount_time'] = datetime.datetime.now()
    if stint_money and balance and balance >= stint_money:
        update_form['statu'] = False
        _data = {
            "title": "超额提示",
            "text": "银行卡：%s, 余额超过设置上限！" % (bankcard_data.get('account')),
            "statu": False
        }
        messageWarnTable.insert_one(_data)

    BankCardTable.update_one({'uuid': bankcard_data.get('uuid')}, {'$set': update_form})
    return result


# 检测银行订单备注
def chackDescription_func(original_string, trg_text):
    original_string = str(original_string).upper()
    cleaned_string = re.sub(r'[^A-Za-z0-9]', '', original_string)
    position = cleaned_string.find(trg_text)
    if position >= 0:
        return True
    return False


# 添加不明收入
def add_unknownIncome(bankcard_data, amount, bank_bill_id, order_note='', note=''):
    if unknownIncomeTable.find_one({'bank_bill_id': bank_bill_id, 'receive_bankacrd_account': bankcard_data.get('account')}):
        return

    _add_Data = {
        'receive_bankacrd_account': bankcard_data.get('account'),
        'state': False,
        'amount': amount,
        'order_note': order_note or '',
        'note': note or '',
        'admin_uid': '',
        'bank_bill_id': bank_bill_id,
        'agentadmin_uuid': bankcard_data.get('agentadmin_uuid') or '',
    }

    is_add = True
    if order_note:
        endtime = datetime.datetime.now()
        statime = endtime - datetime.timedelta(days=3)
        order_note = str(order_note).upper()
        ddl = re.sub(r'[^A-Za-z0-9]', '', order_note)
        p2 = re.compile('R[A-Z]\d{10}')
        number_ls = p2.findall(ddl)
        for nb in number_ls:
            order_data = CollectionOrderTable.find_one({'order_time': {'$gte': statime, '$lte': endtime}, 'order_id': nb})
            if order_data:
                is_add = False
                if bankcard_data.get('account') != order_data.get('payee_bankcard'):
                    is_add = True
                # if order_data.get('pay_statu'):
                #     _add_Data['note'] = '重复支付'
                #     is_add = True
    if is_add:
        unknownIncomeTable.insert_one(_add_Data)


# 添加银行爬虫订单日志
def add_bank_sper_log(bankcard_data, _totalAmount, bank_bill_id, _description, bill_type):
    _ddd = BankCardBillTable.find_one({'bank_bill_id': bank_bill_id, 'bankacrd_uuid': bankcard_data.get('uuid')})
    if _ddd:
        if not _ddd.get('description') and _description.strip():
            BankCardBillTable.update_one({'uuid': _ddd.get('uuid')}, {'$set': {'description': _description.strip()}})
        return
    _bdict = {
        'bankacrd_uuid': bankcard_data.get('uuid'),
        'bankacrd_account': bankcard_data.get('account'),
        'amount': abs(_totalAmount),
        'agentadmin_uuid': bankcard_data.get('agentadmin_uuid'),
        'bill_time': datetime.datetime.now(),
        'bank_bill_id': bank_bill_id,
        'description': _description.strip(),
        'bill_type': bill_type,
    }
    endtime = datetime.datetime.now()
    statime = endtime - datetime.timedelta(days=2)
    cstime = endtime - datetime.timedelta(minutes=21)

    if _bdict.get('description'):
        _description = str(_description).upper()
        ddl = re.sub(r'[^A-Za-z0-9]', '', _description)
        p2 = re.compile('R[A-Z]\d{10}')
        number_ls = p2.findall(ddl)
        is_order = False
        log_bank_order_text = str(bankcard_data.get('account') or '') + '&&&' + str(bank_bill_id or '') + '&&&' + _description
        for nb in number_ls:
            order_data = CollectionOrderTable.find_one({'order_time': {'$gte': statime, '$lte': endtime}, 'order_id': nb})
            if order_data:
                _update_data = {}
                if order_data.get('pay_statu'):
                    _bdict['unusual_type'] = unusualTypes.REPEAT
                    if not order_data.get('is_lose'):
                        _update_data.update({
                            'is_lose': True,
                            'lose_reason': '重复支付',
                        })
                else:
                    _update_data['log_bank_order_text'] = log_bank_order_text
                    if order_data.get('order_time') <= cstime:
                        _bdict['unusual_type'] = unusualTypes.NOT_CALLEDBACK
                        _update_data.update({
                            'actual_amount': int(_totalAmount),
                            'pay_statu': True,
                            'pay_time': datetime.datetime.now(),
                            'is_lose': True,
                            'lose_reason': '订单超时！',
                        })
                        if _totalAmount != order_data.get('order_amount'):
                            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
                            _bdict['unusual_type'] = unusualTypes.DIFFERENT
                    if order_data.get('payee_bankcard') != bankcard_data.get('account'):
                        _bdict['unusual_type'] = unusualTypes.BANKCARD_DIFFERENT
                        _update_data.update({
                            'actual_amount': int(_totalAmount),
                            'pay_statu': True,
                            'pay_time': datetime.datetime.now(),
                            'is_lose': True,
                            'lose_reason': '实际收款卡与订单绑定卡不一致！',
                        })
                        if _totalAmount != order_data.get('order_amount'):
                            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
                            _bdict['unusual_type'] = unusualTypes.DIFFERENT
                if _update_data:
                    CollectionOrderTable.update_one({'uuid': order_data.get('uuid')}, {'$set': _update_data})
                is_order = True
        if not is_order:
            _bdict['unusual_type'] = unusualTypes.NOT_NUMBER

    log_uuid = BankCardBillTable.insert_one(_bdict)
    return log_uuid


# 检测添加数据
def chack_adddata(order_dict, description):
    _order_note = None
    for dk in order_dict.keys():
        if chackDescription_func(description, dk):
            _order_note = dk
            break
    if not _order_note:
        return
    _torder_data = order_dict.get(_order_note)
    if not _torder_data:
        return
    __torder_data = CollectionOrderTable.find_one({'uuid': _torder_data.get('uuid')}) or {}
    if not __torder_data:
        return
    if __torder_data.get('pay_statu'):
        return
    _merchant_data = MerchantTable.find_one({'merchant_id': __torder_data.get('merchant_id')})
    if not _merchant_data:
        return
    result_json = {
        'order_note': _order_note,
        'torder_data': __torder_data,
        'merchant_data': _merchant_data,
    }
    return result_json



# acb银行获取订单
def acb_func(bankcard, bank_data, order_dict, is_manual):
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }
    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    state, bb_datas = ACB.BANK_ACB(username, password, accountNo, rows=100, is_proxy=vpn_url).GET_TRANSACTIONS()
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _type = bb_d.get('type')
        transactionNumber = str(bb_d.get('transactionNumber') or '')
        if _type not in ['IN', 'OUT']:
            continue
        _t_amount = int(float(bb_d.get('amount') or 0))
        if not _t_amount:
            continue
        description = bb_d.get('description') or ''
        bill_type = ''
        if _type == 'IN':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if _type == 'OUT':
            bill_type = BankBillTypes.OUT_ORDER

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _t_amount, transactionNumber, description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _t_amount, bank_bill_id=transactionNumber, order_note=description)
            continue

        result_json = chack_adddata(order_dict, description)
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _t_amount, bank_bill_id=transactionNumber, order_note=description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_t_amount}\n'

        log_bank_order_text = accountNo + '&&&' + str(transactionNumber or '') + '&&&' + description
        _update_data = {
            'actual_amount': int(_t_amount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _t_amount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _t_amount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(1)
                    continue
                is_Callback_success = True
                break
        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return

def ACB_script_func(bankacrd_uuid='', is_manual=False, debug=False):
    crr_bank_code = 'ACB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    task_ls = []
    for bankcard in bankcard_datas:
        acb_func(bankcard, bank_data, order_dict, is_manual)
    #     t = threading.Thread(target=acb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    return True


# TPB银行获取订单
def tpb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'
    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _fo = (time_start - datetime.timedelta(days=1)).strftime('%Y%m%d')
    _ft = time_end.strftime('%Y%m%d')
    state, bb_datas = TPB.BANK_TPB(username, password, accountNo, is_proxy=vpn_url).getHistories(_fo, _ft)
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        category = bb_d.get('category')
        _amount = int(float(bb_d.get('amount') or 0))
        if not _amount:
            continue
        _bid = str(bb_d.get('id') or '')
        description = bb_d.get('description') or ''
        bill_type = ''
        if category == 'transaction_CategoryMoneyIn':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if category == 'transaction_CategoryTransfer' or 'category' not in bb_d:
            bill_type = BankBillTypes.OUT_ORDER
        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _amount, _bid, description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _amount, bank_bill_id=_bid, order_note=description)
            continue

        result_json = chack_adddata(order_dict, description)
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _amount, bank_bill_id=_bid, order_note=description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_amount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + description
        _update_data = {
            'actual_amount': int(_amount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _amount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _amount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(1)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return

def TPB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'TPB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        tpb_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=tpb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# SEAB银行获取订单
def seab_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _fo = (time_start - datetime.timedelta(days=1)).strftime('%Y%m%d')
    _ft = time_end.strftime('%Y%m%d')
    state, bb_datas = SEAB.BANK_SEAB(username, password, accountNo, is_proxy=vpn_url).getTransactions(_fo, _ft)
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return 

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _totalAmount = int(float(bb_d.get('totalAmount') or 0))
        if not _totalAmount:
            continue
        _description = bb_d.get('description') or ''
        _bid = str(bb_d.get('transID') or '')
        bill_type = ''
        __totalAmount = str(bb_d.get('totalAmount') or '')
        if not __totalAmount:
            continue
        if not __totalAmount.startswith('-'):
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if __totalAmount.startswith('-'):
            bill_type = BankBillTypes.OUT_ORDER
        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, _description.strip())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(1)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)
    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def SEAB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'SEAB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return

    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=seab_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True
    for bankcard in bankcard_datas:
        seab_func(bankcard, bank_data, order_dict, is_manual)
    return True


# ICB银行获取订单
def icb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'

    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _fo = (time_start - datetime.timedelta(hours=3)).strftime('%Y-%m-%d')
    _ft = time_end.strftime('%Y-%m-%d')
    state, bb_datas = BANK_ICB(username, password, accountNo, is_proxy=vpn_url, limit=100).getHistories(_fo, _ft)
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return 

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas[:150]:
        is_in = False
        _totalAmount = int(float(bb_d.get('amount') or 0))
        if not _totalAmount:
            continue
        _description = bb_d.get('remark') or ''
        dorC = bb_d.get('dorC')
        if dorC not in ['C', 'D']:
            continue
        _bid = str(bb_d.get('trxId') or '')
        bill_type = ''
        if dorC == 'C':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if dorC == 'D':
            bill_type = BankBillTypes.OUT_ORDER
        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, _description)
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)
    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def ICB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'ICB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        icb_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=icb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# MB银行获取订单
def mb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (time_start - datetime.timedelta(hours=5))
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    state, bb_datas = MB.BANK_MB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start, time_end)
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _totalAmount = int(float(bb_d.get('creditAmount') or 0))
        debitAmount = int(float(bb_d.get('debitAmount') or 0))
        if not _totalAmount and not debitAmount:
            continue

        _description = bb_d.get('description') or ''
        _bid = str(bb_d.get('refNo') or '').replace(' ', '')
        bill_type = ''
        if _totalAmount:
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if debitAmount:
            bill_type = BankBillTypes.OUT_ORDER

        log_uuid = ''
        if bill_type:
            aaa = int(_totalAmount or debitAmount)
            log_uuid = add_bank_sper_log(bankcard, aaa, _bid, _description, bill_type)

        if not order_dict or not _totalAmount:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, _description)
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def MB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'MB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return

    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        mb_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=mb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# NAB银行获取订单(备注小写)
def nab_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (time_start - datetime.timedelta(hours=2))
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    state, bb_datas = NAB.BANK_NAB(username, password, accountNo).get_transaction(time_start.strftime('%d/%m/%Y'), time_end.strftime('%d/%m/%Y'))
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _totalAmount = int(float(bb_d.get('amount') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('description') or ''
        typeTransaction = bb_d.get('typeTransaction')
        if str(typeTransaction).strip() == '1':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if str(typeTransaction).strip() == '0':
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('transactionNumber') or '').replace(' ', '')

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def NAB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'NAB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        nab_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=nab_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# MSB(备注字段：remark，)
def msb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (time_start - datetime.timedelta(hours=2))
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    state, bb_datas = MSB.BNAK_MSB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%Y-%m-%d'))
    if not state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _totalAmount = int(float(bb_d.get('amount') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('remark') or ''
        dcSign = bb_d.get('dcSign') or ''
        if dcSign == 'C':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if dcSign == 'D':
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('coreSn') or '').replace(' ', '')

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def MSB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'MSB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        msb_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=msb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# VAB银行订单获取
def vab_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (datetime.datetime.now() - datetime.timedelta(hours=2))
    time_end = time_end + datetime.timedelta(days=1)

    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }

    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))

    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _state, bb_datas = BANK_VAB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%d/%m/%Y'), time_end.strftime('%d/%m/%Y'))

    if not _state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _totalAmount = int(float(bb_d.get('transactionAmount') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('description') or ''
        creditDebitFlag = bb_d.get('creditDebitFlag') or ''
        if creditDebitFlag == 'C':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if creditDebitFlag == 'D':
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('txnRefNumber') or '').replace(' ', '')

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return

def VAB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'VAB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=vab_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True
    for bankcard in bankcard_datas:
        vab_func(bankcard, bank_data, order_dict, is_manual)
    return True



# BAB银行脚本
def bsb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (datetime.datetime.now() - datetime.timedelta(hours=2))
    time_end = time_end + datetime.timedelta(days=2)
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }
    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _state, bb_datas = BAB.BANK_BAB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%d/%m/%Y'), time_end.strftime('%d/%m/%Y'))
    if not _state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas:
        is_in = False
        _totalAmount = int(float(str(bb_d.get('amount') or '').replace(',', '') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('description') or ''
        __totalAmount = str(bb_d.get('amount') or '')
        if not __totalAmount:
            continue
        if not __totalAmount.startswith('-'):
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if __totalAmount.startswith('-'):
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('transaction_iD') or '').replace(' ', '')

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def BAB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'BAB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        bsb_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=bsb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# BANK_VIETBANK
def vietbank_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (datetime.datetime.now() - datetime.timedelta(hours=2))
    time_end = time_end + datetime.timedelta(days=2)
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }
    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))

    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _state, bb_datas = VIETBANK.BANK_VIETBANK(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%d-%m-%Y'), time_end.strftime('%d-%m-%Y'))

    if not _state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas[:150]:
        is_in = False
        _totalAmount = int(float(str(bb_d.get('amount') or '').replace(',', '') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('description') or ''
        __totalAmount = str(bb_d.get('amount') or '')
        if not __totalAmount:
            continue
        if not __totalAmount.startswith('-'):
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if __totalAmount.startswith('-'):
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('transaction_id') or '').replace(' ', '')

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def VIETBANK_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'VIETBANK'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    for bankcard in bankcard_datas:
        vietbank_func(bankcard, bank_data, order_dict, is_manual)
    return True
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=vietbank_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True


# VPB
def vpb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (datetime.datetime.now() - datetime.timedelta(hours=2))
    time_end = time_end + datetime.timedelta(days=2)
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }
    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))

    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    _state, bb_datas = VPB.BANK_VPB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%d/%m/%Y'), time_end.strftime('%d/%m/%Y'))
    if not _state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(bb_datas)}条数据。\n'
    bb_datas.reverse()
    for bb_d in bb_datas[:150]:
        is_in = False
        _totalAmount = int(float(str(bb_d.get('Amount') or '').replace(',', '') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('Description') or ''
        __totalAmount = str(bb_d.get('Amount') or '')
        if not __totalAmount:
            continue
        if not __totalAmount.startswith('-'):
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if __totalAmount.startswith('-'):
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('TRANSACTIONCODE') or '').replace(' ', '')

        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def VPB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'VPB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=vpb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True
    for bankcard in bankcard_datas:
        vpb_func(bankcard, bank_data, order_dict, is_manual)
    return True



# VCB
def vcb_func(bankcard, bank_data, order_dict, is_manual):
    time_start, time_end = getDayDateSilce()
    time_start = (datetime.datetime.now() - datetime.timedelta(hours=2))
    _log_text = ''
    _log_data = {
        'bankcrad_uid': bankcard.get('uuid'),
        'is_is_manual': is_manual or False,
    }
    _result = balanceData_func(bankcard)
    if _result:
        balance = _result.get('balance') or 0
        totalBalance = _result.get('totalBalance') or 0
        _log_text += f'可用余额：{balance}，真实余额：{totalBalance}\n'
    else:
        _log_text += f'余额获取失败！\n'

    vpn_url = get_vpnurl(bank_data, bankcard_uuid=bankcard.get('uuid'), vpn_uuid=bankcard.get('vpn_uuid'))
    if vpn_url:
        _log_text += f'当前IP：{vpn_url}\n'
    else:
        _log_text += f'当前IP：服务器本地IP！\n'
    username = bankcard.get('username')
    password = bankcard.get('password')
    accountNo = bankcard.get('account')
    # _state, bb_datas = BANK_VPB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%d/%m/%Y'), time_end.strftime('%d/%m/%Y'))
    datas = []
    tt_state = True
    for i in range(8):
        time.sleep(0.5)
        _state, bb_datas = BANK_VCB(username, password, accountNo, is_proxy=vpn_url).getHistories(time_start.strftime('%d/%m/%Y'), time_end.strftime('%d/%m/%Y'), page=i)
        if not _state:
            tt_state = False
            break
        if not bb_datas:
            break
        datas += bb_datas
    if not tt_state:
        _log_text += f'订单获取失败！\n'
        _log_data['log_text'] = _log_text
        BankScriptLogTable.insert_one(_log_data)
        vkkk = 'sf_bankcard_vpn_' + bankcard.get('uuid')
        SiteRedis.dele(vkkk)
        fffk = 'vpn_' + vpn_url.strip()
        SiteRedis.set(fffk, '1', expire=60 * 25)
        return

    _log_text += f'订单获取成功！共{len(datas)}条数据。\n'
    # bb_datas.reverse()
    for bb_d in datas[:150]:
        is_in = False
        _totalAmount = int(float(str(bb_d.get('Amount') or '').replace(',', '').replace('-', '').replace('+', '') or 0))
        if not _totalAmount:
            continue

        bill_type = ''
        _description = bb_d.get('Description') or ''
        __CD = str(bb_d.get('CD') or '')
        if not __CD:
            continue
        if __CD == '+':
            is_in = True
            bill_type = BankBillTypes.INCOME_ORDER
        if __CD == '-':
            bill_type = BankBillTypes.OUT_ORDER
        _bid = str(bb_d.get('PostingTime') or '').replace(' ', '')+str(_totalAmount).replace('-','').replace('+','')
        log_uuid = ''
        if bill_type:
            log_uuid = add_bank_sper_log(bankcard, _totalAmount, _bid, _description, bill_type)

        if not order_dict:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        result_json = chack_adddata(order_dict, str(_description).upper())
        if not result_json:
            if is_in:
                add_unknownIncome(bankcard, _totalAmount, bank_bill_id=_bid, order_note=_description)
            continue

        order_note = result_json.get('order_note')
        torder_data = result_json.get('torder_data')
        merchant_data = result_json.get('merchant_data')
        _log_text += f'备注：{order_note}，金额：{_totalAmount}\n'

        log_bank_order_text = accountNo + '&&&' + str(_bid or '') + '&&&' + _description
        _update_data = {
            'actual_amount': int(_totalAmount),
            'pay_statu': True,
            'pay_time': datetime.datetime.now(),
            'log_bank_order_text': log_bank_order_text,
        }
        if _totalAmount != torder_data.get('order_amount'):
            _update_data['is_lose'] = True
            _update_data['lose_reason'] = '实际支付金额和订单金额不一致！'
            BankCardBillTable.update_one({'uuid': log_uuid}, {'$set': {'unusual_type': unusualTypes.DIFFERENT}})

        CollectionOrderTable.update_one({'uuid': torder_data.get('uuid')}, {'$set': _update_data})
        order_dict.pop(order_note)

        is_Callback_success = False
        if _totalAmount == torder_data.get('order_amount'):
            for i in range(3):
                _state, _res = CallbackPayOrderFunc(torder_data.get('uuid'))
                if not _state:
                    time.sleep(0.5)
                    continue
                is_Callback_success = True
                break

        if is_Callback_success:
            payIncome_addto(order_uuid=torder_data.get('uuid'), merchant_data=merchant_data)

    _log_data['log_text'] = _log_text
    BankScriptLogTable.insert_one(_log_data)
    return True

def VCB_script_func(bankacrd_uuid='', is_manual=False):
    crr_bank_code = 'VCB'
    result = getTaskOrder(crr_bank_code, bankacrd_uuid=bankacrd_uuid, is_manual=is_manual)
    if not result:
        return
    bank_data = result.get('bank_data')
    order_dict = result.get('order_dict')
    bankcard_datas = result.get('bankcard_datas')
    # task_ls = []
    # for bankcard in bankcard_datas:
    #     t = threading.Thread(target=vcb_func, args=(bankcard, bank_data, order_dict, is_manual))
    #     task_ls.append(t)
    #     t.start()
    # while task_ls:
    #     _v = task_ls[0]
    #     if not _v.is_alive():
    #         del task_ls[0]
    #         continue
    #     time.sleep(1)
    # return True
    for bankcard in bankcard_datas:
        vcb_func(bankcard, bank_data, order_dict, is_manual)
    return True


