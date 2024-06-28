from . import dbModel



# 代付订单
class behalfPayOrderTable(dbModel):
    __tablename__ = 'behalfpay_order_table'
    order_id = dbModel.StringField('订单号', is_index=True)
    merchant_id = dbModel.StringField('商户id', is_index=True)
    merchant_order_id = dbModel.StringField('商户订单号', is_index=True)
    receive_bank_uuid = dbModel.StringField('收款银行', is_index=True)
    receive_bank_code = dbModel.StringField('收款银行Code', is_index=True)
    receive_account = dbModel.StringField('收款银行卡号', is_index=True)
    receive_owner = dbModel.StringField('收款人', is_index=True)
    pay_bankacrd_uuid = dbModel.StringField('支付银行卡', is_index=True)

    repay_amount = dbModel.FloatField('手续费')
    order_amount = dbModel.IntegerField('订单金额', is_index=True)
    actual_amount = dbModel.IntegerField('实际支付金额', is_index=True)
    order_time = dbModel.DateTimeField('订单时间', nullable=False)
    pay_statu = dbModel.BooleanField('支付状态', is_index=True)
    reject_pay = dbModel.BooleanField('拒绝支付', is_index=True)
    callback_statu = dbModel.StringField('回调状态', is_index=True)
    callback_time = dbModel.DateTimeField('回调时间')
    callback_url = dbModel.StringField('回调地址', is_index=True)
    callbank_type = dbModel.StringField('回调类型', is_index=True)
    pay_time = dbModel.DateTimeField('支付时间')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    ip = dbModel.StringField('IP')
    bank_memo = dbModel.StringField('附言', is_index=True)
    force_ispay = dbModel.BooleanField('强制支付')
    processor_uid = dbModel.StringField('处理人', is_index=True)
    out_money_userid = dbModel.StringField('出款人', is_index=True)
    is_task = dbModel.BooleanField('是否添加任务')
    script_id = dbModel.StringField('脚本Id', is_index=True)
    payqrcode_url = dbModel.StringField('支付码')
    check_aname_state = dbModel.StringField('账户姓名检测状态')
    sys_payorder = dbModel.BooleanField('是否是系统订单')
    is_read = dbModel.BooleanField('已读')

    @classmethod
    def field_search(cls):
        return [
            'order_id',
            'merchant_id',
            'merchant_order_id',
            'receive_bank_code',
            'receive_account',
            'receive_owner',
            'order_amount',
            'order_time',
            'callback_statu',
            'callbank_type',
            'pay_time',
            'bank_memo',
            'pay_statu',
            'processor_uid',
            'reject_pay',
            'out_money_userid',
            'callback_time',
            'check_aname_state',
        ]



class behalfPayCallbackLogTable(dbModel):
    '''
    代付订单回调记录
    '''
    __tablename__ = 'behalfpay_callback_log_table'
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



# 代付任务
class behalfPayTaskTable(dbModel):
    __tablename__ = 'behalfpay_task_table'
    statu = dbModel.StringField('任务状态')
    order_id = dbModel.StringField('订单ID', is_index=True)
    end_time = dbModel.DateTimeField('任务结束时间')
    note = dbModel.StringField('备注')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)
    script_id = dbModel.StringField('脚本ID')

    @classmethod
    def field_search(cls):
        return [
            'statu',
            'order_id',
            'end_time',
            'note',
        ]



# 脚本
class behalfPayScriptTable(dbModel):
    __tablename__ = 'behalfpay_script_table'
    name = dbModel.StringField('脚本名称')
    secret_key = dbModel.StringField('密钥')
    ips = dbModel.StringField('IP白名单')
    note = dbModel.StringField('备注')
    statu = dbModel.BooleanField('状态')
    desktop_id = dbModel.StringField('桌面编号', is_index=True)
    device_id = dbModel.StringField('设备Id', is_index=True)
    balance_amount = dbModel.FloatField('余额')
    bankowner = dbModel.StringField('银行卡人姓名')
    bankcard_account = dbModel.StringField('银行卡号')
    max_amount = dbModel.IntegerField('最大金额')
    min_amount = dbModel.IntegerField('最小金额')

    @classmethod
    def field_search(cls):
        return [
            'name',
            'statu',
            'desktop_id',
            'device_id',
            'bankcard_account',
        ]



# 脚本日志
class behalfPayScriptLogTable(dbModel):
    __tablename__ = 'behalfpay_script_log_table'
    script_id = dbModel.StringField('脚本ID')
    request_cont = dbModel.StringField('请求内容')
    response_cont = dbModel.StringField('响应')
    ip = dbModel.StringField('请求IP')



# 出款信息记录
class behalfPayBankcardLogTable(dbModel):
    __tablename__ = 'behalfpay_bankcard_log_table'
    user_uuid = dbModel.StringField('出款人员', is_index=True)
    bankcard_info = dbModel.StringField('银行卡信息')



# 订单流程
class behalfPayOrderProcessTable(dbModel):
    __tablename__ = 'behalfpay_order_process_table'
    order_id = dbModel.StringField('订单号', is_index=True)
    text = dbModel.StringField('文本')



# 姓名检测银行卡
class CnBankCardTable(dbModel):
    __tablename__ = 'cn_bankcard_table'
    name = dbModel.StringField('名称', is_index=True)
    username = dbModel.StringField('银行卡用户名', is_index=True)
    password = dbModel.StringField('银行卡密码', is_index=True)
    account = dbModel.StringField('银行卡账户', is_index=True)
    account_username = dbModel.StringField('账户人姓名', is_index=True)
    bank_uid = dbModel.StringField('银行', is_index=True)
    statu = dbModel.BooleanField('状态', is_index=True)
    note = dbModel.StringField('备注')
    create_time = dbModel.DateTimeField('时间', nullable=False)
    vpn_uuid = dbModel.StringField('VPN UUID')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

    @classmethod
    def field_search(cls):
        return [
            'name',
            'username',
            'account',
            'account_username',
            'bank_uid',
            'statu',
        ]




