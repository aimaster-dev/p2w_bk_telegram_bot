# -*- coding: utf-8 -*-
from . import dbModel


class SiteConfigTable(dbModel):
    """网站配置"""
    __tablename__ = 'site_config_table'
    project_name = dbModel.StringField('项目名', nullable=False)
    secret_key = dbModel.StringField('项目秘钥', nullable=False)
    cms_prefix = dbModel.StringField('CMS登录目录', nullable=False)
    max_filesize = dbModel.IntegerField('项目最大文件限制/KB')
    cms_text = dbModel.StringField('后台名称')
    cms_icon = dbModel.StringField('后台ICON图标')
    front_domain = dbModel.StringField('网站前端域名', nullable=False)
    cms_domain = dbModel.StringField('网站后台域名', nullable=False)

    # 网站功能
    site_statu = dbModel.BooleanField('网站状态', default=0, true_text='已开启', false_text='已关闭')
    cms_captcha = dbModel.BooleanField('CMS登录图片验证码', default=0, true_text='已开启', false_text='已关闭')
    cms_log_save_time = dbModel.IntegerField('CMS操作日志保存时间/天')
    front_log_save_time = dbModel.IntegerField('前端日志保存时间/天')
    site_domain = dbModel.StringField('网站域名')

    cms_ip_whitelist = dbModel.StringField('后台ip白名单')
    login_google_verify_statu = dbModel.BooleanField('谷歌登录验证开关')
    bank_collect_api_reqcount = dbModel.IntegerField('银行收款脚本单词获取条数')
    bank_collect_api_sleep = dbModel.IntegerField('银行收款脚本单词获取条数')
    maintain_bankcodes = dbModel.StringField('代付银行维护设置')
    maintain_switch = dbModel.BooleanField('代付功能开关')
    automatic_maintain_switch = dbModel.BooleanField('自动代付功能总开关')
    check_aname_switch = dbModel.BooleanField('代付检测姓名功能开关')



class SystemLogTable(dbModel):
    '''
    系统日志
    '''
    __tablename__ = 'system_log_table'
    user_uuid = dbModel.StringField('用户uuid', is_index=True)
    state_code = dbModel.IntegerField('状态码')
    ip = dbModel.StringField('请求IP')
    url_path = dbModel.StringField('请求路径')
    note = dbModel.StringField('备注')
    method = dbModel.StringField('请求方式')
    agentadmin_uuid = dbModel.StringField('代理ID', is_index=True)

