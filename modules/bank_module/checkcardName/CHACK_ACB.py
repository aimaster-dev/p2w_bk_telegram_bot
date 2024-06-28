import requests
import json
import unidecode
from models.pay_table import BankAccountCacheTable


class ACB_CLS:

    def __init__(self, username, password, account_number, is_proxy=''):
        self.connect = None
        self.clientId = 'iuSuHYVufIUuNIREV0FB9EoLn9kHsDbm'
        self.URL = {"LOGIN": "https://apiapp.acb.com.vn/mb/auth/tokens"}
        self.password = password
        self.username = username
        self.account_number = account_number
        self.proxies = None
        if is_proxy:
            self.proxies = self.getProxy(is_proxy)
        self.token = self.getUserToken

    def getProxy(self, is_proxy_str):
        ip, port, username, password = is_proxy_str.replace(' ','').split(':')
        proxies = {
            "http": f"http://{username}:{password}@{ip}:{port}",
            "https": f"http://{username}:{password}@{ip}:{port}",
        }
        return proxies

    @property
    def getUserToken(self):
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': 'ACB'})
        if not _data:
            return
        return _data.get('token')

    def updateUserInfo(self, data_json):
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': 'ACB'})
        if not _data:
            _d = {
                'username': self.username, 'account': self.account_number, 'bank_code': 'ACB',
                'token': data_json.get('accessToken'),
                'req_data': json.dumps(data_json),
            }
            BankAccountCacheTable.insert_one(_d)
        else:
            BankAccountCacheTable.update_one({'uuid': _data.get('uuid')},{'$set': {
                'token': data_json.get('accessToken'),
                'req_data': json.dumps(data_json),
            }})
        self.token = data_json.get('accessToken')

    def handleLogin(self):
        data = {
            'clientId': self.clientId,
            'username': self.username,
            'password': self.password
        }
        return self.curl_post(self.URL["LOGIN"], data)

    def curl_get(self, url):
        try:
            headers = self.header_null()
            response = requests.get(url, headers=headers, timeout=60,proxies=self.proxies)
            result = response.json()
            return result
        except Exception as e:
            return False

    def curl_post(self, url, data=None):
        try:
            headers = self.header_null()
            response = requests.post(url, headers=headers, json=data, timeout=15,proxies=self.proxies)
            result = response.json()
            return result
        except Exception as e:
            return e

    def header_null(self):
        header = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }
        if self.token:
            header['Authorization'] = 'Bearer ' + self.token
        return header

    def mapping_bank_code(self, bank_name):
        with open('banks.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for bank in data['data']:
            if bank['shortName'].lower() == bank_name.lower():
                return bank['bin']
        return None

    def load_user(self, username):
        # Implement database queries to load user here
        pass

    def login(self):
        self.token = ''
        res = self.handleLogin()
        if 'accessToken' in res:
            print('res:', res)
            self.updateUserInfo(res)
            return {'success': True, 'msg': 'Đăng nhập thành công'}
        return {'success': False, 'msg': res['message']}

    def convert_to_uppercase_no_accents(self, text):
        no_accents = unidecode.unidecode(text)
        return no_accents.upper()

    def get_bank_name(self, ben_account_number, bank_bin):
        if not self.token:
            _Res = self.login()
            if not _Res.get('success'):
                return {'status': False, 'message': '登录失败！', 'data': {}}
        status = False
        data = {}
        url = f'https://apiapp.acb.com.vn/mb/legacy/ss/cs/bankservice/transfers/accounts/{ben_account_number}?bankCode={bank_bin}&accountNumber={self.account_number}'
        count = 0
        while True:
            bankName = self.curl_get(url)
            if bankName and 'token expired' not in str(bankName):
                data = bankName
                status = True
                message = 'Successfully'
                break
            count += 1
            if count >= 2:
                message = 'Connect false'
                break
            _Res = self.login()
        return {'status': status, 'message': message, 'data': data}

    def check_bank_name(self, account_number, account_name, bank_bin):
        get_name_from_account = self.get_bank_name(account_number, bank_bin)
        if 'data' in get_name_from_account and 'data' in get_name_from_account['data'] and 'ownerName' in get_name_from_account['data']['data']:
            input_name = self.convert_to_uppercase_no_accents(account_name).lower().strip()
            output_name = get_name_from_account['data']['data']['ownerName'].lower().strip()
            if output_name == input_name or output_name.replace(' ','') == input_name:
                return True, True
            return True, False
        return False, False


# def process_line(line):
#     parts = line.split()
#     account_name = ' '.join(parts[:-2])
#     account_number = parts[-2]
#     bank_name = parts[-1]
#     check_bank_name = acb.check_bank_name(account_number, bank_name, account_name), line
#     return check_bank_name

# username = "0338542510"
# password = "Hung9988"
# account_number="36191817"
# proxy_list = []
# acb = ACB(username, password, account_number, proxy_list)
# acb.login()
# with open('test_cases.txt', 'r',encoding="utf8") as file:
#     lines = file.readlines()
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     futures = [executor.submit(process_line, line) for line in lines]
#     for future in concurrent.futures.as_completed(futures):
#         result, line = future.result()
#         print(f'{line.strip()}, || {result}')
