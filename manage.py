# -*- coding: utf-8 -*-
import json
import os
import random
import time
import click
import base64
import shortuuid
import requests
import datetime
from app_pay2w import app, ProjectConfig
from models.cms_user import CmsUserTable
from common_utils.lqredis import SiteRedis
from constants import PERMISSION_ALL, ROlE_ALL, CallbackState, ASSETS_FOLDER, taskStatus, BILL_STATEMEN_TYPES
from models.cms_table import SiteConfigTable
from models.pay_table import CollectionOrderTable, messageWarnTable, BankCardTable, BankScriptLogTable, ScriptLogTable
from modules.view_helpres.bank_func import ACB_script_func, SEAB_script_func, TPB_script_func, ICB_script_func, MB_script_func, NAB_script_func, MSB_script_func, VAB_script_func, BAB_script_func, VIETBANK_script_func, VPB_script_func, VCB_script_func
from models.behalfPay import behalfPayTaskTable, behalfPayOrderTable


@click.group()
def mainFunc():
    pass


@mainFunc.command()
@click.option('--account', '-t')
@click.option('--password', '-p')
def init_admin(account, password):
    """ 初始化admin用户 """
    if not account.strip():
        return '请输入登录账户!'
    if not password:
        password = 'admin123'
    # CmsUserTable.delete_many({})
    user_data = {
        'account': account.strip(),
        'password': CmsUserTable.encry_password(password.strip()),
        'username': 'Root管理员',
        'statu': True,
        'permissions': [PERMISSION_ALL.SUPERADMIN],
        '_current_login': '',
        'is_activate': False,
        'role_code': ROlE_ALL.SUPERADMIN,
    }
    CmsUserTable.insert_one(user_data)
    return '%s: 用户添加成功!'%account


@mainFunc.command()
def init_index():
    """创建索引"""
    from common_utils.mongodb.mongo_model import dbModel
    for MCLS in dbModel.__subclasses__():
        if not hasattr(MCLS, '__tablename__') or not getattr(MCLS, '__tablename__'):
            continue
        indexs = MCLS.index_information()
        for k, v in MCLS.fields().items():
            if not hasattr(v, 'is_index'):
                continue
            if not getattr(v, 'is_index'):
                continue
            # print('%s_1' % k, indexs.get('%s_1' % k))
            if not indexs.get('%s_1' % k) and v.is_index:
                print(k, MCLS.create_index(k))
        default_k = ['uuid', 'create_time']
        for k in default_k:
            if not indexs.get('%s_1' % k):
                print(k, MCLS.create_index(k))


@mainFunc.command()
def update_primary_key():
    """更细项目字段主键"""
    print('更新项目字段主键KEY')
    for _k in SiteRedis.get_keys():
        _k = _k.decode()
        if ProjectConfig.PROJECT_NAME in _k and '_field' in _k:
            SiteRedis.dele(_k)
    from common_utils.mongodb.mongo_model import dbModel
    for MCLS in dbModel.__subclasses__():
        if not hasattr(MCLS, '__tablename__') or not getattr(MCLS, '__tablename__'):
            continue
        table_name = getattr(MCLS, '__tablename__')
        for db_field, v_Cls in MCLS.fields().items():
            if not hasattr(v_Cls, 'field_type'):
                continue
            if v_Cls.primary_key:
                v_dict = MCLS.find_one({}, sort=[[db_field, -1]])
                if v_dict:
                    kk_v = v_dict.get(db_field) or 0
                    _redis_check_key = '%s_%s_%s_%s_field' % (ProjectConfig.PROJECT_NAME, ProjectConfig.MONGODB_DB, table_name, db_field)
                    SiteRedis.set(_redis_check_key, kk_v)
                    print(table_name, db_field, kk_v)
    print('项目字段主键KEY更新完毕！')


@mainFunc.command()
def update_secret_key():
    site_data = CmsUserTable.find_one({'project_name': app.config.get("PROJECT_NAME")}) or {}
    new_secret_key = base64.b64encode(os.urandom(66)).decode()
    site_data['secret_key'] = new_secret_key
    SiteConfigTable.save(site_data)
    print('success!')


@mainFunc.command()
def update_loseorder():
    '''
    掉单
    '''
    while True:
        print('order polling...')
        crr_time = datetime.datetime.now() - datetime.timedelta(minutes=25)
        datas = CollectionOrderTable.find_many({'is_lose': False, 'pay_statu': True, 'callback_statu': {'$in': [CallbackState.FAILED, CallbackState.NOT_CALLEDBACK]},  'order_time': {'$gte': crr_time}})
        if not datas:
            time.sleep(10)
            continue
        for da in datas:
            pay_time = da.get('pay_time')
            if pay_time:
                pay_time = pay_time + datetime.timedelta(minutes=1)
                if pay_time < datetime.datetime.now():
                    CollectionOrderTable.update_one({'uuid': da.get('uuid')}, {'$set': {'is_lose': True, 'lose_reason': '已付未回调成功!'}})
                    _data = {
                        "title": "掉单提示",
                        "text": "订单：%s, 超时未回调，进入掉单！" % (da.get('order_id')),
                        "statu": False
                    }
                    messageWarnTable.insert_one(_data)

        time.sleep(10)


@mainFunc.command()
def run_acb_task():
    '''
    银行卡获取历史订单
    '''
    while True:
        print('acb log...')
        ACB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_tpb_task():
    '''
    银行卡获取历史订单
    '''
    while True:
        print('tpb log...')
        TPB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_seab_task():
    '''
    SEAB 银行卡获取历史订单
    '''
    while True:
        print('seab log...')
        SEAB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_icb_task():
    '''
    SEAB 银行卡获取历史订单
    '''
    while True:
        print('icb log...')
        ICB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_mb_task():
    '''
    MB 银行卡获取历史订单
    '''
    while True:
        print('mb log...')
        MB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_nab_task():
    '''
    NAB 银行卡获取历史订单
    '''
    while True:
        print('nab log...')
        NAB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_msb_task():
    '''
    NAB 银行卡获取历史订单
    '''
    while True:
        print('msb log...')
        MSB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_vab_task():
    '''
    NAB 银行卡获取历史订单
    '''
    while True:
        print('vab log...')
        VAB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_bab_task():
    '''
    BAB 银行卡获取历史订单
    '''
    while True:
        print('bab log...')
        BAB_script_func()
        time.sleep(5)


@mainFunc.command()
def run_vietbank_task():
    '''
    vietbank 银行卡获取历史订单
    '''
    while True:
        print('vietbank log...')
        VIETBANK_script_func()
        time.sleep(5)


@mainFunc.command()
def run_vpb_task():
    '''
    VPB 银行卡获取历史订单
    '''
    while True:
        print('vietbank log...')
        VPB_script_func()
        time.sleep(8)


@mainFunc.command()
def run_vcb_task():
    '''
    vcb 银行卡获取历史订单
    '''
    while True:
        print('vietbank log...')
        VCB_script_func()
        time.sleep(8)


@mainFunc.command()
def behalfpay_payqrcode():
    from models.pay_table import BankTable
    from modules.view_helpres.view_func import getPayQrcode_func2, getPayQrcode_func, img_base4_save
    while True:
        print('payQrcode start ...')
        end_time = datetime.datetime.now()
        start_time = end_time - datetime.timedelta(minutes=30)
        datas = behalfPayOrderTable.find_many({'payqrcode_url': {'$exists': False}, 'create_time': {'$gte': start_time, '$lte': end_time}})
        if not datas:
            time.sleep(8)
            continue
        for data in datas:
            payqrcode_url = data.get('payqrcode_url')
            if payqrcode_url:
                continue
            bank_data = BankTable.find_one({'code': data.get('receive_bank_code')})
            if not bank_data:
                continue
            satte, payQrcode = getPayQrcode_func2(
                accountNo=data.get('receive_account'),
                bank_code=bank_data.get('code'),
                shortName=bank_data.get('shortName'),
                bank_name=bank_data.get('name'),
                bank_bin=bank_data.get('bin'),
                amount=data.get('order_amount'),
                addInfo=data.get('bank_memo'),
            )
            if not satte:
                satte, payQrcode = getPayQrcode_func(
                    accountNo=data.get('receive_account'),
                    bank_code=bank_data.get('code'),
                    shortName=bank_data.get('shortName'),
                    bank_name=bank_data.get('name'),
                    bank_bin=bank_data.get('bin'),
                    amount=data.get('order_amount'),
                    addInfo=data.get('bank_memo'),
                )
                if not satte:
                    continue
            relatively_path = f'/assets/payimg/'
            project_static_folder = os.path.join(app.static_folder, app.config.get('PROJECT_NAME'))
            import_folder = project_static_folder + relatively_path
            if not os.path.exists(import_folder):
                os.makedirs(import_folder)
            new_filename = datetime.datetime.now().strftime('%Y%m%d') + '_' + str(shortuuid.uuid())
            img_base4_save(payQrcode, import_folder + new_filename + '.jpg')
            payqrcode_url = relatively_path + new_filename + '.jpg'
            behalfPayOrderTable.update_one({'uuid': data.get('uuid')}, {'$set': {'payqrcode_url': payqrcode_url}})
        time.sleep(5)


@mainFunc.command()
def collection_callback_order():
    from modules.view_helpres.view_func import CallbackPayOrderFunc, payIncome_addto
    from models.pay_table import MerchantTable
    while True:
        print('callback start ...')
        end_time = datetime.datetime.now()
        start_time = end_time - datetime.timedelta(hours=6)
        datas = CollectionOrderTable.find_many({'callback_statu': CallbackState.FAILED, 'create_time': {'$gte': start_time, '$lte': end_time}})
        for data in datas:
            callbank_try = data.get('callbank_try') or 3
            callback_time = data.get('callback_time')
            if callbank_try >= 5:
                continue
            if callback_time and callback_time + datetime.timedelta(minutes=2) >= datetime.datetime.now():
                continue
            _state, _res = CallbackPayOrderFunc(data.get('uuid'))
            if _state:
                merchant_data = MerchantTable.find_one({'merchant_id': data.get('merchant_id')}) or {}
                if not merchant_data:
                    continue
                payIncome_addto(order_uuid=data.get('uuid'), merchant_data=merchant_data)
        time.sleep(8)


@mainFunc.command()
def behalfpay_callback_order():
    from modules.view_helpres.view_func import behalfPayCallbackOrderFunc
    while True:
        print('callback start ...')
        end_time = datetime.datetime.now()
        start_time = end_time - datetime.timedelta(hours=6)
        datas = behalfPayOrderTable.find_many({'callback_statu': CallbackState.FAILED, 'create_time': {'$gte': start_time, '$lte': end_time}})
        for data in datas:
            callbank_try = data.get('callbank_try') or 3
            callback_time = data.get('callback_time')
            if callbank_try >= 5:
                continue
            if callback_time and callback_time + datetime.timedelta(minutes=2) >= datetime.datetime.now():
                continue
            _state, _res = behalfPayCallbackOrderFunc(data.get('uuid'))
        time.sleep(8)



@mainFunc.command()
def bankcard_unusual_monitor():
    while True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'bankcard_unusual_monitor ...', flush=True)
        bankcard_datas = BankCardTable.find_many({'statu': True})
        for bankcard_data in bankcard_datas:
            auto_removal_time = bankcard_data.get('auto_removal_time')
            turn_auto_removal_time = bankcard_data.get('turn_auto_removal_time')
            if not auto_removal_time:
                continue
            try:
                auto_removal_time = int(auto_removal_time)
            except:
                continue
            if not turn_auto_removal_time:
                continue
            if not isinstance(turn_auto_removal_time, datetime.datetime):
                continue
            crr_time = datetime.datetime.now()
            start_time = crr_time - datetime.timedelta(minutes=auto_removal_time)
            if start_time < turn_auto_removal_time:
                continue

            order_counts = CollectionOrderTable.count({'bankcard_id': bankcard_data.get('uuid'),  'order_time': {'$gte': start_time, '$lte': crr_time}})
            not_call_counts = CollectionOrderTable.count({'bankcard_id': bankcard_data.get('uuid'),  'order_time': {'$gte': start_time, '$lte': crr_time}, 'callback_statu': CallbackState.NOT_CALLEDBACK})
            if order_counts and not_call_counts >= order_counts:
                BankCardTable.update_one({'uuid': bankcard_data.get('uuid')}, {'$set': {'is_abnormal': True, 'statu': False}})
                _text = f'自动下架，卡号：{bankcard_data.get("account")}, 原因：规定时间内无回调订单！'
                ScriptLogTable.insert_one({'note': _text})
                continue

            blog_data = BankScriptLogTable.find_one({}, sort=[['create_time', -1]])
            if blog_data and blog_data.get('create_time') < start_time:
                BankCardTable.update_one({'uuid': bankcard_data.get('uuid')}, {'$set': {'is_abnormal': True, 'statu': False}})
                _text = f'自动下架，卡号：{bankcard_data.get("account")}, 原因：规定时间爬虫无更新数据！'
                ScriptLogTable.insert_one({'note': _text})
                continue
        time.sleep(8)



@mainFunc.command()
def init_bank_data():
    import requests
    from constants import PAY_METHOD
    from models.pay_table import BankTable,TunnelTable
    bank_url = 'https://api.vietqr.io/v2/banks'
    req = requests.get(bank_url)
    data_json = req.json().get('data') or []
    if data_json:
        for dj in data_json:
            _code = dj.get('code') or ''
            if BankTable.find_one({'code': _code}):
                continue
            project_static_file = os.path.join(app.static_folder, app.config.get('PROJECT_NAME'), ASSETS_FOLDER, 'bank', 'img')
            if not os.path.exists(project_static_file):
                os.makedirs(project_static_file)
            remm = requests.get(dj.get('logo')).content
            with open(project_static_file + '/' + _code + '.png', 'wb') as wf:
                wf.write(remm)
            dj['local_logo'] = (project_static_file + '/' + _code + '.png').replace(app.static_folder+'/'+app.config.get('PROJECT_NAME'), '')
            BankTable.insert_one(dj)

    for pm in PAY_METHOD.name_arr:
        if TunnelTable.find_one({'code': pm}):
            continue
        _data = {
            'tunnel_name': PAY_METHOD.name_dict.get(pm),
            'code': pm,
            'tunnel_statu': False,
        }
        TunnelTable.insert_one(_data)


@mainFunc.command()
def behalfPayTask():
    while True:
        crrtime = datetime.datetime.now() - datetime.timedelta(minutes=30)
        datas = behalfPayTaskTable.find_many({'statu': taskStatus.processing, 'create': {'$lte': crrtime}}) or []
        if not datas:
            time.sleep(5)
            continue
        for dt in datas:
            behalfPayTaskTable.update_one({'uuid': dt.get('uuid')}, {'$set': {'statu': taskStatus.failed, 'note': '任务超时'}})


@mainFunc.command()
def test():
    from modules.bank_module.ACB import BANK_ACB
    from modules.bank_module.MB import BANK_MB
    from modules.bank_module.MSB import BNAK_MSB
    from modules.bank_module.VAB import BANK_VAB
    from modules.bank_module.NAB import BANK_NAB
    from modules.bank_module.SEAB import BANK_SEAB
    from modules.bank_module.VPB import BANK_VPB
    from modules.bank_module.TPB import BANK_TPB
    from modules.bank_module.ICB import BANK_ICB
    from modules.bank_module.BAB import BANK_BAB
    from modules.bank_module.TCB import BANK_TCB
    from models.pay_table import BankCardTable, BankTable

    username = "0868082974"
    password = "Huy2200@"
    account_number = "19071752244011"
    bb = BANK_TCB(username, password, account_number)
    # print(bb.doLogin())
    print(bb.getBalance())


@mainFunc.command()
def test1():
    from constants import PAY_METHOD
    from models.cms_user import CmsUserTable
    from models.behalfPay import behalfPayOrderTable, CnBankCardTable
    from models.pay_table import BankScriptLogTable, unknownIncomeTable, BankCardBillTable, BankTable, MerchantTable, callbackLogTable, BankCardTable, TunnelTable, MerchantTunnleTable, ApiRequestLogTable, MerchantBillStatementTable
    from constants import TUNNLE_METHOD, MERCHANT_ROLES

    ppp = '/www/pay2world/static/project_pay2world/assets/payimg/'
    datas = os.listdir(ppp)
    print(datas[0])
    print('datas:', len(datas))
    # cc = '20240203'
    # c = 0
    # for data in datas:
    #     c += 1
    #     _V = data.split('_')[0]
    #     if _V <= cc:
    #         os.remove(ppp+data)
    #     if c % 100 == 0:
    #         print('crr:', c)

if __name__ == '__main__':
    mainFunc()
