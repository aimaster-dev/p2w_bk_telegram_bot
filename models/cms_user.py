# -*- coding: utf-8 -*-
from . import dbModel
from werkzeug.security import generate_password_hash, check_password_hash
from constants import PERMISSION_ALL, ROlE_ALL


class CmsUserTable(dbModel):
    """CMS-管理员表"""
    __tablename__ = 'cms_user_table'
    id = dbModel.IDField()
    username = dbModel.StringField('姓名', nullable=False, is_index=True)
    account = dbModel.StringField('登录账户名', nullable=False)
    password = dbModel.PasswordField('密码',nullable=False)
    zalo = dbModel.StringField('zalo')
    telephone = dbModel.StringField('电话')
    email = dbModel.StringField('邮箱')
    portrait = dbModel.StringField('头像')
    statu = dbModel.BooleanField('状态', default=True, nullable=False, true_text='正常', false_text='禁用')
    current_login = dbModel.DateTimeField('最后登录时间')
    current_login_ip = dbModel.StringField('最后登录IP')
    last_login_time = dbModel.DateTimeField('上次登录时间')
    last_login_ip = dbModel.StringField(u'上次登录IP')
    intro = dbModel.StringField('介绍')
    note = dbModel.StringField('备注')
    role_code = dbModel.StringField('角色')
    is_activate = dbModel.BooleanField('激活状态')
    permissions = []
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

    language = dbModel.StringField('language')
    cms_ip_whitelist = dbModel.StringField('后台ip白名单')
    login_google_verify_statu = dbModel.BooleanField('谷歌登录验证开关')
    is_syscard = dbModel.BooleanField('是否使用系统银行卡')
    is_addcard = dbModel.BooleanField('是否使用系统银行卡')
    is_clear_deposit = dbModel.BooleanField('是否使用系统银行卡')
    is_clear_withdraw = dbModel.BooleanField('是否使用系统银行卡')
    is_clear_transit = dbModel.BooleanField('是否使用系统银行卡')
    is_test_withdraw_card = dbModel.BooleanField('是否测试出款卡')
    is_clear_log = dbModel.BooleanField('是否使用系统银行卡')
    is_clear_other = dbModel.BooleanField('是否使用系统银行卡')
    balance_amount = dbModel.FloatField('可用余额')
    in_vnbankqr_rate = dbModel.FloatField('入款-银行扫码费率')
    issued_money_rate = dbModel.FloatField('下发默认利率')
    recharge_money_rate = dbModel.FloatField('内充默认利率')
    paybehalf_rate = dbModel.FloatField('代付默认利率')
    is_online = dbModel.BooleanField('在线')
    outm_max_money = dbModel.IntegerField('出款最大值')
    outm_min_money = dbModel.IntegerField('出款最小值')
    bankcard_info = dbModel.StringField('出款银行卡信息')
    system_paybehalf = dbModel.BooleanField('是否使用系统代付')
    maintain_bankcodes = dbModel.StringField('代付银行维护设置')
    maintain_switch = dbModel.BooleanField('代付功能开关')
    withdrawalcard_uuid = dbModel.StringField('代付功能开关')
    last_not = dbModel.StringField('代付功能开关')

    @classmethod
    def field_sort(cls):
        return ['id', 'telephone', 'account', 'email', 'statu', 'create_time', 'note']
    @classmethod
    def field_search(cls):
        return ['statu', 'username', 'account', 'note', 'create_time', 'role_code','withdrawalcard_uuid', 'is_online']
    @classmethod
    def add_field_sort(cls):
        return ['username', 'account', 'password', 'zalo', 'email', 'note']
    @classmethod
    def edit_field_sort(cls):
        return ['username', 'account', 'email', 'zalo', 'note']

    @property
    def is_superadmin(self):
        if self.permissions == ['superadmin']:
            return True
        return

    @property
    def is_administrator(self):
        if self.role_code == ROlE_ALL.ADMINISTRATOR:
            return True
        return

    def has_permission(self, *args):
        if self.is_superadmin:
            return True
        for p in args:
            if p and p in self.permissions:
                return True
        return False

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


