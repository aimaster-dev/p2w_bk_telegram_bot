from .cms_base import CmsTableViewBase
from models.cms_user import CmsUserTable
from constants import ROlE_ALL, PERMISSION_ALL, BILL_STATEMEN_TYPES
from modules.google_module.google_verify import GooleVerifyCls
from models.pay_table import AgentadminBillLogTable
from flask import request
from models.behalfPay import behalfPayBankcardLogTable
from common_utils.utils_funcs import update_language

class UserListView(CmsTableViewBase):
    add_url_rules = [['/userList', 'userList']]
    title = '账户管理'
    per_page = 30
    sort = [['create_time', -1]]
    MCLS = CmsUserTable
    template = 'cms/userManage/userList.html'

    def get_filter_dict(self):
        fff = {}
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            fff['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            fff['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        role_code = request.args.get('role_code')
        if role_code:
            fff['role_code'] = role_code
        is_online = request.args.get('is_online')
        if is_online:
            if is_online == '1':
                fff['is_online'] = True
            elif is_online == '0':
                fff['is_online'] = False
        return fff

    def user_data_html(self, data_dict={}):
        _action = 'add_user_data'
        if data_dict:
            _action = 'edit_user_data'

        reco_html = ''
        for reco in ROlE_ALL.name_arr[1:]:
            reco_html += f'<option value="{reco}">{ROlE_ALL.name_dict.get(reco)}</option>'

        bddl_html = ''
        for uda in CmsUserTable.find_many({'role_code': ROlE_ALL.AGENTADMIN}):
            bddl_html += f'<option value="{uda.get("uuid")}">{uda.get("account")}-{uda.get("username")}</option>'

        role_html = ''
        select_dl_html = ''
        if not data_dict and ( self.current_admin_user.is_superadmin or self.current_admin_user.is_administrator ):
            role_html += f'''
                <div class="list-group-item">
                    <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">用户角色：</span>
                    <select class="form-control" id="role_code" onchange="select_role()" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                        <option value="">选择用户角色</option>
                        {reco_html}
                    </select>
                </div>                   
            '''
            select_dl_html += f'''
                <div class="list-group-item" style="display: none;">
                    <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">选择绑定代理：</span>
                    <select class="form-control" id="agentadmin_uuid" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                        <option value="">选择绑定代理</option>
                        {bddl_html}
                    </select>
                </div>                   
            '''
        if not data_dict and self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            role_html += f'''
                <div class="list-group-item">
                    <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">用户角色：</span>
                    <select class="form-control" id="role_code" onchange="select_role()" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                        <option value="">选择用户角色</option>
                        <option value="{ROlE_ALL.SYSTEMUSER}">{ROlE_ALL.name_dict.get(ROlE_ALL.SYSTEMUSER)}</option>
                        <option value="{ROlE_ALL.OUT_MONEY_USER}">{ROlE_ALL.name_dict.get(ROlE_ALL.OUT_MONEY_USER)}</option>
                    </select>
                </div>                   
            '''

        outm_html = ''
        if data_dict:
            if data_dict.get('role_code') in [ROlE_ALL.OUT_MONEY_USER, ROlE_ALL.SYS_OUT_MONEY_USER]:
                outm_html += f'''
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款最小值：</span>
                        <input type="number" class="form-control" id="outm_min_money" value="{ data_dict.get('outm_min_money') or '' }" placeholder="出款最小值，包含输入值" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>                  
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款最大值：</span>
                        <input type="number" class="form-control" id="outm_max_money" value="{ data_dict.get('outm_max_money') or '' }" placeholder="出款最大值，包含输入值" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>                                      
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款银行卡信息：</span>
                        <input type="text" class="form-control" id="bankcard_info" value="{ data_dict.get('bankcard_info') or '' }" placeholder="出款银行卡信息" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>                                      
                '''
        else:
            outm_html += f'''
                <div class="list-group-item" style="display:none">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款最小值：</span>
                    <input type="number" class="form-control" id="outm_min_money" value="{data_dict.get('outm_min_money') or ''}" placeholder="出款最小值，包含输入值" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item" style="display:none">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款最大值：</span>
                    <input type="number" class="form-control" id="outm_max_money" value="{data_dict.get('outm_max_money') or ''}" placeholder="出款最大值，包含输入值" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item" style="display:none">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款银行卡信息：</span>
                    <input type="text" class="form-control" id="bankcard_info" value="{data_dict.get('bankcard_info') or ''}" placeholder="出款最大值" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>                                      
            '''
        permithtml = ''
        permit_payer_html = ''
        if self.current_admin_dict.get("role_code") == ROlE_ALL.SUPERADMIN or self.current_admin_dict.get("role_code") == ROlE_ALL.AGENTADMIN:
            if data_dict.get('role_code') == ROlE_ALL.SYSTEMUSER or data_dict.get('role_code')==ROlE_ALL.ADMINISTRATOR:
                permithtml += f'''
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否添加银行卡：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_addcard') else '0' }" id="is_addcard">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_addcard') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>                  
                '''
            if data_dict.get('role_code') in [ROlE_ALL.SUPERADMIN, ROlE_ALL.AGENTADMIN, ROlE_ALL.ADMINISTRATOR, ROlE_ALL.SYSTEMUSER]:
                permithtml +=f'''
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否入款卡清零：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_clear_deposit') else '0' }" id="is_clear_deposit">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_clear_deposit') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>                  
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否出款卡清零：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_clear_withdraw') else '0' }" id="is_clear_withdraw">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_clear_withdraw') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>                  
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否中转卡清零：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_clear_transit') else '0' }" id="is_clear_transit">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_clear_transit') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>                  
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否其他卡清零：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_clear_other') else '0' }" id="is_clear_other">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_clear_other') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>   
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否交易日志清零：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_clear_log') else '0' }" id="is_clear_log">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_clear_log') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>                  
                '''

            if data_dict.get('role_code') in [ROlE_ALL.OUT_MONEY_USER, ROlE_ALL.SYS_OUT_MONEY_USER]:
                permit_payer_html +=f'''
                <div class="list-group-item" style="display:flex;align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否测试出款卡：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_test_withdraw_card') else '0' }" id="is_test_withdraw_card">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_test_withdraw_card') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>                             
                '''

        is_show = False
        config_html_statu = False
        if self.current_admin_user.is_superadmin or self.current_admin_user.is_administrator:
            if data_dict:
                if data_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                    config_html_statu = True
                    is_show = True
            else:
                config_html_statu = True

        config_html = ''
        if config_html_statu:
            config_html += f'''
                <div class="list-group-item" style="display: { 'flex' if is_show else 'none' };align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否使用系统银行卡：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('is_syscard') else '0' }" id="is_syscard">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('is_syscard') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>     
                <div class="list-group-item" style="display: { 'flex' if is_show else 'none' };align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">是否使用系统代付：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('system_paybehalf') else '0' }" id="system_paybehalf">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('system_paybehalf') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>     
                <div class="list-group-item" style="display: { 'flex' if is_show else 'none' };align-items: center; justify-content:center; margin-top: 0;margin-bottom: 0; padding-top: 0;padding-bottom: 0;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">登录谷歌验证开关：</span>
                    <input type="hidden" alt="" aria-label="" value="{ '1' if data_dict.get('login_google_verify_statu') else '0' }" id="login_google_verify_statu">
                    <div style="display: inline-block; width: calc(100% - 250px); text-align: left;">
                        <i class="iconfont { 'icon-kaiguan4' if data_dict.get('login_google_verify_statu') else 'icon-kaiguanguan' } pointer" style="font-size: 40px;" onclick="switch_func($(this))"></i>                        
                    </div>
                </div>     
                <div class="list-group-item" style="display: { 'flex' if is_show else 'none' };align-items: center;justify-content: center;">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">登录IP白名单：</span>
                    <textarea rows="5" class="form-control" id="cms_ip_whitelist" placeholder="登录IP白名单，一行一个" aria-label="" style="display: inline-block; width: calc(100% - 250px)">{data_dict.get('cms_ip_whitelist') or ''}</textarea>
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">代付费率%：</span>
                    <input type="text" class="form-control" id="paybehalf_rate" value="{ data_dict.get('paybehalf_rate')*100 if data_dict.get('paybehalf_rate') else '' }" placeholder="代付费率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">下发默认利率%：</span>
                    <input type="text" class="form-control" id="issued_money_rate" value="{ data_dict.get('issued_money_rate')*100 if data_dict.get('issued_money_rate') else '' }" placeholder="下发默认利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">内充利率%：</span>
                    <input type="text" class="form-control" id="recharge_money_rate" value="{ data_dict.get('recharge_money_rate')*100 if data_dict.get('recharge_money_rate') else '' }" placeholder="内充利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>

                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">越南网银扫码 利率%：</span>
                    <input type="text" class="form-control" id="in_vnbankqr_rate" value="{ round(data_dict.get('in_vnbankqr_rate')*100,2) if data_dict.get('in_vnbankqr_rate') else '' }" placeholder="VNBANKQR 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">越南ZALO pay 利率%：</span>
                    <input type="text" class="form-control" id="in_vnzalo_rate" value="{ round(data_dict.get('in_vnzalo_rate')*100,2) if data_dict.get('in_vnzalo_rate') else '' }" placeholder="VNZALO 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">越南MOMO pay 利率%：</span>
                    <input type="text" class="form-control" id="in_vnmomo_rate" value="{ round(data_dict.get('in_vnmomo_rate')*100,2) if data_dict.get('in_vnmomo_rate') else '' }" placeholder="VNMOMO 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">越南ViettelPay 利率%：</span>
                    <input type="text" class="form-control" id="in_vnvtpay_rate" value="{ round(data_dict.get('in_vnvtpay_rate')*100,2) if data_dict.get('in_vnvtpay_rate') else '' }" placeholder="VNVTPAY 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">世界付支付(网银扫码)自定义 利率%：</span>
                    <input type="text" class="form-control" id="in_vnbankqr2_rate" value="{ round(data_dict.get('in_vnbankqr2_rate')*100,2) if data_dict.get('in_vnbankqr2_rate') else '' }" placeholder="VNBANKQR2 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">世界付支付(momopay)自定义 利率%：</span>
                    <input type="text" class="form-control" id="in_vnmo2mo_rate" value="{ round(data_dict.get('in_vnmo2mo_rate')*100,2) if data_dict.get('in_vnmo2mo_rate') else '' }" placeholder="VNMO2MO 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">世界付支付(zalopay)自定义 利率%：</span>
                    <input type="text" class="form-control" id="in_vnza2lo_rate" value="{ round(data_dict.get('in_vnza2lo_rate')*100,2) if data_dict.get('in_vnza2lo_rate') else '' }" placeholder="VNZA2LO 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
                <div class="list-group-item">
                    <span style="width: 240px; text-align: right; display: inline-block; position: relative;">世界付支付(viettelpay)自定义 利率%：</span>
                    <input type="text" class="form-control" id="in_vnvt2pay_rate" value="{ round(data_dict.get('in_vnvt2pay_rate')*100,2) if data_dict.get('in_vnvt2pay_rate') else '' }" placeholder="VNVT2PAY 利率" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                </div>
            '''

        html = f'''
            <div class="addUserBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto;">
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">姓名：</span>
                        <input type="text" class="form-control" id="username" value="{ data_dict.get('username') or '' }" placeholder="姓名" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">账户：</span>
                        <input type="text" class="form-control" id="account" value="{ data_dict.get('account') or '' }" placeholder="账户" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>
                    <div class="list-group-item">
                        <span { '' if data_dict else 'class="loglable"' } style="width: 240px; text-align: right; display: inline-block; position: relative;">密码：</span>
                        <input type="text" class="form-control" id="password" placeholder="密码" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>
                    <div class="list-group-item">
                        <span { '' if data_dict else 'class="loglable"' } style="width: 240px; text-align: right; display: inline-block; position: relative;">确认密码：</span>
                        <input type="text" class="form-control" id="confirm_password" placeholder="密码" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>
                    { role_html }
                    { select_dl_html }
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">电话：</span>
                        <input type="text" class="form-control" id="telephone" value="{ data_dict.get('telephone') or '' }" placeholder="电话" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>           
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">备注：</span>
                        <input type="text" class="form-control" id="note" value="{ data_dict.get('note') or '' }" placeholder="备注" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>  
                    {permithtml}             
                    { outm_html }                            
                    { config_html }       
                    { permit_payer_html}          
                </div>

                <div class="blank" style="background: #eeeeee; height: 1px; margin: 15px 0;"></div>

                <div style="position: relative; text-align: center">
                    <span class="btn btn-primary" onclick="post_user_data('{_action}', '{ data_dict.get('uuid') if data_dict else '' }')">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>
        '''
        return html
    
    def jmoney_html(self):
        html = f'''
            <div class="formBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto;">
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">输入扣除金额：</span>
                        <input type="number" class="form-control" id="jmoney" value="" placeholder="输入扣除金额" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>                                               
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">备注：</span>
                        <input type="text" class="form-control" id="note" value="" placeholder="备注" aria-label="" style="display: inline-block; width: calc(100% - 250px)" onchange="monitorRechargeMoney()">
                    </div>
                </div>

                <div class="blank" style="background: #eeeeee; height: 1px; margin: 15px 0;"></div>

                <div style="position: relative; text-align: center">
                    <span class="btn btn-primary" onclick="post_kc_money('{self.data_dict.get("uuid")}')">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>        
        '''
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))

    def detailsInfo_html(self, uid):
        html = ''
        html += f'''
            <div class="formBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto; text-align: left; overflow-x: hidden; box-sizing: border-box;">               
                    <ul class="layui-timeline">
                    
        '''
        datas = behalfPayBankcardLogTable.find_many({'user_uuid': uid}, sort=[['create_time', -1]])
        if not datas:
            html += f'''
                        <li class="layui-timeline-item">
                            <i class="layui-icon layui-timeline-axis"></i>
                            <div class="layui-timeline-content layui-text">
                                <div class="layui-timeline-title">暂无数据</div>
                            </div>
                        </li>            
            '''            
        else:
            for data in datas:
                html += f'''
                            <li class="layui-timeline-item">
                                <i class="layui-icon layui-timeline-axis"></i>
                                <div class="layui-timeline-content layui-text">
                                    <div class="layui-timeline-title">{self.format_time_func(data.get('create_time'))}，{ data.get('bankcard_info') or '' }</div>
                                </div>
                            </li>            
                '''

        html += '''
                    </ul>        
                </div>
            </div>        
        '''
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))

    def dealwith_main_context(self):
        all_datas = self.context.get('all_datas') or []
        datas = []
        ddd = {}
        online_cnt = 0
        for data in all_datas:
            agentadmin_uuid = data.get('agentadmin_uuid') or ''
            if agentadmin_uuid:
                dss = ddd.get(agentadmin_uuid) or {}
                if not dss:
                    dss = CmsUserTable.find_one({'uuid': agentadmin_uuid}) or {}
                    ddd.update({agentadmin_uuid: dss})
                data['agentadmin_data'] = dss
            datas.append(data)
            if data.get("is_online") == True:
                if self.current_admin_dict.get("role_code") == ROlE_ALL.SUPERADMIN:
                    if data.get("role_code") == ROlE_ALL.SYS_OUT_MONEY_USER:
                        online_cnt += 1
                else:
                    online_cnt += 1
        self.context['all_datas'] = datas
        self.context['online_cnt'] = online_cnt
        self.context['req_host'] = str(request.host_url).strip('/')

    def get_context(self):
        return {
            'ROlE_ALL': ROlE_ALL,
        }

    def get_permission(self, user_cls):
        html = '<div id="permission_div">'
        html += '<table class="table table-bordered table-hover text-center">'
        html += '<thead class="thead-light"><tr>'
        html += '<th width="130">菜单名</th>'
        html += '<th>拥有权重</th>'
        html += '</tr></thead>'
        html += '<tbody>'
        for k, v in PERMISSION_ALL.name_dict.items():
            if k == 'ROOT':
                continue
            if user_cls.role_code == ROlE_ALL.OUT_MONEY_USER and PERMISSION_ALL.adminUserManage in v:
                continue
            html += '<tr>'
            html += '<td>%s</td>' % k
            html += '<td align="left">'
            for per, ptext in v.items():
                if not self.current_admin_user.is_superadmin and not self.current_admin_user.is_administrator:
                    if per not in PERMISSION_ALL.name_arr:
                        continue
                    if 'CnBankCard' in per:
                        continue
                if self.data_dict.get('permissions') and per in self.data_dict.get('permissions') and not user_cls.is_superadmin:
                    html += f"""<span class="btn btn-success btn-xs mt-2" onclick="update_permission('{self.data_dict.get('uuid')}', '{per}')"><i class="bi-check-circle-fill"></i>&ensp;{ptext}</span> """
                else:
                    html += f"""<span class="btn btn-default btn-xs mt-2" onclick="update_permission('{self.data_dict.get('uuid')}', '{per}')">{ptext}</span> """
            html += '</td></tr>'
        html += '</tbody>'
        html += '</table></div>'
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))

    def cz_html(self):
        html = f'''
            <div class="formBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto;">       
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">代理账户：</span>
                        <span style="display: inline-block;width: calc(100% - 250px);text-align: left;font-size: 16px;vertical-align: -1px;">{ self.data_dict.get('account') }</span>
                    </div>
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">代理姓名：</span>
                        <span style="display: inline-block;width: calc(100% - 250px);text-align: left;font-size: 16px;vertical-align: -1px;">{ self.data_dict.get('username') }</span>
                    </div>
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">充值金额：</span>
                        <input type="number" class="form-control" id="cz_amount" value="" placeholder="充值金额" aria-label="" style="display: inline-block; width: calc(100% - 250px)" onchange="monitorRechargeMoney()">
                    </div>                    
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">内充利率%：</span>
                        <input type="number" class="form-control" id="recharge_money_rate" value="{ self.data_dict.get('recharge_money_rate') * 100 if self.data_dict.get('recharge_money_rate') else 0 }" placeholder="内充利率%" aria-label="" style="display: inline-block; width: calc(100% - 250px)" onchange="monitorRechargeMoney()">
                    </div>     
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">手续费：</span>
                        <span style="display: inline-block;width: calc(100% - 250px);text-align: left;font-size: 16px;vertical-align: -1px;"><span id="repay_amount_text">0</span>元</span>
                    </div>                                   
                    <div class="list-group-item">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">备注：</span>
                        <input type="text" class="form-control" id="note" value="" placeholder="备注" aria-label="" style="display: inline-block; width: calc(100% - 250px)" onchange="monitorRechargeMoney()">
                    </div>
                </div>

                <div class="blank" style="background: #eeeeee; height: 1px; margin: 15px 0;"></div>

                <div style="position: relative; text-align: center">
                    <span class="btn btn-primary" onclick="post_recharge_money('{self.data_dict.get("uuid")}')">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>
        '''
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))

    def edit_udata_info_html(self, data_dict={}):
        html = ''
        html += f'''
            <div class="formBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto;">      
                    <div class="list-group-item" style="display: flex; justify-content: center;">
                        <span style="width: 240px; text-align: right; display: inline-block; position: relative;">出款银行卡信息：</span>
                        <textarea class="form-control" id="bankcard_info" rows="5" placeholder="出款银行卡信息" style="display: inline-block; width: calc(100% - 250px)">{ data_dict.get('bankcard_info') or '' }</textarea>                                        
                    </div>                           
                </div>
                <div class="blank" style="background: #eeeeee; height: 1px; margin: 15px 0;"></div>
                <div style="position: relative; text-align: center">
                    <span class="btn btn-primary" onclick="edit_udata_info_func('edit_udata_info', '{ data_dict.get('uuid') if data_dict else '' }')">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>        
        '''
        return self.xtjson.json_result(message=html)

    def resetPasswordHtml(self):
        html = f'''
            <div class="formBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto;">       
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">原密码：</span>
                        <input type="text" class="form-control" id="low_password" placeholder="新密码" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">新密码：</span>
                        <input type="text" class="form-control" id="password" placeholder="新密码" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>
                    <div class="list-group-item">
                        <span class="loglable" style="width: 240px; text-align: right; display: inline-block; position: relative;">确认密码：</span>
                        <input type="text" class="form-control" id="confirmPassword" placeholder="确认密码" aria-label="" style="display: inline-block; width: calc(100% - 250px)">
                    </div>                                
                </div>

                <div class="blank" style="background: #eeeeee; height: 1px; margin: 15px 0;"></div>

                <div style="position: relative; text-align: center">
                    <span class="btn btn-primary" onclick="resetPassword_func()">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>         
        '''
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))

    def post_other_way(self):
        if self.action == 'add_form_html':
            html = self.user_data_html()
            return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))
        if self.action == 'add_user_data':
            username = self.request_data.get('username') or ''
            account = self.request_data.get('account') or ''
            password = self.request_data.get('password') or ''
            role_code = self.request_data.get('role_code') or ''
            agentadmin_uuid = self.request_data.get('agentadmin_uuid') or ''
            telephone = self.request_data.get('telephone') or ''
            note = self.request_data.get('note')
            outm_min_money = self.request_data.get('outm_min_money')
            outm_max_money = self.request_data.get('outm_max_money')
            bankcard_info = self.request_data.get('bankcard_info') or ''

            _is_syscard = self.request_data.get('is_syscard')
            _system_paybehalf = self.request_data.get('system_paybehalf')
            cms_ip_whitelist = self.request_data.get('cms_ip_whitelist')
            in_vnbankqr_rate = self.request_data.get('in_vnbankqr_rate')
            in_vnzalo_rate = self.request_data.get('in_vnzalo_rate')
            in_vnmomo_rate = self.request_data.get('in_vnmomo_rate')
            in_vnvtpay_rate = self.request_data.get('in_vnvtpay_rate')
            in_vnbankqr2_rate = self.request_data.get('in_vnbankqr2_rate')
            in_vnmo2mo_rate = self.request_data.get('in_vnmo2mo_rate')
            in_vnza2lo_rate = self.request_data.get('in_vnza2lo_rate')
            in_vnvt2pay_rate = self.request_data.get('in_vnvt2pay_rate')
            paybehalf_rate = self.request_data.get('paybehalf_rate')
            recharge_money_rate = self.request_data.get('recharge_money_rate')
            issued_money_rate = self.request_data.get('issued_money_rate')
            _login_google_verify_statu = self.request_data.get('login_google_verify_statu')
            if not account or not password or not username:
                return self.xtjson.json_params_error('缺少数据！')

            if self.MCLS.find_one({"account": account}):
                return self.xtjson.json_params_error('用户已存在!')
            if len(username) > 25:
                return self.xtjson.json_params_error('姓名长度太长！')
            if len(account) > 18:
                return self.xtjson.json_params_error('账户长度太长！')
            if len(password) > 18:
                return self.xtjson.json_params_error('密码长度太长！')
            
            if self.current_admin_user.is_superadmin or self.current_admin_user.is_administrator:
                if not role_code:
                    return self.xtjson.json_params_error('缺少数据！')
                self.data_from['role_code'] = role_code
                if role_code in [ROlE_ALL.SYSTEMUSER, ROlE_ALL.OUT_MONEY_USER]:
                    if not agentadmin_uuid:
                        return self.xtjson.json_params_error('缺少数据！')
                    self.data_from['agentadmin_uuid'] = agentadmin_uuid
            elif self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                if role_code not in [ROlE_ALL.OUT_MONEY_USER, ROlE_ALL.SYSTEMUSER]:
                    return self.xtjson.json_params_error('用户角色错误！')
                self.data_from['role_code'] = role_code
                self.data_from['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
            elif self.current_admin_dict.get('role_code') in [ROlE_ALL.OUT_MONEY_USER, ROlE_ALL.SYSTEMUSER]:
                if role_code not in [ROlE_ALL.OUT_MONEY_USER, ROlE_ALL.SYSTEMUSER]:
                    return self.xtjson.json_params_error('用户角色错误！')
                self.data_from['role_code'] = role_code
                self.data_from['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
            else:
                return self.xtjson.json_params_error('操作失败！')
            if role_code == ROlE_ALL.AGENTADMIN:
                self.data_from['balance_amount'] = 0

            if (self.current_admin_user.is_superadmin or self.current_admin_user.is_administrator) and role_code == ROlE_ALL.AGENTADMIN:
                self.data_from['cms_ip_whitelist'] = cms_ip_whitelist or ''
                login_google_verify_statu = False
                if _login_google_verify_statu == '1':
                    login_google_verify_statu = True
                self.data_from['login_google_verify_statu'] = login_google_verify_statu
                is_syscard = False
                if _is_syscard == '1':
                    is_syscard = True

                self.data_from['is_syscard'] = is_syscard
                system_paybehalf = False
                if _system_paybehalf == '1':
                    system_paybehalf = True
                self.data_from['system_paybehalf'] = system_paybehalf

                if in_vnbankqr_rate:
                    try:
                        in_vnbankqr_rate = float(in_vnbankqr_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnbankqr_rate: 参数错误！')
                else:
                    in_vnbankqr_rate = 0
                self.data_from['in_vnbankqr_rate'] = round(in_vnbankqr_rate / 100, 5)

                if in_vnzalo_rate:
                    try:
                        in_vnzalo_rate = float(in_vnzalo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnzalo_rate: 参数错误！')
                else:
                    in_vnzalo_rate = 0
                self.data_from['in_vnzalo_rate'] = round(in_vnzalo_rate / 100, 5)

                if in_vnmomo_rate:
                    try:
                        in_vnmomo_rate = float(in_vnmomo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnmomo_rate: 参数错误！')
                else:
                    in_vnmomo_rate = 0
                self.data_from['in_vnmomo_rate'] = round(in_vnmomo_rate / 100, 5)

                if in_vnvtpay_rate:
                    try:
                        in_vnvtpay_rate = float(in_vnvtpay_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnvtpay_rate: 参数错误！')
                else:
                    in_vnvtpay_rate = 0
                self.data_from['in_vnvtpay_rate'] = round(in_vnvtpay_rate / 100, 5)

                if in_vnbankqr2_rate:
                    try:
                        in_vnbankqr2_rate = float(in_vnbankqr2_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnbankqr2_rate: 参数错误！')
                else:
                    in_vnbankqr2_rate = 0
                self.data_from['in_vnbankqr2_rate'] = round(in_vnbankqr2_rate / 100, 5)

                if in_vnmo2mo_rate:
                    try:
                        in_vnmo2mo_rate = float(in_vnmo2mo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnmo2mo_rate: 参数错误！')
                else:
                    in_vnmo2mo_rate = 0
                self.data_from['in_vnmo2mo_rate'] = round(in_vnmo2mo_rate / 100, 5)

                if in_vnza2lo_rate:
                    try:
                        in_vnza2lo_rate = float(in_vnza2lo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnza2lo_rate: 参数错误！')
                else:
                    in_vnza2lo_rate = 0
                self.data_from['in_vnza2lo_rate'] = round(in_vnza2lo_rate / 100, 5)

                if in_vnvt2pay_rate:
                    try:
                        in_vnvt2pay_rate = float(in_vnvt2pay_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnvt2pay_rate: 参数错误！')
                else:
                    in_vnvt2pay_rate = 0
                self.data_from['in_vnvt2pay_rate'] = round(in_vnvt2pay_rate / 100, 5)

                if paybehalf_rate:
                    try:
                        paybehalf_rate = float(paybehalf_rate) or 0
                    except:
                        return self.xtjson.json_params_error('paybehalf_rate: 参数错误！')
                else:
                    paybehalf_rate = 0
                self.data_from['paybehalf_rate'] = round(paybehalf_rate / 100, 5)

                if recharge_money_rate:
                    try:
                        recharge_money_rate = float(recharge_money_rate) or 0
                    except:
                        return self.xtjson.json_params_error('recharge_money_rate: 参数错误！')
                else:
                    recharge_money_rate = 0
                self.data_from['recharge_money_rate'] = round(recharge_money_rate / 100, 5)

                if issued_money_rate:
                    try:
                        issued_money_rate = float(issued_money_rate) or 0
                    except:
                        return self.xtjson.json_params_error('issued_money_rate: 参数错误！')
                else:
                    issued_money_rate = 0
                self.data_from['issued_money_rate'] = round(issued_money_rate / 100, 5)

            if outm_min_money:
                try:
                    outm_min_money = int(outm_min_money.strip() or 0)
                except:
                    return self.xtjson.json_params_error('出款最小值输入错误！')

            if outm_max_money:
                try:
                    outm_max_money = int(outm_max_money)
                except:
                    return self.xtjson.json_params_error('出款最大值输入错误！')

            if role_code == ROlE_ALL.OUT_MONEY_USER:
                self.data_from['bankcard_info'] = bankcard_info.strip() or ''

            self.data_from['account'] = account.strip()
            self.data_from['username'] = username.strip()
            self.data_from['password'] = self.MCLS.encry_password(password.strip())
            self.data_from['telephone'] = telephone
            self.data_from['note'] = note
            self.data_from['outm_min_money'] = outm_min_money or 0
            self.data_from['outm_max_money'] = outm_max_money or 0
            self.data_from['permissions'] = []
            __uuid = self.MCLS.insert_one(self.data_from)
            self.add_SystemLog(note='添加账户')
            if role_code == ROlE_ALL.OUT_MONEY_USER and bankcard_info.strip():
                behalfPayBankcardLogTable.insert_one({'user_uuid': __uuid, 'bankcard_info': bankcard_info.strip()})

            return self.xtjson.json_result()
        if self.action == 'resetPasswordHtml':
            return self.resetPasswordHtml()

    def post_data_other_way(self):
        if self.action == 'del':
            if self.data_uuid == self.current_admin_dict.get('uuid'):
                self.add_SystemLog(note='删除用户', code=400)
                return self.xtjson.json_params_error('当前用户不可删除！')

            permissions = self.data_dict.get('permissions') or []
            if PERMISSION_ALL.SUPERADMIN in permissions:
                self.add_SystemLog(note='删除用户', code=400)
                return self.xtjson.json_params_error('系统管理员，不可删除！')
            if self.data_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                if not self.current_admin_user.is_superadmin and not self.current_admin_user.is_administrator:
                    self.add_SystemLog(note='删除用户', code=400)
                    return self.xtjson.json_params_error('不可删除！')
                from common_utils.mongodb.mongo_model import dbModel
                for MCLS in dbModel.__subclasses__():
                    if not hasattr(MCLS, '__tablename__') or not getattr(MCLS, '__tablename__'):
                        continue
                    if MCLS.__name__ in ['TunnelTable', 'BankTable', 'SiteConfigTable']:
                        continue
                    MCLS.delete_many({'agentadmin_uuid': self.data_uuid})
            self.add_SystemLog(note='删除用户')
            self.MCLS.delete_one({'uuid': self.data_uuid})
            return self.xtjson.json_result()
        if self.action == 'edit_form_html':
            html = self.user_data_html(self.data_dict)
            return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))
        if self.action == 'edit_user_data':
            username = self.request_data.get('username') or ''
            account = self.request_data.get('account') or ''
            password = self.request_data.get('password') or ''
            telephone = self.request_data.get('telephone') or ''
            note = self.request_data.get('note')
            outm_min_money = self.request_data.get('outm_min_money')
            outm_max_money = self.request_data.get('outm_max_money')
            bankcard_info = self.request_data.get('bankcard_info') or ''

            _is_syscard = self.request_data.get('is_syscard')
            _is_addcard = self.request_data.get('is_addcard')
            _is_test_withdraw_card = self.request_data.get('is_test_withdraw_card')
            _is_clear_deposit = self.request_data.get('is_clear_deposit')
            _is_clear_withdraw = self.request_data.get('is_clear_withdraw')
            _is_clear_transit = self.request_data.get('is_clear_transit')
            _is_clear_other = self.request_data.get('is_clear_other')
            _is_clear_log = self.request_data.get('is_clear_log')
            _system_paybehalf = self.request_data.get('system_paybehalf')
            cms_ip_whitelist = self.request_data.get('cms_ip_whitelist')
            in_vnbankqr_rate = self.request_data.get('in_vnbankqr_rate')
            in_vnzalo_rate = self.request_data.get('in_vnzalo_rate')
            in_vnmomo_rate = self.request_data.get('in_vnmomo_rate')
            in_vnvtpay_rate = self.request_data.get('in_vnvtpay_rate')
            in_vnbankqr2_rate = self.request_data.get('in_vnbankqr2_rate')
            in_vnmo2mo_rate = self.request_data.get('in_vnmo2mo_rate')
            in_vnza2lo_rate = self.request_data.get('in_vnza2lo_rate')
            in_vnvt2pay_rate = self.request_data.get('in_vnvt2pay_rate')
            paybehalf_rate = self.request_data.get('paybehalf_rate')
            issued_money_rate = self.request_data.get('issued_money_rate')
            recharge_money_rate = self.request_data.get('recharge_money_rate')
            _login_google_verify_statu = self.request_data.get('login_google_verify_statu')

            if not account or not username or not account.strip():
                self.add_SystemLog(note='修改用户', code=400)
                return self.xtjson.json_params_error('缺少数据！')

            if len(username) > 25:
                return self.xtjson.json_params_error('姓名长度太长！')
            if len(account) > 18:
                return self.xtjson.json_params_error('账户长度太长！')

            if password and password.strip():
                if len(password) > 18:
                    return self.xtjson.json_params_error('密码长度太长！')
                self.data_from['password'] = self.MCLS.encry_password(password.strip())

            if self.data_dict.get('account') != account.strip() and self.MCLS.find_one({'account': account.strip()}):
                return self.xtjson.json_params_error('当前账户已存在!')

            if self.current_admin_dict.get("role_code") in [ROlE_ALL.SUPERADMIN, ROlE_ALL.AGENTADMIN]:
                is_addcard = False
                if _is_addcard == '1':
                    is_addcard = True
                self.data_from['is_addcard'] = is_addcard
                
                is_clear_deposit = False
                if _is_clear_deposit == '1':
                    is_clear_deposit = True
                self.data_from['is_clear_deposit'] = is_clear_deposit
                
                is_test_withdraw_card = False
                if _is_test_withdraw_card == '1':
                    is_test_withdraw_card = True
                self.data_from['is_test_withdraw_card'] = is_test_withdraw_card
                
                is_clear_withdraw = False
                if _is_clear_withdraw == '1':
                    is_clear_withdraw = True
                self.data_from['is_clear_withdraw'] = is_clear_withdraw
                
                is_clear_transit = False
                if _is_clear_transit == '1':
                    is_clear_transit = True
                self.data_from['is_clear_transit'] = is_clear_transit
                
                is_clear_other = False
                if _is_clear_other == '1':
                    is_clear_other = True
                self.data_from['is_clear_other'] = is_clear_other

                is_clear_log = False
                if _is_clear_log == '1':
                    is_clear_log = True
                self.data_from['is_clear_log'] = is_clear_log


            if self.current_admin_user.is_superadmin or self.data_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                self.data_from['cms_ip_whitelist'] = cms_ip_whitelist or ''
                login_google_verify_statu = False
                if _login_google_verify_statu == '1':
                    login_google_verify_statu = True
                self.data_from['login_google_verify_statu'] = login_google_verify_statu

                is_syscard = False
                if _is_syscard == '1':
                    is_syscard = True
                self.data_from['is_syscard'] = is_syscard
                
                system_paybehalf = False
                if _system_paybehalf == '1':
                    system_paybehalf = True
                self.data_from['system_paybehalf'] = system_paybehalf

                if in_vnbankqr_rate:
                    try:
                        in_vnbankqr_rate = float(in_vnbankqr_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnbankqr_rate: 参数错误！')
                else:
                    in_vnbankqr_rate = 0
                self.data_from['in_vnbankqr_rate'] = round(in_vnbankqr_rate / 100, 5)

                if in_vnzalo_rate:
                    try:
                        in_vnzalo_rate = float(in_vnzalo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnzalo_rate: 参数错误！')
                else:
                    in_vnzalo_rate = 0
                self.data_from['in_vnzalo_rate'] = round(in_vnzalo_rate / 100, 5)

                if in_vnmomo_rate:
                    try:
                        in_vnmomo_rate = float(in_vnmomo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnmomo_rate: 参数错误！')
                else:
                    in_vnmomo_rate = 0
                self.data_from['in_vnmomo_rate'] = round(in_vnmomo_rate / 100, 5)

                if in_vnvtpay_rate:
                    try:
                        in_vnvtpay_rate = float(in_vnvtpay_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnvtpay_rate: 参数错误！')
                else:
                    in_vnvtpay_rate = 0
                self.data_from['in_vnvtpay_rate'] = round(in_vnvtpay_rate / 100, 5)

                if in_vnbankqr2_rate:
                    try:
                        in_vnbankqr2_rate = float(in_vnbankqr2_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnbankqr2_rate: 参数错误！')
                else:
                    in_vnbankqr2_rate = 0
                self.data_from['in_vnbankqr2_rate'] = round(in_vnbankqr2_rate / 100, 5)

                if in_vnmo2mo_rate:
                    try:
                        in_vnmo2mo_rate = float(in_vnmo2mo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnmo2mo_rate: 参数错误！')
                else:
                    in_vnmo2mo_rate = 0
                self.data_from['in_vnmo2mo_rate'] = round(in_vnmo2mo_rate / 100, 5)

                if in_vnza2lo_rate:
                    try:
                        in_vnza2lo_rate = float(in_vnza2lo_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnza2lo_rate: 参数错误！')
                else:
                    in_vnza2lo_rate = 0
                self.data_from['in_vnza2lo_rate'] = round(in_vnza2lo_rate / 100, 5)

                if in_vnvt2pay_rate:
                    try:
                        in_vnvt2pay_rate = float(in_vnvt2pay_rate) or 0
                    except:
                        return self.xtjson.json_params_error('in_vnvt2pay_rate: 参数错误！')
                else:
                    in_vnvt2pay_rate = 0
                self.data_from['in_vnvt2pay_rate'] = round(in_vnvt2pay_rate / 100, 5)

                if paybehalf_rate:
                    try:
                        paybehalf_rate = float(paybehalf_rate) or 0
                    except:
                        return self.xtjson.json_params_error('paybehalf_rate: 参数错误！')
                else:
                    paybehalf_rate = 0
                self.data_from['paybehalf_rate'] = round(paybehalf_rate / 100, 5)

                if recharge_money_rate:
                    try:
                        recharge_money_rate = float(recharge_money_rate) or 0
                    except:
                        return self.xtjson.json_params_error('recharge_money_rate: 参数错误！')
                else:
                    recharge_money_rate = 0
                self.data_from['recharge_money_rate'] = round(recharge_money_rate / 100, 5)

                if issued_money_rate:
                    try:
                        issued_money_rate = float(issued_money_rate) or 0
                    except:
                        return self.xtjson.json_params_error('issued_money_rate: 参数错误！')
                else:
                    issued_money_rate = 0
                self.data_from['issued_money_rate'] = round(issued_money_rate / 100, 5)

            if outm_min_money:
                try:
                    outm_min_money = int(outm_min_money.strip() or 0)
                except:
                    return self.xtjson.json_params_error('出款最小值输入错误！')

            if outm_max_money:
                try:
                    outm_max_money = int(outm_max_money)
                except:
                    return self.xtjson.json_params_error('出款最大值输入错误！')

            if self.data_dict.get('role_code') in [ROlE_ALL.OUT_MONEY_USER, ROlE_ALL.SYS_OUT_MONEY_USER] and self.data_dict.get('bankcard_info') != bankcard_info.strip():
                self.data_from['bankcard_info'] = bankcard_info.strip()
                behalfPayBankcardLogTable.insert_one({'user_uuid': self.data_uuid, 'bankcard_info': bankcard_info.strip()})

            self.data_from['account'] = account.strip()
            self.data_from['username'] = username.strip()
            self.data_from['telephone'] = telephone
            self.data_from['note'] = note
            self.data_from['outm_min_money'] = outm_min_money or 0
            self.data_from['outm_max_money'] = outm_max_money or 0

            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            self.add_SystemLog(note='修改用户')
            return self.xtjson.json_result()
        if self.action == 'update_statu':
            if self.data_dict.get('statu'):
                self.data_from['statu'] = False
            else:
                self.data_from['statu'] = True
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            return self.xtjson.json_result()
        if self.action == 'getGoogleQrcode':
            if not self.data_uuid:
                self.add_SystemLog(note='获取用户GOOGLE码', code=400)
                return self.xtjson.json_params_error()

            user_dict = self.MCLS.find_one({'uuid': self.data_uuid})
            if not user_dict:
                return self.xtjson.json_params_error()

            google_cls = GooleVerifyCls(pwd=self.data_uuid, account=user_dict.get('account'), s_label='pay2wold')
            generate_qrcode = google_cls.secret_generate_qrcode()
            self.add_SystemLog(note='获取用户GOOGLE码')
            return self.xtjson.json_result(data={'generate_qrcode': generate_qrcode})
        if self.action == 'get_permission_html':
            crrUser = self.MCLS.query_one({'uuid': self.data_uuid})
            return self.get_permission(crrUser)
        if self.action == '_edit_permission':
            crrUser = self.MCLS.query_one({'uuid': self.data_uuid})
            if crrUser.is_superadmin:
                return self.xtjson.json_params_error('最高管理员权限不可修改!')
            if crrUser.role_code == ROlE_ALL.AGENTADMIN:
                return self.xtjson.json_params_error('代理权限不可调节!')
            per = self.request_data.get('p')
            if not per:
                return self.xtjson.json_params_error('操作错误!')
            u_permissions = self.data_dict.get('permissions') or []
            if per in u_permissions:
                u_permissions.remove(per)
            else:
                u_permissions.append(per)
            if PERMISSION_ALL.SUPERADMIN in u_permissions:
                return self.xtjson.json_params_error('操作错误!')
            self.data_dict['permissions'] = u_permissions
            self.MCLS.save(self.data_dict)
            return self.get_permission(crrUser)
        if self.action == 'cz_html':
            return self.cz_html()
        if self.action == 'rechargeMoney':
            if self.data_dict.get('role_code') != ROlE_ALL.AGENTADMIN:
                return self.xtjson.json_params_error('操作错误！')
            note = self.request_data.get('note') or ''
            cz_amount = self.request_data.get('cz_amount')
            recharge_money_rate = self.request_data.get('recharge_money_rate')

            if recharge_money_rate:
                try:
                    recharge_money_rate = float(recharge_money_rate) or 0
                except:
                    return self.xtjson.json_params_error('recharge_money_rate: 参数错误！')
            else:
                recharge_money_rate = 0

            if recharge_money_rate >= 100:
                return self.xtjson.json_params_error('内充利率要小于100%！')

            if cz_amount:
                try:
                    cz_amount = float(cz_amount) or 0
                except:
                    return self.xtjson.json_params_error('cz_amount: 参数错误！')
            else:
                cz_amount = 0

            if cz_amount <= 0:
                return self.xtjson.json_params_error('充值金额要大于0！')

            repay_amount = 0
            if recharge_money_rate:
                repay_amount = round(cz_amount * recharge_money_rate/100.0, 2)

            zs_cz_money = cz_amount - repay_amount
            _balance_amount = self.data_dict.get('balance_amount') or 0
            balance_amount = _balance_amount + zs_cz_money

            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': {'balance_amount': balance_amount}})

            _log = {
                'agentadmin_uuid': self.data_uuid,
                'amount': cz_amount,
                'repay_amount': repay_amount,
                'balance_amount': balance_amount,
                'bill_type': BILL_STATEMEN_TYPES.RECHARGE,
                'note': note or '',
            }
            AgentadminBillLogTable.insert_one(_log)
            return self.xtjson.json_result()
        if self.action == 'jmoney_html':
            return self.jmoney_html()
        if self.action == 'kcMoney_data':
            jmoney = self.request_data.get('jmoney')
            note = self.request_data.get('note') or ''
            try:
                jmoney = int(jmoney)
            except:
                return self.xtjson.json_params_error('金额输入错误！')

            _balance_amount = self.data_dict.get('balance_amount') or 0
            balance_amount = _balance_amount - jmoney

            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': {'balance_amount': balance_amount}})

            _log = {
                'agentadmin_uuid': self.data_uuid,
                'amount': jmoney,
                'repay_amount': 0,
                'balance_amount': balance_amount,
                'bill_type': BILL_STATEMEN_TYPES.REDUCE,
                'note': note.strip() or '',
            }
            AgentadminBillLogTable.insert_one(_log)
            return self.xtjson.json_result()
        if self.action == 'updateOnlineStatu':
            if self.data_dict.get('is_online'):
                self.data_from['is_online'] = False
            else:
                self.data_from['is_online'] = True
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            return self.xtjson.json_result()
        if self.action == 'detailsInfo_html':
            return self.detailsInfo_html(self.data_uuid)
        if self.action == 'edit_udata_info_html':
            return self.edit_udata_info_html(self.data_dict)
        if self.action == 'edit_udata_info':
            bankcard_info = self.request_data.get('bankcard_info')
            if not bankcard_info or not bankcard_info.strip():
                return self.xtjson.json_params_error('请输入出款账户信息！')
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': {'bankcard_info': bankcard_info.strip()}})
            return self.xtjson.json_result()
        if self.action == 'resetPassword':
            password = self.request_data.get('password')
            low_password = self.request_data.get('low_password')
            if not password or not low_password or not password.strip() or not low_password.strip():
                return self.xtjson.json_params_error()

            if not self.current_admin_user.check_password(self.data_dict.get('password'), low_password.strip()):
                return self.xtjson.json_params_error('原密码错误！')

            self.data_from['password'] = self.MCLS.encry_password(password.strip())
            print(self.data_from)
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            return self.xtjson.json_result()
