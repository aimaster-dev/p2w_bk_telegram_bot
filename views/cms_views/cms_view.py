import os, requests, datetime, re, json
from .cms_base import CmsFormViewBase, CmsTableViewBase
from flask import render_template, request, current_app
from models.cms_table import SiteConfigTable, SystemLogTable
from models.pay_table import TunnelTable, CollectionOrderTable, MerchantTable, VpnTable, BankCardTable, BankTable
from common_utils.utils_funcs import getDayDateSilce, PagingCLS
from constants import PAY_METHOD, CallbackState, BANK_CODE, taskStatus, ROlE_ALL, REQUEST_METHOD, CHECK_ANAME_STATES, OPERATION_TYPES, BANK_SCRIPT_ALL
from models.cms_user import CmsUserTable
from models.site_table import ExportDataModel
from models.pay_table import ApiRequestLogTable
from common_utils.utils_funcs import update_language


class CmsIndexView(CmsFormViewBase):
    add_url_rules = [['/', 'cms_index']]
    title = '世界付'

    def view_get(self):
        self.context['title'] = self.title

        fff1 = {}
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            fff1['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            fff1['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')

        # 商户总余额
        ddsls = MerchantTable.collection().aggregate([
            {"$match": fff1},
            {"$group": {"_id": None, "balance_amount": {"$sum": '$balance_amount'}}},
        ])
        total_balance_amount = 0
        if ddsls:
            ddsls = list(ddsls)
        if ddsls:
            total_balance_amount = list(ddsls)[0].get('balance_amount') or 0
        self.context['total_balance_amount'] = self.format_money(round(total_balance_amount, 2))

        # 今日订单数量
        time_start, time_end = getDayDateSilce()
        fff3 = {}
        fff2 = {'order_time': {'$gte':time_start, '$lte': time_end}}
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            fff2['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
            fff3['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            fff2['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
            fff3['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        orderDayCount = CollectionOrderTable.count(fff2)
        self.context['orderDayCount'] = orderDayCount or 0

        # 订单总数量
        allOrderCount = CollectionOrderTable.count(fff3)
        self.context['allOrderCount'] = allOrderCount or 0

        # 今日代收金额
        fff2['pay_statu'] = True
        ddsls = CollectionOrderTable.collection().aggregate([
            {"$match": fff2},
            {"$group": {"_id": None, "actual_amount": {"$sum": '$actual_amount'}}},
        ])
        day_actual_amount = 0
        if ddsls:
            ddsls = list(ddsls)
        if ddsls:
            day_actual_amount = list(ddsls)[0].get('actual_amount') or 0
        self.context['day_actual_amount'] = self.format_money(round(day_actual_amount, 2))

        html = render_template('cms/index.html', **self.context)
        return update_language(self.current_admin_dict.get("language"), html)

    def post_other_way(self):
        if self.action == 'updateOnlineStatu':
            if self.current_admin_user.is_online:
                self.data_from['is_online'] = False
            else:
                self.data_from['is_online'] = True
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            return self.xtjson.json_result()


class SettingView(CmsFormViewBase):
    add_url_rules = [['/setting', 'setting_view']]
    title = '系统设置'
    MCLS = SiteConfigTable

    def getConfig(self):
        site_data = {}
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            site_data['cms_ip_whitelist'] = self.current_admin_dict.get('cms_ip_whitelist') or ''
            site_data['login_google_verify_statu'] = self.current_admin_dict.get('login_google_verify_statu')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            site_data['cms_ip_whitelist'] = self.current_admin_dict.get('agentadmin_data').get('cms_ip_whitelist') or ''
            site_data['login_google_verify_statu'] = self.current_admin_dict.get('agentadmin_data').get('login_google_verify_statu')
        else:
            _data = self.MCLS.find_one({})
            ks = [
                'cms_ip_whitelist', 'login_google_verify_statu', 'bank_collect_api_reqcount', 'bank_collect_api_sleep', 'site_domain'
            ]
            for k in ks:
                site_data[k] = _data.get(k) or ''
        return site_data

    def check_domain(self, url):
        pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        if re.match(pattern, url):
            return True
        return False

    def updateNginxConfig(self, update_site_domain_text):
        configText = '''
server {
    listen 80;
    server_name %s;
    root /www/pay2world;

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:5030;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        alias /www/pay2world/static;
    }

    location /public/world/img {
        alias /www/pay2world/static/pay2world/public/img;
        expires 30d;  # 设置缓存有效期为30天
        add_header Cache-Control "public, no-transform";  # 设置缓存控制头
    }

    location /assets/bank/img {
        alias /www/pay2world/static/project_pay2world/assets/bank/img;
        expires 30d;  # 设置缓存有效期为30天
        add_header Cache-Control "public, no-transform";  # 设置缓存控制头
    }

}
        ''' % update_site_domain_text
        with open('/etc/nginx/sites-enabled/pay2wold_dd2.conf', 'w+') as wd:
            wd.write(configText)
        cmd = 'sudo service nginx reload'
        os.popen(cmd)

    def view_get(self):
        self.context['title'] = self.title
        self.context['site_data'] = self.getConfig()

        html = render_template('cms/setting.html', **self.context)
        return update_language(self.current_admin_dict.get("language"), html)

    def post_other_way(self):
        if self.action == 'update_language':
            language = self.request_data.get('language')
            CmsUserTable.update_one({"uuid": self.current_admin_dict.get('uuid')},{
                '$set': {'language': language}})

            return self.xtjson.json_result()
            
        if self.action == 'getSiteConfig':
            site_data = self.getConfig()
            return self.xtjson.json_result(data=site_data)
        if self.action == 'updateConfig':
            cms_ip_whitelist = self.request_data.get('cms_ip_whitelist')
            _login_google_verify_statu = self.request_data.get('login_google_verify_statu')

            self.data_from['cms_ip_whitelist'] = cms_ip_whitelist or ''
            login_google_verify_statu = False
            if _login_google_verify_statu == '1':
                login_google_verify_statu = True
            self.data_from['login_google_verify_statu'] = login_google_verify_statu

            if self.current_admin_user.is_superadmin or self.current_admin_user.is_administrator:
                bank_collect_api_reqcount = self.request_data.get('bank_collect_api_reqcount')
                bank_collect_api_sleep = self.request_data.get('bank_collect_api_sleep')
                site_domain = self.request_data.get('site_domain')
                if not bank_collect_api_reqcount:
                    bank_collect_api_reqcount = 0
                else:
                    try:
                        bank_collect_api_reqcount = int(bank_collect_api_reqcount.strip())
                    except:
                        return self.xtjson.json_params_error('bank_collect_api_sleep: 参数错误！')
                if not bank_collect_api_sleep:
                    bank_collect_api_sleep = 0
                else:
                    try:
                        bank_collect_api_sleep = int(bank_collect_api_sleep.strip())
                    except:
                        return self.xtjson.json_params_error('bank_collect_api_sleep: 参数错误！')

                self.data_from['bank_collect_api_reqcount'] = bank_collect_api_reqcount
                self.data_from['bank_collect_api_sleep'] = bank_collect_api_sleep

                is_update = False
                _update_site_domain_text = ''
                _site_data = self.MCLS.find_one({})
                if self.current_admin_user.is_superadmin and site_domain and site_domain.strip():
                    _site_domain = ''
                    for ff in site_domain.split('\n'):
                        if not self.check_domain(ff):
                            return self.xtjson.json_params_error(f'{ff}:域名格式错误！')
                        _site_domain += ff.strip() + '\n'
                        _update_site_domain_text += ff.strip() + ' '
                    self.data_from['site_domain'] = _site_domain.strip('\n') or ''
                    if _site_data.get('site_domain') != _site_domain and _site_domain:
                        is_update = True
                _site_data.update(self.data_from)
                self.MCLS.save(_site_data)
                if is_update:
                    self.updateNginxConfig(_update_site_domain_text)
            elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
                CmsUserTable.update_one({'uuid': self.current_admin_dict.get('agentadmin_uuid')}, {'$set': self.data_from})
            elif self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                CmsUserTable.update_one({'uuid': self.current_admin_dict.get('uuid')}, {'$set': self.data_from})

            self.add_SystemLog('更新系统配置')
            return self.xtjson.json_result()



class TunnelView(CmsFormViewBase):
    add_url_rules = [['/tunnle', 'tunnle_view']]
    title = '收款通道'
    MCLS = TunnelTable

    def view_get(self):
        datas = self.MCLS.find_many({})
        self.context['title'] = self.title
        self.context['datas'] = datas
        html = render_template('cms/tunnle.html', **self.context)
        return update_language(self.current_admin_dict.get("language"), html)

    def post_data_other_way(self):
        if self.action == 'update_statu':
            if self.data_dict.get('tunnel_statu'):
                self.data_from['tunnel_statu'] = False
            else:
                self.data_from['tunnel_statu'] = True
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            self.add_SystemLog('更新通道状态')
            return self.xtjson.json_result()



class BankScriptListView(CmsFormViewBase):
    add_url_rules = [['/bankScript', 'bankScript']]
    title = '银行脚本列表'
    MCLS = TunnelTable

    def view_get(self):
        cmd = 'supervisorctl status'
        cmdreault = os.popen(cmd)
        cmdtext = cmdreault.read()
        datas = []
        for dd in cmdtext.split('\n'):
            _vv = []
            for d1 in dd.split('  '):
                _v = d1.strip()
                if not _v:
                    continue
                if 'uptime' in _v:
                    _v = _v.split('uptime')[-1].strip()
                _vv.append(_v)
            if not _vv:
                continue
            if len(_vv) != 3 and _vv[0] not in BANK_SCRIPT_ALL:
                continue
            if 'STARTING' in _vv:
                _dv = {
                    'task_name': _vv[0],
                    'run_time': '00:00:00',
                    'statu': True
                }
            else:
                _dv = {
                    'task_name': _vv[0],
                    'run_time': _vv[-1],
                }
                if _vv[1] == 'RUNNING':
                    _dv['statu'] = True
                else:
                    _dv['statu'] = False
            bank_data = BANK_SCRIPT_ALL.get(_dv.get('task_name'))
            if not bank_data:
                continue
            _dv['bank_data'] = bank_data
            datas.append(_dv)
        self.context['datas'] = datas
        html = render_template('cms/bankScript.html', **self.context)
        return update_language(self.current_admin_dict.get("language"), html)

    def post_other_way(self):
        if self.action == 'startScript':
            if self.data_uuid not in BANK_SCRIPT_ALL:
                return self.xtjson.json_params_error()
            cmd = 'supervisorctl start ' + self.data_uuid
            os.popen(cmd)
            self.add_SystemLog('更新银行脚本开启状态')
            return self.xtjson.json_result()
        if self.action == 'stopScript':
            if self.data_uuid not in BANK_SCRIPT_ALL:
                return self.xtjson.json_params_error()
            cmd = 'supervisorctl stop ' + self.data_uuid
            os.popen(cmd)
            self.add_SystemLog('更新银行脚本开启状态')
            return self.xtjson.json_result()



class SystemLogListView(CmsTableViewBase):
    add_url_rules = [['/systemLog', 'systemLog']]
    per_page = 30
    MCLS = SystemLogTable
    template = 'cms/systemLog.html'
    title = '系统日志'

    def get_filter_dict(self):
        fff = {
            'note': {'$ne': OPERATION_TYPES.name_dict.get(OPERATION_TYPES.ACCESS)}
        }
        uname = request.args.get('uname')
        if uname and uname.strip():
            fff.update({'$or': [{'username': uname.strip()}, {'account': uname.strip()}]})

        if self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            fff['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            fff['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        return fff

    def dealwith_main_context(self):
        all_datas = self.context.get('all_datas')
        _datas = []
        for d in all_datas:
            udata = CmsUserTable.find_one({'uuid': d.get('user_uuid')}) or {}
            d['udata'] = udata
            _datas.append(d)
        self.context['all_datas'] = _datas
        uname = request.args.get('uname')
        if uname and uname.strip():
            search_res = self.context.get('search_res') or {}
            search_res['uname'] = uname
            self.context['search_res'] = search_res



class VpnView(CmsTableViewBase):
    add_url_rules = [['/vpnList', 'vpnList']]
    per_page = 30
    MCLS = VpnTable
    template = 'cms/vpnList.html'
    title = 'VPN列表'

    def getProxy(self, is_proxy_str):
        try:
            ip, port, username, password = is_proxy_str.replace(' ', '').split(':')
            proxies = {
                "http": f"http://{username}:{password}@{ip}:{port}",
                "https": f"http://{username}:{password}@{ip}:{port}",
            }
            return proxies
        except:
            return

    def testVpnReq(self, vpn):
        proxies = self.getProxy(vpn)
        if not proxies:
            return
        ip, port, username, password = vpn.replace(' ', '').split(':')
        try:
            req = requests.get(url='https://api.ipify.org/?format=json', timeout=15, proxies=proxies)
            data_json = req.json()
            if data_json.get('ip') == ip:
                return True
            return
        except:
            return

    def form_bulkvpn_html(self, action = 'add'):
        udatahtml = ''
        udatas = CmsUserTable.find_many({'role_code': ROlE_ALL.AGENTADMIN})
        for udata in udatas:
            udatahtml += '''
            <option value="%s">%s  (%s)</option>
            ''' % (udata.get('uuid'), udata.get('account'), udata.get('username'))
        
        add_html = f'''
        <div class="list-group-item">
            <span style="width: 120px; text-align: right; display: inline-block; position: relative;">绑定代理：</span>
            <select class="form-control" id="agentadmin_uuid" aria-label="" style="display: inline-block; width: calc(100% - 180px)">
                <option value="">选择代理</option>
                { udatahtml }
            </select>
        </div>
        <div class="list-group-item">
            <span style="width: 120px; text-align: right; display: inline-block; position: relative;">备注：</span>
            <input type="text" class="form-control" id="note" placeholder="备注" aria-label="" style="display: inline-block; width: calc(100% - 180px)">
        </div>   
        ''' if action == 'add' else ''

        placeholder = f''' 输入如下 vpn 数据
        103.176.150.35:38866:linhvudieu329:l0Ks3Jp
        103.175.65.23:38866:linhvudieu329:l0Ks3Jp
        103.176.150.184:38866:linhvudieu329:l0Ks3Jp
        ''' if action == 'add' else f''' 输入如下 vpn 数据
        103.176.150.35:38866:linhvudieu329:l0Ks3Jp
        103.175.65.23:38866:linhvudieu329:l0Ks3Jp
        103.176.150.184:38866:linhvudieu329:l0Ks3Jp
或者
        103.176.150.35
        103.175.65.23
        103.176.150.184
        '''

        html = f'''
            <div class="formBox">
                <div class="list-group-item">
                    <div id="vpn_content"style="height: 24rem; position: relative; box-sizing: border-box; overflow-y: auto;">          
                        <span style="width: 120px; text-align: right; display: inline-block; position: relative;">VPN：</span>
                        <textarea class="form-control" rows="15" id="bulk_vpn" placeholder='{placeholder}' style="display: inline-block; width: calc(100% - 180px)"></textarea>
                    </div>
                </div> 
                {add_html}
             
                <div style="position: relative; text-align: center; margin-top:15px">
                    <span class="btn btn-primary" onclick="post_bulkvpn_data('{action}')">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>
        '''
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))
    
    def form_vpn_html(self, data_dict={}):
        _action = 'add_vpn_data'
        if data_dict:
            _action = 'edit_vpn_data'

        udatahtml = ''
        udatas = CmsUserTable.find_many({'role_code': ROlE_ALL.AGENTADMIN})
        for udata in udatas:
            if data_dict:
                udatahtml += f'''
                <option value="{udata.get('uuid')}" { 'selected' if data_dict.get('agentadmin_uuid') == udata.get('uuid') else '' }>{ udata.get('account') } ({ udata.get('username')})</option>
                '''
            else:
                udatahtml += '''
                <option value="%s">%s  (%s)</option>
                ''' % (udata.get('uuid'), udata.get('account'), udata.get('username'))

        html = f'''
            <div class="formBox">
                <div style="height: 28rem; position: relative; box-sizing: border-box; overflow-y: auto;">          
                    <div class="list-group-item">
                        <span class="loglable" style="width: 120px; text-align: right; display: inline-block; position: relative;">名称：</span>
                        <input type="text" class="form-control" id="name" value="{data_dict.get('name') or ''}" placeholder="名称" aria-label="" style="display: inline-block; width: calc(100% - 180px)">
                    </div>
                    <div class="list-group-item">
                        <span class="loglable" style="width: 120px; text-align: right; display: inline-block; position: relative;">VPN 链接：</span>
                        <input type="text" class="form-control" id="vpn_url" value="{data_dict.get('vpn_url') or ''}" placeholder="VPN 链接" aria-label="" style="display: inline-block; width: calc(100% - 180px)">
                    </div>
                    <div class="list-group-item">
                        <span style="width: 120px; text-align: right; display: inline-block; position: relative;">绑定代理：</span>
                        <select class="form-control" id="agentadmin_uuid" aria-label="" style="display: inline-block; width: calc(100% - 180px)">
                            <option value="">选择代理</option>
                            { udatahtml }
                        </select>
                    </div>
                    <div class="list-group-item">
                        <span style="width: 120px; text-align: right; display: inline-block; position: relative;">备注：</span>
                        <input type="text" class="form-control" id="note" value="{data_dict.get('note') or ''}" placeholder="备注" aria-label="" style="display: inline-block; width: calc(100% - 180px)">
                    </div>     
                </div>

                <div class="blank" style="background: #eeeeee; height: 1px; margin: 15px 0;"></div>

                <div style="position: relative; text-align: center">
                    <span class="btn btn-primary" onclick="post_vpn_data('{_action}', '{data_dict.get('uuid') if data_dict else ''}')">确定</span>&emsp;
                    <span class="btn btn-default" onclick="xtalert.close()">取消</span>
                </div>                                                                                 
            </div>
        '''
        return self.xtjson.json_result(message=update_language(self.current_admin_dict.get("language"), html))

    def dealwith_main_context(self):
        all_datas = self.context['all_datas']
        datas = []
        for data in all_datas:
            bcount = BankCardTable.count({'vpn_uuid': data.get('uuid')}) or 0
            data['bcount'] = bcount

            dd = BankCardTable.collection().aggregate([
                {"$match": {'vpn_uuid': data.get('uuid')}},
                {"$group": {"_id": "$bank_uid", "count": {"$sum": 1}}}
            ])
            bkcount = len(list(dd))
            data['bkcount'] = bkcount

            datas.append(data)
        self.context['all_datas'] = datas

    def post_other_way(self):
        if self.action == 'add_bulkvpn_html':
            return self.form_bulkvpn_html('add')
        if self.action == 'del_bulkvpn_html':
            return self.form_bulkvpn_html('del')
        if self.action == 'add_vpn_html':
            return self.form_vpn_html()
        if self.action == 'add_vpn_data':
            name = self.request_data.get('name')
            note = self.request_data.get('note')
            vpn_url = self.request_data.get('vpn_url')
            agentadmin_uuid = self.request_data.get('agentadmin_uuid')
            if not vpn_url:
                return self.xtjson.json_params_error('缺少数据！')

            if self.MCLS.find_one({'vpn_url': vpn_url}):
                return self.xtjson.json_params_error('重复数据!')

            _data = {
                "name": name.strip(),
                "vpn_url": vpn_url.strip() or '',
                "note": note or '',
                "agentadmin_uuid": agentadmin_uuid or '',
                'statu': True,
            }
            self.MCLS.insert_one(_data)
            return self.xtjson.json_result()
        if self.action == 'add_bulk_vpn':
            vpn_url = self.request_data.get('vpn_url')
            note = self.request_data.get('note')
            agentadmin_uuid = self.request_data.get('agentadmin_uuid')
            vpns = vpn_url.split('\n')

            for vpn in vpns:
                name = vpn.split(":")[0]
                if not vpn:
                    return self.xtjson.json_params_error('缺少数据！')
                if not name:
                    return self.xtjson.json_params_error('缺少数据！')
                if self.MCLS.find_one({'vpn_url': vpn}):
                    continue
                _data = {
                    "name": name.strip(),
                    "vpn_url": vpn.strip() or '',
                    "note": note or '',
                    "agentadmin_uuid": agentadmin_uuid or '',
                    'statu': True,
                }
                self.MCLS.insert_one(_data)

        if self.action == 'del_bulk_vpn':
            vpn_url = self.request_data.get('vpn_url')
            vpns = vpn_url.split('\n')

            for vpn in vpns:
                name = vpn.split(":")[0]
                if not vpn:
                    continue
                self.MCLS.delete_many({'vpn_url': {"$regex": vpn}})
             
            return self.xtjson.json_result()
        if self.action == 'allCheckVpn':
            return self.xtjson.json_result(message='后台检测中，请稍后查看！')

    def post_data_other_way(self):
        if self.action == 'edit_vpn_html':
            return self.form_vpn_html(self.data_dict)
        if self.action == 'edit_vpn_data':
            name = self.request_data.get('name')
            note = self.request_data.get('note')
            vpn_url = self.request_data.get('vpn_url')
            agentadmin_uuid = self.request_data.get('agentadmin_uuid')
            if not vpn_url:
                return self.xtjson.json_params_error('缺少数据！')

            _data = {
                "name": name.strip(),
                "vpn_url": vpn_url.strip() or '',
                "note": note or '',
                "agentadmin_uuid": agentadmin_uuid or '',
            }
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': _data})
            return self.xtjson.json_result()
        if self.action == 'update_statu':
            if self.data_dict.get('statu'):
                self.data_from['statu'] = False
            else:
                self.data_from['statu'] = True
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            return self.xtjson.json_result()
        if self.action == 'testVpn':
            vpn_url = self.data_dict.get('vpn_url')
            if not vpn_url:
                return self.xtjson.json_params_error('测试失败！')
            req = self.testVpnReq(vpn_url)
            if not req:
                self.data_from['statu'] = False
            else:
                self.data_from['statu'] = True
            self.MCLS.update_one({'uuid': self.data_uuid}, {'$set': self.data_from})
            return self.xtjson.json_result()
        if self.action == 'get_bankcard_lsit':
            _datas = BankCardTable.find_many({'vpn_uuid': self.data_uuid}) or []
            if not _datas:
                return self.xtjson.json_params_error('暂无银行卡绑定该VPN！')
            bankcard_datas = []
            for _da in _datas:
                bank_data = BankTable.find_one({'uuid': _da.get('bank_uid')}) or {}
                bankcard_datas.append({
                    'account': _da.get('account'),
                    'account_username': _da.get('account_username'),
                    'short_name': bank_data.get('shortName'),
                })
            return self.xtjson.json_result(data={'bankcard_datas': bankcard_datas})
        if self.action == 'del':
            self.MCLS.delete_one({'uuid': self.data_uuid})
            return self.xtjson.json_result()

class ExportFilesView(CmsTableViewBase):
    title = '导出文件'
    MCLS = ExportDataModel
    add_url_rules = [['/exportFiles', 'ExportFilesView']]
    template = 'cms/exportFile.html'
    per_page = 20
    sort = [['create_time', -1]]

    def get_filter_dict(self):
        dd = {}
        if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
            dd['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
        elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
            dd['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
        return dd

    def post_other_way(self):
        if self.action == 'del_all':
            self.MCLS.delete_many({})
            return self.xtjson.json_result()
        if self.action == 'batchDel':
            create_time = request.args.get('create_time')
            filename = request.args.get('filename')
            if create_time and create_time.strip():
                start_time, end_time = PagingCLS.by_silce(create_time)
            else:
                crrdate = datetime.datetime.now()
                start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0,0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day,23, 59, 59)
            fff = {}
            if create_time:
                fff['create_time'] = {'$gte': start_time, '$lte': end_time}
            if filename:
                fff['filename'] = filename.strip()
            if not fff:
                return self.xtjson.json_params_error('请先进行筛选')
            if self.current_admin_dict.get('role_code') == ROlE_ALL.AGENTADMIN:
                fff['agentadmin_uuid'] = self.current_admin_dict.get('uuid')
            elif self.current_admin_dict.get('role_code') == ROlE_ALL.SYSTEMUSER:
                fff['agentadmin_uuid'] = self.current_admin_dict.get('agentadmin_uuid')
            datas = self.MCLS.find_many(fff) or []
            for data in datas:
                filePath = current_app.static_folder + '/' + current_app.config.get('PROJECT_NAME') + data.get('path')
                if os.path.exists(filePath):
                    os.remove(filePath)
                self.MCLS.delete_one({'uuid': data.get('uuid')})
            return self.xtjson.json_result()

    def post_data_other_way(self):
        if self.action == 'del':
            filePath = current_app.static_folder + '/' + current_app.config.get('PROJECT_NAME') + self.data_dict.get('path')
            if os.path.exists(filePath):
                os.remove(filePath)
            self.MCLS.delete_one({'uuid': self.data_uuid})
            return self.xtjson.json_result(message='数据删除成功！')



class ApiLogView(CmsTableViewBase):
    title = 'API请求日志'
    MCLS = ApiRequestLogTable
    add_url_rules = [['/apiLog', 'ApiLogView']]
    template = 'cms/apiLog.html'
    per_page = 50
    sort = [['create_time', -1]]

    def get_filter_dict(self):
        fff = {}
        order_time = request.args.get('create_time')
        if order_time and order_time.strip():
            start_time, end_time = PagingCLS.by_silce(order_time)
        else:
            crrdate = datetime.datetime.now()
            start_time, end_time = datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 0, 0,0), datetime.datetime(crrdate.year, crrdate.month, crrdate.day, 23,59, 59)
            order_time = start_time.strftime('%Y-%m-%d %H:%M:%S') + '|' + end_time.strftime('%Y-%m-%d %H:%M:%S')
        fff['create_time'] = {'$gte': start_time, '$lte': end_time}

        if 'request_method' in self.filter_dict:
            del self.filter_dict['request_method']
        print(self.filter_dict)

        request_method = request.args.get('request_method')
        if request_method == 'post':
            fff['$or'] = [{"request_method": 'psot'}, {"request_method": 'post'}]
        elif request_method == 'get':
            fff["request_method"]= request_method,

        return fff

