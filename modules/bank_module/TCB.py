import requests
import json
import random
import hashlib
import base64
import time
import re
from models.pay_table import BankAccountCacheTable, BankCardTable



class BANK_TCB():

    def __init__(self, username, password, account_number, is_proxy=None, otpLogin=False, codekey='', login_lock=False):
        self.code_verifier = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=96))
        self.code_challenge = self.get_code_challenge(self.code_verifier)
        self.username = username
        self.password = password
        self.account_number = account_number
        self.auth_token = None
        self.refresh_token = None
        self.identification_id = None
        self.name_account = None
        self.is_login = False
        self.fullname = None
        self.pending_transfer = []
        self.proxy = None
        self.cookies = {}
        self.bank_code = 'TCB'
        self.otpLogin = otpLogin
        self.login_lock = login_lock
        self.codekey = codekey
        self.state = self.get_imei()
        self.nonce = self.get_imei()
        self.session = requests.Session()
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
        self.auth_token = _data.get('auth_token') or None
        self.refresh_token = _data.get('refresh_token') or None
        return json.loads(_data.get('token') or '{}') or {}

    def updateUserInfo(self):
        data_json = self.session.cookies.get_dict()
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            _d = {
                'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code,
                'token': json.dumps(data_json),
                'req_data': json.dumps(data_json),
                'auth_token': self.auth_token,
                'refresh_token': self.refresh_token,
            }
            BankAccountCacheTable.insert_one(_d)
        else:
            BankAccountCacheTable.update_one({'uuid': _data.get('uuid')},{'$set': {
                'token': json.dumps(data_json),
                'req_data': json.dumps(data_json),
                'auth_token': self.auth_token,
                'refresh_token': self.refresh_token,
            }})

    def get_code_challenge(self, string):
        sha256_hash = hashlib.sha256(string.encode()).digest()
        base64_string = base64.b64encode(sha256_hash).decode()
        encrypted_string = base64_string.replace('+', '-').replace('/', '_').replace('=', '')
        return encrypted_string

    def get_imei(self):
        time = hashlib.md5(str(self.get_microtime()).encode()).hexdigest()
        text = '-'.join([time[:8], time[8:12], time[12:16], time[16:20], time[17:]])
        text = text.upper()
        return text

    def get_microtime(self):
        return int(time.time() * 1000)

    def get_user_agent(self):
        user_agent_array = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 OPR/49.0.2725.64",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  Trident/5.0)",
        "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS x86_64 9901.77.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.97 Safari/537.36"
                        ]
        return random.choice(user_agent_array)

    def get_login_url(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'identity-tcb.techcombank.com.vn',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.get_user_agent(),  # You can use the get_user_agent() function defined previously
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = f"https://identity-tcb.techcombank.com.vn/auth/realms/backbase/protocol/openid-connect/auth?client_id=tcb-web-client&redirect_uri=https%3A%2F%2Fonlinebanking.techcombank.com.vn%2Flogin&state={self.state}&response_mode=fragment&response_type=code%20id_token%20token&scope=openid&nonce={self.nonce}&ui_locales=en-US%20vi&code_challenge={self.code_challenge}&code_challenge_method=S256"
        res = self.session.get(url, headers=headers, proxies=self.proxy, timeout=15)
        pattern = r'form (.*)action="(.*)" method'
        matches = re.search(pattern, res.text)
        url = matches[2].replace("amp;", "&").replace("&&", "&")+'&kc_locale=en-US'
        return url

    def check_session(self, url):
        headers = {
           'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'identity-tcb.techcombank.com.vn',
            'Origin': 'null',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.get_user_agent()
        }
        data = {
            'oob-authn-action': 'confirmation-poll'
        }
        res = self.session.post(url, headers=headers, data=data, timeout=15, proxies=self.proxy)
        return res.text

    def is_json(self, string):
        try:
            json.loads(string)
            return True
        except json.JSONDecodeError:
            return False

    def continue_check_session(self, url):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'identity-tcb.techcombank.com.vn',
            'Origin': 'null',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.get_user_agent()
        }
        data = {
            'oob-authn-action': 'confirmation-continue'
        }
        response = self.session.post(url, headers=headers, data=data, allow_redirects=False, proxies=self.proxy, timeout=15)
        if response.status_code == 302:
            new_url = response.headers.get('Location')
            return new_url

    def get_token(self, code, url):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Host': 'identity-tcb.techcombank.com.vn',
            'Origin': 'https://onlinebanking.techcombank.com.vn',
            'Referer': 'https://onlinebanking.techcombank.com.vn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': self.get_user_agent(),
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        data = {
            'code': code,
            'grant_type': 'authorization_code',
            'client_id': 'tcb-web-client',
            'redirect_uri': url if url else 'https://onlinebanking.techcombank.com.vn/login',
            'code_verifier': self.code_verifier
        }
        url = 'https://identity-tcb.techcombank.com.vn/auth/realms/backbase/protocol/openid-connect/token'
        response = self.session.post(url, headers=headers, data=data, proxies=self.proxy, timeout=15)
        result = response.json()
        if 'access_token' in result:
            self.auth_token = result['access_token']
        return result

    def do_refresh_token(self):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Host': 'identity-tcb.techcombank.com.vn',
            'Origin': 'https://onlinebanking.techcombank.com.vn',
            'Referer': 'https://onlinebanking.techcombank.com.vn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': self.get_user_agent(),
            'Authorization': f'Bearer {self.auth_token}',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data = {
            'grant_type': 'refresh_token',
            'client_id': 'tcb-web-client',
            'refresh_token': self.refresh_token,
        }
        response = self.session.post('https://identity-tcb.techcombank.com.vn/auth/realms/backbase/protocol/openid-connect/token', data=data, headers=headers, timeout=15, proxies=self.proxy)
        result = response.json()
        if 'access_token' in result:
            self.updateUserInfo()
        return result

    def get_info(self):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Host': 'onlinebanking.techcombank.com.vn',
            'Referer': 'https://onlinebanking.techcombank.com.vn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'YOUR_USER_AGENT',  # Replace with your user agent
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Authorization': f'Bearer {self.auth_token}'
        }
        url = 'https://onlinebanking.techcombank.com.vn/api/arrangement-manager/client-api/v2/productsummary/context/arrangements?businessFunction=Product%20Summary&resourceName=Product%20Summary&privilege=view&productKindName=Current%20Account&from=0&size=1000000'
        response = self.session.get(url, headers=headers, proxies=self.proxy, timeout=15)
        if response.status_code == 200:
            result = response.json()
            return result

    def sync_balance_techcom_bank(self):
        try:
            self.refresh_token = self.do_refresh_token()
            ary_info = self.get_info()
        except:
            return
        ary_balance = {}
        for acc in ary_info:
            if 'BBAN' in acc:
                ary_balance[acc['BBAN']] = acc['availableBalance']
            else:
                return {
                    'status': 'error',
                    'msg': 'Please relogin!',
                    'code': 401
                }
        if self.account_number in ary_balance:
            self.is_login = 'Đã đăng nhập'
            balance = ary_balance[self.account_number]
            return {
                'status': 'success',
                'balance': balance,
                'code': 200
            }

    def do_login(self):
        try:
            login_url = self.get_login_url()
        except:
            return {
                'status': 'ERROR',
                'message': 'An error occurred. Please try again later!'
            }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'identity-tcb.techcombank.com.vn',
            'Origin': 'null',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.get_user_agent()
        }
        data = {
            'username': self.username,
            'password': self.password,
            'threatMetrixBrowserType': 'DESKTOP_BROWSER'
        }
        try:
            res = self.session.post(login_url, headers=headers, data=data)
            result = res.text
        except:
            return {
                'status': 'ERROR',
                'message': 'An error occurred. Please try again later!'
            }
        pattern = r'form (.*)action="(.*)" method'
        matches = re.search(pattern, res.text)
        url = matches[2].replace("amp;", "&").replace("&&", "&")+'&kc_locale=en-US'
        if 'A verification request has been sent to your registered Techcombank Mobile device' in result or 'Một yêu cầu xác thực đăng nhập đã được gửi đến thiết bị' in result:
            return {
                'status': 'PENDING',
                'url': url,
                'message': 'A verification request has been sent to your registered Techcombank Mobile device'
            }
        elif 'Incorrect username or password' in result:
            return {
                'status': 'ERROR',
                'message': 'Incorrect username or password'
            }
        elif 'Please download, register with Techcombank Mobile app and relogin.' in result:
            return {
                'status': 'ERROR',
                'message': 'Please download, register with Techcombank Mobile app and relogin.'
            }
        else:
            return {
                'status': 'ERROR',
                'message': 'An error occurred. Please try again later!'
            }

    def doLogin(self):
        login = self.do_login()
        if login['status'] == "PENDING":
            url = login['url']
            status = "PENDING"
            tryCount = 60
            while tryCount:
                time.sleep(1)
                tryCount -= 1
                try:
                    cr = self.check_session(url)
                except:
                    continue
                if self.is_json(cr):
                    check = json.loads(cr)
                    url = check['actionUrl']
                    status = check['status']
                    if status == "PENDING":
                        continue
                    else:
                        break
        else:
            BankCardTable.update_one({'username': self.username, 'account': self.account_number}, {'$set': {'login_lock': False}})
            return
        try:
            continue_check = self.continue_check_session(url)
            output_array = re.findall(r'code=(.*?)&id_token=', continue_check)
            token = self.get_token(output_array[0], "https://onlinebanking.techcombank.com.vn/login")
            if token:
                result = self.sync_balance_techcom_bank()
                self.updateUserInfo()
                BankCardTable.update_one({'username': self.username, 'account': self.account_number},{'$set': {'login_lock': False}})
                return True
            BankCardTable.update_one({'username': self.username, 'account': self.account_number},{'$set': {'login_lock': True}})
            return
        except Exception as e:
            BankCardTable.update_one({'username': self.username, 'account': self.account_number},{'$set': {'login_lock': True}})
            return

    def get_transactions(self, from_date="2022-11-15", to_date="2022-11-15"):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Host': 'onlinebanking.techcombank.com.vn',
            'Referer': 'https://onlinebanking.techcombank.com.vn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'YOUR_USER_AGENT',  # Replace with your user agent
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Authorization': f'Bearer {self.auth_token}'
        }
        url = f'https://onlinebanking.techcombank.com.vn/api/transaction-manager/client-api/v2/transactions?bookingDateGreaterThan={from_date}&bookingDateLessThan={to_date}&from=0&size=500&orderBy=bookingDate&direction=DESC'
        response = self.session.get(url, headers=headers, proxies=self.proxy, timeout=15)
        if response.status_code == 200:
            result = response.json()
            return result
        return None

    def getBalance(self):
        try:
            result = self.sync_balance_techcom_bank()
            if not result:
                BankCardTable.update_one({'username': self.username, 'account': self.account_number},{'$set': {'login_lock': False}})
                return False, ''
            return True, {
                'account_number': self.account_number,
                # 可用余额
                'balance': result.get('balance') or 0,
                # 总余额
                'totalBalance': result.get('balance') or 0,
            }
        except Exception as e:
            BankCardTable.update_one({'username': self.username, 'account': self.account_number}, {'$set': {'login_lock': False}})
            return False, ''

    def getHistories(self, start, end):
        self.do_refresh_token()
        ary_data = self.get_transactions(start, end)
        if not ary_data or ('status' in ary_data and ary_data['status'] == 401) or ('error' in ary_data and ary_data['error'] == 'Unauthorized'):
            return False, 'Please relogin!'
        return True, ary_data or []


# if __name__ == '__main__':
    # Example usage of the Techcombank class
    # user = BANK_TCB("0948798417", "Phu2023@", "19050162614019")
    #un comment login for first time, after that just call sync_balance_techcom_bank or sync_techcom_bank
    # balance = sync_balance_techcom_bank(user)
    # print(balance)
    # transactions = sync_techcom_bank(user,"2023-12-30","2023-12-30")
    # print(transactions)



'''
{'status': 'PENDING', 'url': 'https://identity-tcb.techcombank.com.vn/auth/realms/backbase/login-actions/authenticate?session_code=XHFt1OfQVsFpKrmrfzGS6mimAbXJtZMOzvQOOT8dSOM&execution=5a3daa8c-4308-4a15-9509-b41705bba6f6&client_id=tcb-web-client&tab_id=j3DxyYB1Vmo&auth_session_id=5d4112d2-b9aa-4b02-ab87-a5ce09b16324&kc_locale=en-US', 'message': 'A verification request has been sent to your registered Techcombank Mobile device'}
login success
continue_check: https://onlinebanking.techcombank.com.vn/login#state=4F7B0565-8F05-A5B7-AC0E-C0EADED0FB34445&session_state=5d4112d2-b9aa-4b02-ab87-a5ce09b16324&code=10d09dce-2321-4abd-a7e3-bd66e317c1c8.5d4112d2-b9aa-4b02-ab87-a5ce09b16324.ec45e1ad-c4ef-417a-97be-3bf554d3d0f8&id_token=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICItSUt0TzlZUVNBXy1jN08tQTNTcERfNzZGajAwT0psR3lSRVVJS1VBY2QwIn0.eyJleHAiOjE3MDYwMDk3MzMsImlhdCI6MTcwNjAwOTQzMywiYXV0aF90aW1lIjoxNzA2MDA5NDMzLCJqdGkiOiI2ODk0MTQ2MC1lZTIyLTQyNTgtYWE1My1kYWVhYzk3MTM4MzciLCJpc3MiOiJodHRwczovL2lkZW50aXR5LXRjYi50ZWNoY29tYmFuay5jb20udm4vYXV0aC9yZWFsbXMvYmFja2Jhc2UiLCJhdWQiOiJ0Y2Itd2ViLWNsaWVudCIsInN1YiI6IjM4ZWYzYTg5LTM0YzktNDgxNS1iMWNhLThmY2Q2OTRkZTlkZSIsInR5cCI6IklEIiwiYXpwIjoidGNiLXdlYi1jbGllbnQiLCJub25jZSI6IjRGN0IwNTY1LThGMDUtQTVCNy1BQzBFLUMwRUFERUQwRkIzNDQ0NSIsInNlc3Npb25fc3RhdGUiOiI1ZDQxMTJkMi1iOWFhLTRiMDItYWI4Ny1hNWNlMDliMTYzMjQiLCJhdF9oYXNoIjoicGdub1pUbllsa1dlUDBDSVFYaVczQSIsImNfaGFzaCI6IjNUMTdRYlM4b3ZHYTNYc2JDUDlLSHciLCJhY3IiOiIxIiwic19oYXNoIjoiY21mQ200ZkpOMkVuREt2ZUd3Wl90USIsInNpZCI6IjVkNDExMmQyLWI5YWEtNGIwMi1hYjg3LWE1Y2UwOWIxNjMyNCIsImN1c3RvbWVyVHlwZSI6IjIwMCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibW9iaWxlTnVtYmVyIjoiMDk0ODc5ODQxNyIsIm5hbWUiOiJMRSBIVVlOSCBEQU5HIFBIVSIsImN1c3RvbWVySWQiOiI1MDE2MjYxNCIsImNpdGl6ZW5JZCI6IjA5MjIwMDAwMzM0NyIsInByZWZlcnJlZF91c2VybmFtZSI6IjA5NDg3OTg0MTciLCJnaXZlbl9uYW1lIjoiTEUgSFVZTkggREFORyIsImxvY2FsZSI6ImVuLVVTIiwiZmFtaWx5X25hbWUiOiJQSFUiLCJlbWFpbCI6Im1pc3NpbmdAZW1haWwuY29tIn0.AWMfj3aO_vsA17-170-NEph4Swbh4l6OJgJ1CqNciDfIF95XEmou-Z2AGHj_zGbg5Tj68fBIPfWaKv0D7iHhEBpo10xmSKTdcDsuI0WDXqaQanDHezF59LZ94i3oL7DUIaZ_IpBtiiyVFc91gFlMJUtp-yxFvq_hWd7OJTNVGeL8kDoFfC6MSYnT1PE9YCC4sZbnRP6PDivz7awqh3sGqD6ipZiARx0de95XM9lYXHDkE0s3YFz91RvhWG5wNFKCoFyB9FGvdt9pGMIeyPT_ImJ3Q0Xz6mYmcuDswhZNhaj1ij33iN8kxVNzWz9TY-6SWSTH2PxkUlSE-OBGaz9mrw&access_token=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICItSUt0TzlZUVNBXy1jN08tQTNTcERfNzZGajAwT0psR3lSRVVJS1VBY2QwIn0.eyJleHAiOjE3MDYwMDk3MzMsImlhdCI6MTcwNjAwOTQzMywiYXV0aF90aW1lIjoxNzA2MDA5NDMzLCJqdGkiOiJiYzEwMmMxMS04NGQzLTQ2NTEtOThhMy1iZDIwYjcyMzhhYzAiLCJpc3MiOiJodHRwczovL2lkZW50aXR5LXRjYi50ZWNoY29tYmFuay5jb20udm4vYXV0aC9yZWFsbXMvYmFja2Jhc2UiLCJzdWIiOiIzOGVmM2E4OS0zNGM5LTQ4MTUtYjFjYS04ZmNkNjk0ZGU5ZGUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0Y2Itd2ViLWNsaWVudCIsIm5vbmNlIjoiNEY3QjA1NjUtOEYwNS1BNUI3LUFDMEUtQzBFQURFRDBGQjM0NDQ1Iiwic2Vzc2lvbl9zdGF0ZSI6IjVkNDExMmQyLWI5YWEtNGIwMi1hYjg3LWE1Y2UwOWIxNjMyNCIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiNWQ0MTEyZDItYjlhYS00YjAyLWFiODctYTVjZTA5YjE2MzI0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJ1c2VyX25hbWUiOiIwOTQ4Nzk4NDE3IiwibW9iaWxlTnVtYmVyIjoiMDk0ODc5ODQxNyIsInByZWZlcnJlZF91c2VybmFtZSI6IjA5NDg3OTg0MTciLCJnaXZlbl9uYW1lIjoiTEUgSFVZTkggREFORyIsImxvY2FsZSI6ImVuLVVTIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9ncm91cF91c2VyKFVTRVIpIiwiZGVmYXVsdC1yb2xlcy1iYWNrYmFzZSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXSwiY3VzdG9tZXJUeXBlIjoiMjAwIiwibmFtZSI6IkxFIEhVWU5IIERBTkcgUEhVIiwiY3VzdG9tZXJJZCI6IjUwMTYyNjE0IiwiY2l0aXplbklkIjoiMDkyMjAwMDAzMzQ3IiwiZmFtaWx5X25hbWUiOiJQSFUiLCJlbWFpbCI6Im1pc3NpbmdAZW1haWwuY29tIn0.N4jXLnFUoDL767-YbglIIXflLSY2n6PhxycOROohUdD2UKpnX9gd8pbo1VTvDNpsLbu_PUTUMr_uOBcUqaRhrrom3hOJGLRTHRYZgmEM62i18BMPUo92DPcH4BAK9fk9nyYC6ABB54ZiluZEc5mk2vnIfaDca-F1EQoCVSFLUn9Hyyz2vu8xB4o9Njrj7rHS_T4xf265RdwC-e0GWRuXCUbjw0vMN1m_adw0UXoxCluDL2Wth5OlPYSw-Zbr4N5FGD1zPbMcJ9h0MZkJqVFfPvBBMV7PHcDvg9iSjWF3FU52TenXO00FW-tievOWgI-BI8dUkmsle2ijtkm5sHJzhg&token_type=Bearer&expires_in=300
result: [{'id': '0ed5629c-2ff1-46a3-b812-33b9c091824e', 'legalEntityIds': ['8a03b1fa8a803d5c018a8df913342608'], 'name': 'VND-TGTT-LE HUYNH DANG PHU', 'BBAN': '19050162614019', 'currency': 'VND', 'productKindName': 'Current Account', 'productTypeName': 'Current Account', 'bankBranchCode': 'VN0010225', 'creditAccount': True, 'debitAccount': True, 'bookedBalance': 170851, 'availableBalance': 170851, 'creditLimit': 0, 'productId': '884d3580-9e0b-4cf9-9862-ae13a4a23e41', 'visible': True, 'accountOpeningDate': '2023-09-13T00:00:00Z', 'accountHolderNames': 'LE HUYNH DANG PHU', 'favorite': False, 'product': {'externalId': '1001', 'externalTypeId': '1001', 'typeName': 'Current Account', 'productKind': {'id': 1, 'externalKindId': 'kind1', 'kindName': 'Current Account', 'kindUri': 'current-account'}}, 'displayName': 'VND-TGTT-LE HUYNH DANG PHU', 'debitCards': []}]
{'status': 'success', 'balance': 170851, 'code': 200}
result: [{'id': '0ed5629c-2ff1-46a3-b812-33b9c091824e', 'legalEntityIds': ['8a03b1fa8a803d5c018a8df913342608'], 'name': 'VND-TGTT-LE HUYNH DANG PHU', 'BBAN': '19050162614019', 'currency': 'VND', 'productKindName': 'Current Account', 'productTypeName': 'Current Account', 'bankBranchCode': 'VN0010225', 'creditAccount': True, 'debitAccount': True, 'bookedBalance': 170851, 'availableBalance': 170851, 'creditLimit': 0, 'productId': '884d3580-9e0b-4cf9-9862-ae13a4a23e41', 'visible': True, 'accountOpeningDate': '2023-09-13T00:00:00Z', 'accountHolderNames': 'LE HUYNH DANG PHU', 'favorite': False, 'product': {'externalId': '1001', 'externalTypeId': '1001', 'typeName': 'Current Account', 'productKind': {'id': 1, 'externalKindId': 'kind1', 'kindName': 'Current Account', 'kindUri': 'current-account'}}, 'displayName': 'VND-TGTT-LE HUYNH DANG PHU', 'debitCards': []}]
{'status': 'success', 'balance': 170851, 'code': 200}
[{'id': '8a04a1a78d052135018d0781f5da1a4c', 'arrangementId': '0ed5629c-2ff1-46a3-b812-33b9c091824e', 'reference': 'FT23364240392986\\BNK', 'description': 'test', 'typeGroup': 'OTHERS', 'type': 'DBIT', 'category': 'Spending', 'bookingDate': '2023-12-30', 'valueDate': '2023-12-30', 'creditDebitIndicator': 'DBIT', 'transactionAmountCurrency': {'amount': '2000', 'currencyCode': 'VND'}, 'counterPartyName': 'TRAN DUY QUANG', 'counterPartyAccountNumber': '060282953067', 'counterPartyBankName': 'NGAN HANG TMCP SAI GON THUONG TIN (SACOMBANK)', 'runningBalance': 170795, 'additions': {'creditBank': 'NGAN HANG TMCP SAI GON THUONG TIN (SACOMBANK)', 'debitAcctName': 'LE HUYNH DANG PHU', 'creditAcctNo': '060282953067', 'debitBank': 'Techcombank', 'debitAcctNo': '19050162614019', 'creditAcctName': 'TRAN DUY QUANG'}, 'checkImageAvailability': 'UNAVAILABLE', 'creationTime': '2023-12-30T10:14:16+07:00', 'state': 'COMPLETED'}, {'id': '8a04a1a78d052135018d0781f5da1a4b', 'arrangementId': '0ed5629c-2ff1-46a3-b812-33b9c091824e', 'reference': 'FT23364524998908\\BNK', 'description': 'test', 'typeGroup': 'OTHERS', 'type': 'DBIT', 'category': 'Spending', 'bookingDate': '2023-12-30', 'valueDate': '2023-12-30', 'creditDebitIndicator': 'DBIT', 'transactionAmountCurrency': {'amount': '2000', 'currencyCode': 'VND'}, 'counterPartyName': 'TRAN DUY QUANG', 'counterPartyAccountNumber': '060282953067', 'counterPartyBankName': 'NGAN HANG TMCP SAI GON THUONG TIN (SACOMBANK)', 'runningBalance': 172795, 'additions': {'creditBank': 'NGAN HANG TMCP SAI GON THUONG TIN (SACOMBANK)', 'debitAcctName': 'LE HUYNH DANG PHU', 'creditAcctNo': '060282953067', 'debitBank': 'Techcombank', 'debitAcctNo': '19050162614019', 'creditAcctName': 'TRAN DUY QUANG'}, 'checkImageAvailability': 'UNAVAILABLE', 'creationTime': '2023-12-30T10:05:34+07:00', 'state': 'COMPLETED'}]
'''
