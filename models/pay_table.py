from . import dbModel
from werkzeug.security import generate_password_hash, check_password_hash



class MerchantTable(dbModel):
    '''
    商户
    '''
    __tablename__ = 'merchant_table'
    merchant_id = dbModel.StringField('商户ID', default=10000, is_index=True)
    merchant_name = dbModel.StringField('商户名称', is_index=True)
    balance_amount = dbModel.FloatField('可用余额')
    freeze_amount =  dbModel.FloatField('冻结金额')
    statu = dbModel.BooleanField('状态', is_index=True)
    account = dbModel.StringField('登录账户名', nullable=False, is_index=True)
    password = dbModel.PasswordField('密码', nullable=False)
    note = dbModel.StringField('备注')
    current_login = dbModel.DateTimeField('最后登录时间')
    current_login_ip = dbModel.StringField('最后登录IP')
    last_login_time = dbModel.DateTimeField('上次登录时间')
    last_login_ip = dbModel.StringField(u'上次登录IP')
    is_activate = dbModel.BooleanField('激活状态')
    is_review = dbModel.BooleanField('审核状态')
    payment_rate = dbModel.FloatField('代付默认利率')
    issued_money_rate = dbModel.FloatField('下发默认利率')
    recharge_money_rate = dbModel.FloatField('内充默认利率')
    secret_key = dbModel.StringField('密钥')
    cms_ip_whitelist = dbModel.StringField('登录ip白名单')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    is_syscard = dbModel.BooleanField('是否使用系统银行卡')
    ip_whitelist = dbModel.StringField('IP白名单')
    logoUrl = dbModel.StringField('Logo地址')
    collect_money_switch = dbModel.BooleanField('代收功能')
    paybehalf_switch = dbModel.BooleanField('代付功能')
    paybehalf_max_money = dbModel.IntegerField('代付金额最大值')
    paybehalf_min_money = dbModel.IntegerField('代付金额最小值')
    role_code = dbModel.StringField('角色')
    upper_mid = dbModel.StringField('上级id', is_index=True)
    account_name = dbModel.StringField('账户名称', is_index=True)

    @classmethod
    def encry_password(cls, raspwd):
        return generate_password_hash(raspwd)

    @classmethod
    def check_password(cls, pwd, rawpwd):
        """
        :param pwd: 密文
        :param rawpwd: 明文
        """
        return check_password_hash(pwd, rawpwd)

    @classmethod
    def field_search(cls):
        return [
            'merchant_id',
            'note',
            'merchant_name',
            'account',
            'agentadmin_uuid',
            'create_time',
            'role_code',
        ]



class AgentadminBillLogTable(dbModel):
    '''
    代理账单
    '''
    __tablename__ = 'agentadmin_bill_log_table'
    agentadmin_uuid = dbModel.StringField('代理UUID', is_index=True)
    amount = dbModel.IntegerField('金额')
    balance_amount = dbModel.FloatField('当前余额')
    bill_type = dbModel.StringField('账单类型')
    note = dbModel.StringField('备注')
    pay_method = dbModel.StringField('交易模式')
    repay_amount = dbModel.FloatField('手续费')
    order_id = dbModel.StringField('订单号', is_index=True)
    merchant_id = dbModel.StringField('商户ID', is_index=True)
    merchant_order_id = dbModel.StringField('商户订单号', is_index=True)
    @classmethod
    def field_search(cls):
        return [
            'amount',
            'bill_type',
            'note',
            'order_id',
            'merchant_order_id',
            'merchant_id',
        ]



class MerchantTunnleTable(dbModel):
    '''
    商家通道
    '''
    __tablename__ = 'merchant_tunnle_table'
    tunnle_name = dbModel.StringField('通道名称')
    tunnle_id = dbModel.StringField('通道id')
    statu = dbModel.BooleanField('状态')
    single_amount_max = dbModel.IntegerField('单笔金额最大')
    single_amount_min = dbModel.IntegerField('单笔金额最小')
    merchant_uuid = dbModel.StringField('商户uuId')
    rate = dbModel.FloatField('利率%')
    tunnle_method = dbModel.StringField('通道模式')


class WithdrawalCardTable(dbModel):
    '''
    商家银行卡
    '''
    __tablename__ = 'withdrawl_card_table'
    bank_uid = dbModel.StringField('银行', is_index=True)
    admin_uuid = dbModel.StringField('商户uuId', is_index=True)
    account = dbModel.StringField('银行卡账户', is_index=True)
    bank_name = dbModel.StringField('银行名字', is_index=True)
    location = dbModel.StringField('地点', is_index=True)
    balance_amount = dbModel.FloatField('余额', is_index=True)
    start_money = dbModel.FloatField('起始资金', is_index=True)
    deposit_uuid = dbModel.StringField('银行卡用于存款', is_index=True)
    payer_uuids = [] #dbModel.StringField('商户uuId', is_index=True)
    is_deleted = dbModel.BooleanField('有订购', is_index=True)
    # withdraw_amount = dbModel.FloatField('提款余额', is_index=True)

    total_request = dbModel.FloatField('余额', is_index=True)
    total_transfer_out = dbModel.FloatField('余额', is_index=True)
    total_transfer_in = dbModel.FloatField('余额', is_index=True)
    total_other_transfer_in = dbModel.FloatField('余额', is_index=True)
    total_other_transfer_out = dbModel.FloatField('余额', is_index=True)
    total_issue = dbModel.FloatField('余额', is_index=True)
    total_init_money = dbModel.FloatField('余额', is_index=True)

    
    current_date = dbModel.StringField('银行卡用于存款', is_index=True)

    note = dbModel.StringField('注解', is_index=True)
    is_order = dbModel.BooleanField('有订购', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'bank_uid', 'account', 'bank_name','location','admin_uuid','note',
        ]


class WithdrawalOrderLogTable(dbModel):
    '''
    商家银行卡
    '''
    __tablename__ = 'withdrawl_order_log_table'
    
    admin_uuid = dbModel.StringField('管理员uuId', is_index=True)
    operator_uuid = dbModel.StringField('管理员uuId', is_index=True)
    operator_agent_uuid = dbModel.StringField('管理员uuId', is_index=True)
    payer_uuids = []#dbModel.StringField('用户uuId', is_index=True)

    former_card_uuid = dbModel.StringField('银行卡uuid', is_index=True)
    former_location = dbModel.StringField('银行卡uuid', is_index=True)
    former_bankcard_account = dbModel.StringField('转出银行卡账户', is_index=True)
    former_bank_code = dbModel.StringField('转出银行代码', is_index=True)
    former_bank_name = dbModel.StringField('转出银行姓名', is_index=True)
    former_cur_balance = dbModel.FloatField('当前余额', is_index=True)
    former_pre_balance = dbModel.FloatField('先前余额', is_index=True)

    latter_card_uuid = dbModel.StringField('转入银行卡账户', is_index=True)
    latter_location = dbModel.StringField('转入银行卡账户', is_index=True)
    latter_bankcard_account = dbModel.StringField('转入银行卡账户', is_index=True)
    latter_bank_code = dbModel.StringField('转入银行代码', is_index=True)
    latter_bank_name = dbModel.StringField('转入银行姓名', is_index=True)
    latter_cur_balance = dbModel.FloatField('当前余额', is_index=True)
    latter_cur_balance = dbModel.FloatField('先前余额', is_index=True)

    transfer_money = dbModel.FloatField('请求金额', is_index=True)
    request_money = dbModel.FloatField('请求金额', is_index=True)

    order_status = dbModel.StringField('订单状态', is_index=True)
    accepted_status = dbModel.StringField('订单状态', is_index=True)

    behavior = dbModel.StringField('行为', is_index=True)
    payqrcode_url = dbModel.StringField('QRCode', is_index=True)
    note = dbModel.StringField('注解', is_index=True)

    pay_time = dbModel.DateTimeField('支付时间')
    order_time = dbModel.DateTimeField('订单时间', nullable=False)

    @classmethod
    def field_search(cls):
        return [
            'bank_uid', 'account', 'account_username','former_location','latter_location','admin_uuid', 'transfer_money'
        ]



class MerchantBankCardTable(dbModel):
    '''
    商家银行卡
    '''
    __tablename__ = 'merchant_bankcard_table'
    bank_uid = dbModel.StringField('银行', is_index=True)
    account = dbModel.StringField('银行卡账户', is_index=True)
    account_username = dbModel.StringField('账户人姓名', is_index=True)
    merchant_uuid = dbModel.StringField('商户uuId', is_index=True)
    @classmethod
    def field_search(cls):
        return [
            'bank_uid', 'account', 'account_username'
        ]

class MerchantLogTable(dbModel):
    '''
    商户操作日志
    '''
    __tablename__ = 'merchant_log_table'
    merchant_uuid = dbModel.StringField('商户uuId', is_index=True)
    ip = dbModel.StringField('登录IP', is_index=True)
    ua = dbModel.StringField('UA')
    address = dbModel.StringField('地理位置')



class MerchantBillStatementTable(dbModel):
    '''
    商户资金流水
    '''
    __tablename__ = 'merchant_bill_statement_table'
    merchant_uuid = dbModel.StringField('商户uuId', is_index=True)
    start_balance = dbModel.FloatField('原余额')
    amount = dbModel.IntegerField('金额')
    balance_amount = dbModel.FloatField('当前余额')
    repay_amount = dbModel.FloatField('手续费')
    bill_type = dbModel.StringField('账单类型')
    note = dbModel.StringField('备注')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    order_id = dbModel.StringField('订单号', is_index=True)
    merchant_order_id = dbModel.StringField('商户订单号', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'merchant_uuid',
            'amount',
            'bill_type',
            'create_time',
            'order_id',
            'merchant_order_id',
            'note'
        ]



class BankTable(dbModel):
    '''
    银行
    '''
    __tablename__ = 'back_table'
    name = dbModel.StringField('银行名称', is_index=True)
    shortName = dbModel.StringField('银行简称', is_index=True)
    code = dbModel.StringField('银行代码', is_index=True)
    bin = dbModel.StringField('银行编码', is_index=True)
    logo = dbModel.StringField('logo')
    local_logo = dbModel.StringField('logo本地地址')
    transferSupported = dbModel.StringField('银行APP支持扫描VietQR码转账')
    lookupSupported = dbModel.StringField('可以使用账号查找API来查找银行账户')
    statu = dbModel.BooleanField('状态')
    is_ip_pool = dbModel.BooleanField('IP池状态')
    ip_single_period = dbModel.IntegerField('IP单次有效期/秒')
    ip_disable_period = dbModel.IntegerField('IP单次禁用时间/秒')
    ips = dbModel.StringField('IP池')

    @classmethod
    def field_search(cls):
        return [
            'statu', 'name', 'code'
        ]



class BankCardTable(dbModel):
    '''
    银行卡
    '''
    __tablename__ = 'bankcard_table'
    name = dbModel.StringField('名称', is_index=True)
    username = dbModel.StringField('银行卡用户名', is_index=True)
    password = dbModel.StringField('银行卡密码', is_index=True)
    account = dbModel.StringField('银行卡账户', is_index=True)
    account_username = dbModel.StringField('账户人姓名', is_index=True)
    index = dbModel.IntegerField('序值', is_index=True, primary_key=True)
    bank_uid = dbModel.StringField('银行', is_index=True)
    balance_amount = dbModel.FloatField('余额')
    total_balance =  dbModel.FloatField('真实余额')
    collection_money_min = dbModel.IntegerField('收款最小金额')
    collection_money_max = dbModel.IntegerField('收款最大金额')
    statu = dbModel.BooleanField('状态', is_index=True)
    day_collection_money_limit = dbModel.IntegerField('日收款金额上限')
    day_collection_pencount_limit = dbModel.IntegerField('日收款笔数上限')
    note = dbModel.StringField('备注')
    create_time = dbModel.DateTimeField('时间', nullable=False)
    merchant_uid = dbModel.StringField('商户UUID')
    stint_money = dbModel.IntegerField('限制提醒金额')
    start_money = dbModel.IntegerField('初始资金')
    vpn_uuid = dbModel.StringField('VPN UUID')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    bankcard_type = dbModel.StringField('银行卡类型', is_index=True)
    script_statu = dbModel.BooleanField('脚本执行状态')
    start_time = dbModel.DateTimeField('开启时间')
    method_type = dbModel.StringField('通道类型', is_index=True)
    update_balance_amount_time = dbModel.DateTimeField('余额更新时间')
    update_newbalance_amount_time = dbModel.DateTimeField('余额更新有变动时间')
    is_otp_login = dbModel.BooleanField('OTP登录')
    is_sms_login = dbModel.BooleanField('SMS登录')
    login_lock = dbModel.BooleanField('登录锁定')
    is_abnormal = dbModel.BooleanField('是否异常')
    auto_removal_time = dbModel.IntegerField('自动下架检测时间范围')
    turn_auto_removal_time = dbModel.DateTimeField('开启自动下架功能时间')

    @classmethod
    def field_search(cls):
        return [
            'statu', 'bank_uid', 'account', 'account_username', 'note','create_time', 'bankcard_type', 'is_otp_login', 'is_sms_login', 'login_lock', 'is_abnormal'
        ]


# 银行卡账单
class BankCardBillTable(dbModel):
    '''
    银行卡账单
    '''
    __tablename__ = 'bankcard_bill_table'
    bankacrd_uuid = dbModel.StringField('银行卡UUID', is_index=True)
    bankacrd_account = dbModel.StringField('银行卡号', is_index=True)
    bill_type = dbModel.StringField('账单类型', is_index=True)
    amount = dbModel.IntegerField('金额', is_index=True)
    note = dbModel.StringField('备注')
    agentadmin_uuid = dbModel.StringField('agentadmin_uuid', is_index=True)
    bill_time = dbModel.DateTimeField('账单时间')
    bank_bill_id = dbModel.StringField('原订单ID',is_index=True)
    description = dbModel.StringField('原订单备注', is_index=True)
    unusual_type = dbModel.StringField('异常类型', is_index=True)
    @classmethod
    def field_search(cls):
        return [
            'bankacrd_uid',
            'bill_type',
            'amount',
            'bill_time',
            'agentadmin_uuid',
            'description',
            'bank_bill_id',
        ]



class CollectionOrderTable(dbModel):
    '''
    代收订单
    '''
    __tablename__ = 'collection_order_table'
    merchant_id = dbModel.StringField('商户id', is_index=True)
    order_id = dbModel.StringField('订单号', is_index=True)
    merchant_order_id = dbModel.StringField('商户订单号', is_index=True)
    bankcard_id = dbModel.StringField('收款银行卡', is_index=True)
    payee_bankcard = dbModel.StringField('收款银行卡', is_index=True)
    payee_username = dbModel.StringField('收款人姓名', is_index=True)
    bank_code = dbModel.StringField('银行code', is_index=True)
    repay_amount = dbModel.FloatField('手续费')
    order_amount = dbModel.IntegerField('订单金额', is_index=True)
    actual_amount = dbModel.IntegerField('实际支付金额', is_index=True)
    order_time = dbModel.DateTimeField('订单时间', nullable=False)
    pay_statu = dbModel.BooleanField('支付状态', is_index=True)
    proc_statu = dbModel.BooleanField('处理状态', is_index=True)
    callback_statu = dbModel.StringField('回调状态', is_index=True)
    callback_time = dbModel.DateTimeField('回调时间')
    callback_url = dbModel.StringField('回调地址', is_index=True)
    callbank_type = dbModel.StringField('回调类型', is_index=True)
    back_url = dbModel.StringField('跳转Url', is_index=True)
    bank_account_name = dbModel.StringField('付款人姓名', is_index=True)
    bank_memo = dbModel.StringField('附言', is_index=True)
    pay_time = dbModel.DateTimeField('支付时间')
    pay_method = dbModel.StringField('支付模式', is_index=True)
    force_ispay = dbModel.BooleanField('强制入款')
    ip = dbModel.StringField('IP')
    is_lose = dbModel.BooleanField('掉单')
    lose_reason = dbModel.StringField('掉单原因')
    lose_note = dbModel.StringField('掉单备注')
    success_seconds = dbModel.IntegerField('成功用时/S')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    note = dbModel.StringField('备注')
    payqrcode_url = dbModel.StringField('支付码')
    proc_time = dbModel.DateTimeField('处理时间')

    @classmethod
    def field_search(cls):
        return [
            'pay_statu',
            'callback_statu',
            'order_id',
            'merchant_order_id',
            'pay_method',
            'bank_memo',
            'create_time',
            'order_time',
            'pay_time',
            'merchant_id',
            'order_amount',
            'actual_amount',
            'callbank_type',
            'payee_bankcard',
            'callback_time',
            'note',
        ]



class SystemLogTable(dbModel):
    '''
    系统日志
    '''
    __tablename__ = 'system_log_table'
    user_id = dbModel.StringField('操作人')
    ip = dbModel.StringField('IP')
    log_type = dbModel.StringField('操作类型')
    os = dbModel.StringField('设备系统')
    cpu = dbModel.StringField('设备CPU')
    browser = dbModel.StringField('Browser')
    note = dbModel.StringField('备注')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)



class TunnelTable(dbModel):
    '''
    支付通道
    '''
    __tablename__ = 'tunnel_table'
    tunnel_name = dbModel.StringField('通道名称')
    code = dbModel.StringField('编码')
    tunnel_statu = dbModel.BooleanField('通道状态')



class callbackLogTable(dbModel):
    '''
    回调记录
    '''
    __tablename__ = 'callback_log_table'
    order_uuid = dbModel.StringField('订单uuid', is_index=True)
    order_id = dbModel.StringField('订单order_id', is_index=True)
    merchant_uuid = dbModel.StringField('商户uuid', is_index=True)
    request_text = dbModel.StringField('请求内容')
    affidavit_text = dbModel.StringField('加签原文')
    callback_url = dbModel.StringField('回调地址')
    response_code = dbModel.IntegerField('响应code')
    response_text = dbModel.StringField('响应内容')
    statu = dbModel.BooleanField('状态')
    note = dbModel.StringField('备注')
    callbank_type = dbModel.StringField('回调类型')
    admin_uuid = dbModel.StringField('手动回调操作人')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    @classmethod
    def field_search(cls):
        return [
            'order_uuid',
            'statu',
            'create_time',
            'order_id'
        ]



class RechargeMoneyTable(dbModel):
    '''
    充值记录
    '''
    __tablename__ = 'recharge_money_table'
    operate_user_uuid = dbModel.StringField('操作人员UUID')
    merchant_id = dbModel.StringField('商户id', is_index=True)
    amount = dbModel.FloatField('金额')
    actual_amount = dbModel.FloatField('实际充值金额')
    repay_amount = dbModel.FloatField('手续费')
    note = dbModel.StringField('备注')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'create_time',
            'merchant_id',
            'note'
        ]

class ReduceMoneyTable(dbModel):
    '''
    充值记录
    '''
    __tablename__ = 'reduce_money_table'
    operate_user_uuid = dbModel.StringField('操作人员UUID')
    merchant_id = dbModel.StringField('商户id', is_index=True)
    amount = dbModel.FloatField('金额')
    note = dbModel.StringField('备注')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'create_time',
            'merchant_id',
            'note'
        ]



class BankAccountCacheTable(dbModel):
    '''
    银行脚本信息缓存
    '''
    __tablename__ = 'bank_account_cache_table'
    username = dbModel.StringField('银行卡用户名', is_index=True)
    account = dbModel.StringField('银行卡账户', is_index=True)
    token = dbModel.StringField('TOKEN')
    bank_code = dbModel.StringField('银行编码', is_index=True)
    req_data = {}



class WithdrawTable(dbModel):
    '''
    提现申请
    '''
    __tablename__ = 'withdraw_table'
    merchant_uuid = dbModel.StringField('商户uuId', is_index=True)
    amount = dbModel.IntegerField('金额')
    actual_amount = dbModel.FloatField('实际金额')
    repay_amount = dbModel.FloatField('手续费')
    statu = dbModel.StringField('申请状态')
    bankcard_uuid = dbModel.StringField('银行卡UUID')
    admin_uuid = dbModel.StringField('处理人')
    dealwith_time = dbModel.DateTimeField('处理时间')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    payee_bank = dbModel.StringField('收款银行', is_index=True)
    payee_bankcard = dbModel.StringField('收款银行卡', is_index=True)
    payee_username = dbModel.StringField('收款人姓名', is_index=True)
    payqrcode_url = dbModel.StringField('支付码')
    @classmethod
    def field_search(cls):
        return [
            'amount',
            'statu',
            'create_time',
            'payee_bank',
            'payee_bankcard',
            'payee_username',
        ]



# 银行脚本执行日志
class BankScriptLogTable(dbModel):
    '''
    银行脚本执行日志
    '''
    __tablename__ = 'bank_script_log_table'
    bankcrad_uid = dbModel.StringField('银行卡UUID', is_index=True)
    bankcrad_account = dbModel.StringField('银行卡-卡号')
    log_text = dbModel.StringField('日志TEXT')
    is_manual = dbModel.BooleanField('手动')



class unknownIncomeTable(dbModel):
    '''
    不明收入
    '''
    __tablename__ = 'unknown_income_table'
    receive_bankacrd_account = dbModel.StringField('收款银行卡号', is_index=True)
    state = dbModel.BooleanField('处理状态')
    amount = dbModel.IntegerField('金额')
    order_note = dbModel.StringField('订单备注')
    note = dbModel.StringField('备注')
    admin_uid = dbModel.StringField('操作人', is_index=True)
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    bank_bill_id = dbModel.StringField('原订单ID',is_index=True)
    proc_time = dbModel.DateTimeField('处理时间')

    @classmethod
    def field_search(cls):
        return [
            'receive_bankacrd_account',
            'state',
            'order_note',
            'note',
            'amount',
            'bank_bill_id',
            # 'receive_time',
        ]



class VpnTable(dbModel):
    '''
    VPN配置
    '''
    __tablename__ = 'vpn_table'
    name = dbModel.StringField('名称', is_index=True)
    statu = dbModel.BooleanField('状态')
    internet_speed = dbModel.StringField('网速')
    note = dbModel.StringField('备注')
    vpn_url = dbModel.StringField('vpn_url')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'name',
            'vpn_url',
            'statu',
        ]



class messageWarnTable(dbModel):
    '''
    消息提示
    '''
    __tablename__ = 'message_warn_table'
    title = dbModel.StringField('标题')
    text = dbModel.StringField('内容')
    statu = dbModel.BooleanField('提示状态')



# 订单绑定银行卡记录
class order_bankcard_bind_table(dbModel):
    __tablename__ = 'order_bankcard_bind_table'
    order_id = dbModel.StringField('订单号', is_index=True)
    merchant_order_id = dbModel.StringField('商户订单号', is_index=True)
    payee_bankcard = dbModel.StringField('收款银行卡', is_index=True)



# API请求日志
class ApiRequestLogTable(dbModel):
    __tablename__ = 'api_request_log_table'
    ip = dbModel.StringField('IP', is_index=True)
    request_method = dbModel.StringField('请求模式', is_index=True)
    request_data = dbModel.StringField('请求内容')
    response_code = dbModel.IntegerField('响应状态', is_index=True)
    response_text = dbModel.StringField('响应内容')
    url_path = dbModel.StringField('请求路径', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'ip',
            'request_method',
            'request_data',
            'response_code',
            'response_text',
            'url_path',
            'create_time',
        ]


# 支付二维码创建日志
class payQrcodeLogTable(dbModel):
    __tablename__ = 'pay_payqrcode_log_table'
    order_uuid = dbModel.StringField('订单UUID')
    

# 脚本日志
class ScriptLogTable(dbModel):
    __tablename__ = 'script_log_table'
    note = dbModel.StringField('备注')
