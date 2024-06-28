import requests
import json
import time
from requests.cookies import RequestsCookieJar
import re
import urllib.parse
import html
from models.pay_table import BankAccountCacheTable


class BANK_VAB_1:

    def __init__(self, username, password, account_number, is_proxy=None):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.keyanticaptcha = "b8246038ce1540888c4314a6c043dcae"
        self.cookies = RequestsCookieJar()
        self.session = requests.Session()
        self._ss = ''
        self.bank_code = 'VAB'
        self.proxy = None
        if is_proxy:
            self.proxy = self.getProxy(is_proxy)
        self.session.cookies.clear()
        self.session.cookies.update(self.getUserToken)

    def getProxy(self, is_proxy_str):
        ip, port, username, password = is_proxy_str.replace(' ','').split(':')
        proxies = {
            "http": f"http://{username}:{password}@{ip}:{port}",
            "https": f"http://{username}:{password}@{ip}:{port}",
        }
        return proxies

    @property
    def getUserToken(self):
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            return {}
        return json.loads(_data.get('token') or '{}')

    def updateUserInfo(self):
        data_json = self.session.cookies.get_dict()
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            _d = {
                'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code,
                'token': json.dumps(data_json),
                'req_data': json.dumps(data_json),
            }
            BankAccountCacheTable.insert_one(_d)
        else:
            BankAccountCacheTable.update_one({'uuid': _data.get('uuid')},{'$set': {
                'token': json.dumps(data_json),
                'req_data': json.dumps(data_json),
            }})

    def check_title(self, html_content):
        pattern = r'<title>(.*?)</title>'
        match = re.search(pattern, html_content)
        return match.group(1) if match else None

    def check_error_message(self, html_content):
        pattern = r'<div id="ul.errors" class="errorblock" style="color:red; ">(.*?)</div>'
        match = re.search(pattern, html_content)
        return match.group(1) if match else None

    def extract_data_cId(self, html_content):
        pattern = r'<input id="data_cId" name="data_cId" type="hidden" value="(.*)"/>'
        match = re.search(pattern, html_content)
        return match.group(1) if match else None

    def extract_transaction(self, html_content):
        pattern = r'var transHis = (.*)];'
        match = re.search(pattern, html_content)
        return match.group(1) + ']' if match else None

    def extract_account_number(self, html_content):
        pattern = r'<a href="/accountdetailsview\.html\?pid=\w+&fcid=asmp">(\d+)</a>\s*-\s*.*?<td.*?>([\d,.]+)</td>'

        matches = re.findall(pattern, html_content, re.DOTALL)

        extracted_data = []
        for match in matches:
            account_number = match[0]
            account_balance = float(match[1].replace(',', ''))
            account_info = {'account_number': account_number, 'balance': account_balance}
            extracted_data.append(account_info)

        if extracted_data:
            return (extracted_data)
        else:
            return None

    def doLogin(self):
        self.session.cookies.clear()
        url = "https://ebanking.vietabank.com.vn/"
        payload = {}
        headers = {}
        try:
            response = self.session.get(url, headers=headers, data=payload, timeout=15, proxies=self.proxy)
        except:
            return

        url = "https://ebanking.vietabank.com.vn/"
        payload = 'disable-pwd-mgr-1=disable-pwd-mgr-1&disable-pwd-mgr-2=disable-pwd-mgr-2&disable-pwd-mgr-3=disable-pwd-mgr-3&askRename=&askRenameMsg=&actionFlg=&idChannelUser=' + str(self.username) + '&password=' + urllib.parse.quote(str(self.password))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ebanking.vietabank.com.vn',
            'Connection': 'keep-alive',
            'Referer': 'https://ebanking.vietabank.com.vn/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = self.session.post(url, headers=headers, data=payload, timeout=15, proxies=self.proxy)
        except:
            return
        self._ss = str(int(time.time() * 1000))
        title = self.check_title(response.text)
        if title == 'Tổng quan tài khoản':
            self.updateUserInfo()
            return {
                'success': True,
                'message': 'Đăng nhập thành công',
            }

        check_error_message = self.check_error_message(response.text)
        if check_error_message:
            return {
                'success': False,
                'message': html.unescape(check_error_message)
            }
        return {
            'success': False,
            'message': 'Lỗi không xác định, vui lòng thử lại!'
        }

    def get_accounts_list(self):
        payload = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://ebanking.vietabank.com.vn/accountdetailsview.html',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

        try:
            response = self.session.get("https://ebanking.vietabank.com.vn/accountsummary.html", headers=headers, data=payload, timeout=15, proxies=self.proxy)
        except:
            return
        accounts = self.extract_account_number(response.text)
        return accounts

    def get_account_details(self):
        timestamp = str(int(time.time() * 1000))
        payload = {'rqAccountDetail.account.nbrAccount': str(self.account_number),
                   'flgAction': 'getdetail',
                   '_ls': self._ss,
                   '_ss': self._ss,
                   'data_cId': timestamp}
        files = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://ebanking.vietabank.com.vn',
            'Connection': 'keep-alive',
            'Referer': 'https://ebanking.vietabank.com.vn/accountdetailsview.html',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        response = self.session.post("https://ebanking.vietabank.com.vn/accountdetailsview.html", headers=headers, data=payload, files=files, timeout=15, proxies=self.proxy)
        return response.text

    def getBalance(self):
        accounts_list = self.get_accounts_list()
        if accounts_list:
            for account in accounts_list:
                if account.get('account_number') == self.account_number:
                    return True, {
                        'account_number': self.account_number,
                        # 可用余额
                        'balance': account.get('balance') or 0,
                        # 总余额
                        'totalBalance': account.get('balance') or 0,
                    }

        _statu = self.doLogin()
        if not _statu:
            return False, '登录失败！'

        accounts_list = self.get_accounts_list()
        if accounts_list:
            for account in accounts_list:
                if account.get('account_number') == self.account_number:
                    return True, {
                        'account_number': self.account_number,
                        # 可用余额
                        'balance': account.get('balance') or 0,
                        # 总余额
                        'totalBalance': account.get('balance') or 0,
                    }
        return False, '余额获取失败！'

    def get_transactions(self, fromDate, toDate):
        url = "https://ebanking.vietabank.com.vn/accountactivityprepare.html"
        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        try:
            response = self.session.get(url, headers=headers, data=payload, timeout=15, proxies=self.proxy)
        except:
            return
        data_cId = self.extract_data_cId(response.text)
        payload = {
            'refid': '',
            'rqTrans.account.nbrAccount': str(self.account_number),
            'rqTrans.searchBy': '3',
            'rqTrans.searchTxnType': '0',
            'rqFromDate': fromDate,
            'rqToDate': toDate,
            'rqFromAmount': '',
            'rqToAmount': '',
            'rqTrans.sortBy': '0',
            'rqTrans.sortOrder': '0',
            'rqTrans.toaccount.nbrAccount': '',
            'rqTrans.page.pageNo': '1',
            'rsTrans.totalPages': '0',
            'reporttype': '',
            'flgAction': 'find',
            '_ls': '1',
            '_ss': '1',
            'data_cId': str(data_cId)
        }
        files = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://ebanking.vietabank.com.vn',
            'Connection': 'keep-alive',
            'Referer': 'https://ebanking.vietabank.com.vn/accountactivityprepare.html',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = self.session.post("https://ebanking.vietabank.com.vn/accountactivityprepare.html", headers=headers, data=payload, files=files, timeout=15, proxies=self.proxy)
            return json.loads(self.extract_transaction(response.text))
        except:
            return

    def getHistories(self, fromDate, toDate):
        try:
            data_json = self.get_transactions(fromDate, toDate)
            if data_json:
                return True, data_json
        except:
            pass

        _statu = self.doLogin()
        if not _statu:
            return False, '登录失败！'

        try:
            data_json = self.get_transactions(fromDate, toDate)
            if data_json:
                return True, data_json
        except:
            pass
        return False, '获取订单失败！'



class BANK_VAB:

    def __init__(self, username, password, account_number, is_proxy=None):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.keyanticaptcha = "b8246038ce1540888c4314a6c043dcae"
        self.session = requests.Session()
        self.tokenNo = ''
        self._ss = ''
        self.bank_code = 'VAB'
        self.proxy = None
        if is_proxy:
            self.proxy = self.getProxy(is_proxy)
        self.session.cookies.clear()
        self.session.cookies.update(self.getUserToken)

    def getProxy(self, is_proxy_str):
        ip, port, username, password = is_proxy_str.replace(' ','').split(':')
        proxies = {
            "http": f"http://{username}:{password}@{ip}:{port}",
            "https": f"http://{username}:{password}@{ip}:{port}",
        }
        return proxies

    @property
    def getUserToken(self):
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            return {}
        return json.loads(_data.get('token') or '{}')

    def updateUserInfo(self):
        data_json = self.session.cookies.get_dict()
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            _d = {
                'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code,
                'token': json.dumps(data_json),
                'req_data': json.dumps(data_json),
            }
            BankAccountCacheTable.insert_one(_d)
        else:
            BankAccountCacheTable.update_one({'uuid': _data.get('uuid')},{'$set': {
                'token': json.dumps(data_json),
                'req_data': json.dumps(data_json),
            }})

    def check_title(self, html_content):
        pattern = r'<title>(.*?)</title>'
        match = re.search(pattern, html_content)
        return match.group(1) if match else None

    def check_error_message(self, html_content):
        pattern = r'<div id="ul.errors" class="errorblock" style="color:red; ">(.*?)</div>'
        match = re.search(pattern, html_content)
        return match.group(1) if match else None

    def extract_data_cId(self, html_content):
        pattern = r'<input id="data_cId" name="data_cId" type="hidden" value="(.*)"/>'
        match = re.search(pattern, html_content)
        return match.group(1) if match else None

    def extract_transaction(self, html_content):
        pattern = r'var transHis = (.*)];'
        match = re.search(pattern, html_content)
        return match.group(1) + ']' if match else None

    def extract_account_number(self, html_content):
        pattern = r'<a href="/accountdetailsview\.html\?pid=\w+&fcid=asmp">(\d+)</a>\s*-\s*.*?<td.*?>([\d,.]+)</td>'
        matches = re.findall(pattern, html_content, re.DOTALL)
        extracted_data = []
        for match in matches:
            account_number = match[0]
            account_balance = float(match[1].replace(',', ''))
            account_info = {'account_number': account_number, 'balance': account_balance}
            extracted_data.append(account_info)
        return extracted_data or None

    def doLogin(self):
        self.session.cookies.clear()
        url = "https://ebanking.vietabank.com.vn/"
        payload = {}
        headers = {}
        try:
            response = self.session.get(url, headers=headers, data=payload, timeout=15, proxies=self.proxy)
        except:
            print(12)
            return {'success': False,'message': 'Lỗi không xác định, vui lòng thử lại!'}
        print(13)
        url = "https://ebanking.vietabank.com.vn/"
        payload = 'ipify=0.0.0.0&disable-pwd-mgr-1=disable-pwd-mgr-1&disable-pwd-mgr-2=disable-pwd-mgr-2&disable-pwd-mgr-3=disable-pwd-mgr-3&askRename=&askRenameMsg=&actionFlg=&idChannelUser=' + str(self.username) + '&password=' + urllib.parse.quote(str(self.password))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ebanking.vietabank.com.vn',
            'Connection': 'keep-alive',
            'Referer': 'https://ebanking.vietabank.com.vn/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = self.session.post(url, headers=headers, data=payload, timeout=15, proxies=self.proxy)
            print(13)
        except:
            print(14)
            return {
                'success': False,
                'message': 'Lỗi không xác định, vui lòng thử lại!'
            }
        self._ss = str(int(time.time() * 1000))
        title = self.check_title(response.text)
        print(15)
        if title == 'Tổng quan tài khoản':
            print(16)
            self.updateUserInfo()
            return {
                'success': True,
                'message': 'Đăng nhập thành công',
                'tokenNo': self.tokenNo
            }
        print(17)
        check_error_message = self.check_error_message(response.text)
        if check_error_message:
            return {
                'success': False,
                'message': html.unescape(check_error_message)
            }
        print(18)
        return {
            'success': False,
            'message': 'Lỗi không xác định, vui lòng thử lại!'
        }

    def get_accounts_list(self):
        payload = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://ebanking.vietabank.com.vn/accountdetailsview.html',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = self.session.get("https://ebanking.vietabank.com.vn/accountsummary.html", headers=headers, data=payload, timeout=15, proxies=self.proxy)
        except:
            return
        accounts = self.extract_account_number(response.text)
        return accounts

    def get_account_details(self, account_number):
        timestamp = str(int(time.time() * 1000))
        payload = {'rqAccountDetail.account.nbrAccount': str(account_number),'flgAction': 'getdetail','_ls': self._ss,'_ss': self._ss,'data_cId': timestamp}
        files = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://ebanking.vietabank.com.vn',
            'Connection': 'keep-alive',
            'Referer': 'https://ebanking.vietabank.com.vn/accountdetailsview.html',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

        response = self.session.post("https://ebanking.vietabank.com.vn/accountdetailsview.html", headers=headers, data=payload, files=files, timeout=15, proxies=self.proxy)
        return response.text

    def getBalance(self):
        accounts_list = self.get_accounts_list()
        if accounts_list:
            for account in accounts_list:
                if account.get('account_number') == self.account_number:
                    return True, {
                        'account_number': self.account_number,
                        # 可用余额
                        'balance': account.get('balance') or 0,
                        # 总余额
                        'totalBalance': account.get('balance') or 0,
                    }

        _statu = self.doLogin()
        if not _statu:
            return False, '登录失败！'

        accounts_list = self.get_accounts_list()
        if accounts_list:
            for account in accounts_list:
                if account.get('account_number') == self.account_number:
                    return True, {
                        'account_number': self.account_number,
                        # 可用余额
                        'balance': account.get('balance') or 0,
                        # 总余额
                        'totalBalance': account.get('balance') or 0,
                    }
        return False, '余额获取失败！'

    def get_transactions(self, fromDate, toDate):
        url = "https://ebanking.vietabank.com.vn/accountactivityprepare.html"
        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        response = self.session.get(url, headers=headers, data=payload, timeout=15, proxies=self.proxy)
        data_cId = self.extract_data_cId(response.text)
        payload = {'refid': '',
                   'rqTrans.account.nbrAccount': str(self.account_number),
                   'rqTrans.searchBy': '3',
                   'rqTrans.searchTxnType': '0',
                   'rqFromDate': fromDate,
                   'rqToDate': toDate,
                   'rqFromAmount': '',
                   'rqToAmount': '',
                   'rqTrans.sortBy': '0',
                   'rqTrans.sortOrder': '0',
                   'rqTrans.toaccount.nbrAccount': '',
                   'rqTrans.page.pageNo': '1',
                   'rsTrans.totalPages': '0',
                   'reporttype': '',
                   'flgAction': 'find',
                   '_ls': '1',
                   '_ss': '1',
                   'data_cId': str(data_cId)}
        files = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.100.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://ebanking.vietabank.com.vn',
            'Connection': 'keep-alive',
            'Referer': 'https://ebanking.vietabank.com.vn/accountactivityprepare.html',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        try:
            response = self.session.post("https://ebanking.vietabank.com.vn/accountactivityprepare.html", headers=headers, data=payload, files=files, proxies=self.proxy, timeout=15)
            return json.loads(self.extract_transaction(response.text))
        except:
            return 

    def getHistories(self, fromDate, toDate):
        try:
            data_json = self.get_transactions(fromDate, toDate)
            if data_json:
                return True, data_json
        except:
            pass

        _statu = self.doLogin()
        if not _statu:
            return False, '登录失败！'

        try:
            data_json = self.get_transactions(fromDate, toDate)
            if data_json:
                return True, data_json
        except:
            pass
        return False, '获取订单失败！'



# username = "0568919718"
# password = "Tay252525"
# fromDate = '25/12/2023'
# toDate = '25/12/2023'
# account_number = "00195363"
# vietabank = BANK_VAB(username, password, account_number)
#
# session_raw = vietabank.login()
# print(session_raw)
#
# # accounts_list = vietabank.get_accounts_list()
# # print(accounts_list)
#
# # balance = vietabank.get_balance()
# # print(balance)
#
# history = vietabank.get_transactions(fromDate, toDate)
# print(history)
