import re
import time
import json
import string
import random
import requests
import datetime
from models.pay_table import BankAccountCacheTable


class VTB:

    bank_code = 'ICB'

    def __init__(self, username, password, account_number, limit=20, is_proxy=None):
        self.url = {
            'captcha': 'https://api-ipay.vietinbank.vn/api/get-captcha/',
            'login': 'https://api-ipay.vietinbank.vn/ipay/wa/signIn',
            'getCustomerDetails': 'https://api-ipay.vietinbank.vn/ipay/wa/getCustomerDetails',
            'getEntitiesAndAccounts': 'https://api-ipay.vietinbank.vn/ipay/wa/getEntitiesAndAccounts',
            'getCmsData': 'https://api-ipay.vietinbank.vn/ipay/wa/getCmsData',
            'getBillPayees': 'https://api-ipay.vietinbank.vn/ipay/wa/getBillPayees',
            'creditAccountList': 'https://api-ipay.vietinbank.vn/ipay/wa/creditAccountList',
            'getAvgAccountBal': 'https://api-ipay.vietinbank.vn/ipay/wa/getAvgAccountBal',
            'getHistTransactions': 'https://api-ipay.vietinbank.vn/ipay/wa/getHistTransactions',
            'getAccountDetails': 'https://api-ipay.vietinbank.vn/ipay/wa/getAccountDetails',
            'getCodeMapping': 'https://api-ipay.vietinbank.vn/ipay/wa/getCodeMapping',
            'napasTransfer': 'https://api-ipay.vietinbank.vn/ipay/wa/napasTransfer',
            'makeInternalTransfer': 'https://api-ipay.vietinbank.vn/ipay/wa/makeInternalTransfer',
            'getPayees': 'https://api-ipay.vietinbank.vn/ipay/wa/getPayees',
            'authenSoftOtp': 'https://api-ipay.vietinbank.vn/ipay/wa/authenSoftOtp'
        }
        self.browser_info = "Chrome-98.04758102"
        self.lang = 'vi'
        self.client_info = '127.0.0.1;MacOSProMax'
        self.timeout = 15
        self.public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLenQHmHpaqYX4IrRVM8H1uB21\nxWuY+clsvn79pMUYR2KwIEfeHcnZFFshjDs3D2ae4KprjkOFZPYzEWzakg2nOIUV\nWO+Q6RlAU1+1fxgTvEXi4z7yi+n0Zs0puOycrm8i67jsQfHi+HgdMxCaKzHvbECr\n+JWnLxnEl6615hEeMQIDAQAB\n-----END PUBLIC KEY-----"
        self.account_number = account_number
        self.ipay_id = None
        self.token_id = None
        self.username = username
        self.access_code = password
        self.captcha_id = None
        self.request_id = None
        self.customer_number = None
        self.bsb = None
        self.account_type = None
        self.currency_code = None
        self.limit = limit
        self.session_id = self.getUserToken
        self.proxy = None
        if is_proxy:
            self.proxy = self.getProxy(is_proxy)

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
            return
        return _data.get('token')

    def updateUserInfo(self, data_json):
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            _d = {
                'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code,
                'token': data_json.get('sessionId'),
                'req_data': json.dumps(data_json),
            }
            BankAccountCacheTable.insert_one(_d)
        else:
            BankAccountCacheTable.update_one({'uuid': _data.get('uuid')},{'$set': {
                'token': data_json.get('sessionId'),
                'req_data': json.dumps(data_json),
            }})
        self.session_id = data_json.get('sessionId')

    def bypass_captcha(self, svg):
        model = {
            "MCLCLCLCLCLCCLCLCLCLCLCLCCLCLCLCLCCLCLCLCLCCZMCCLCLCCLCLCCLCLCCLCZ": 0,
            "MLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLZ": 1,
            "MLLLLLLLLLLLLCLCLCCLCLCLLLLLLLLLLLLLLLLLLLLLLLLLLLLLZ": 2,
            "MCLCCLCLCCLCLCLLLLLLLLLLLCCCCCLLLLLLLLLLLLCCCCCCCCLLLLLCCCLCCLCCLCLCCZ": 3,
            "MLLLLLLLLLLLLLLLLLCLCLCCLCLCLLLLLLLLLLLLLLLLLLLLLLLLLZMLLLLLLLLLLLLLLLZMLLLZ": 4,
            "MCLCLCLCLCLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLCCLLLLLLLCLCLCZ": 5,
            "MCLCLCLCLCCCLCLCLCLCLCLCLCLCLCLCLCLCLCLCLCLCCLCLCZMLCCCCLCLCCLCZ": 6,
            "MLCLCCLCLCLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLCZ": 7,
            "MCLCLCLCCLCCLCLCLCLCCLCLCLCLCCLCCLCLCLCCLCLCCLCLCZMLCLCCCCLCZMLCCLCLCCCCLCZ": 8,
            "MLCLCLCLCLCLCCLCLCLCLCCLCLCLCLCCCCCLCLCLCLCLCLCLCLCZMLCCCCCLCLCCCCLCZ": 9
        }
        chars = {}
        matches = re.findall(r'<path fill="(.*?)" d="(.*?)"/>', svg)
        if len(matches) != 6:
            return len(matches)

        paths = [match[1] for match in matches]
        for path in paths:
            p = re.search(r"M([0-9]+)", path)
            if p:
                pattern = re.sub(r"[0-9 \.]", "", path)
                chars[int(p.group(1))] = model[pattern]

        chars = dict(sorted(chars.items()))
        return "".join(str(chars[key]) for key in chars)

    def header_null(self):
        headers = {
            "Accept-Encoding": "gzip",
            "Accept-Language": "vi-VN",
            "Accept": "application/json",
            "Cache-Control": "no-store, no-cache",
            "User-Agent": "okhttp/3.11.0"
        }
        if self.session_id:
            headers["sessionId"] = self.session_id
        return headers

    def make_body_request_json(self, params):
        if self.session_id:
            params['sessionId'] = self.session_id
        return self.encrypt_data(params)

    def encrypt_data(self, data):
        # url = "http://tingting09.com/controller/bidv/api.php?act=encrypt_viettin"
        url = 'https://encrypt.pay2world.org/api.php?act=encrypt_viettin'
        payload = json.dumps(data)
        headers = {
            'Content-Type': 'application/json',
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload, proxies=self.proxy, timeout=15)
        except:
            return
        return json.loads(response.text)

    def get_captcha(self):
        self.captcha_id = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=9))
        headers = self.header_null()
        response = requests.get(self.url['captcha'] + self.captcha_id, headers=headers, timeout=self.timeout, proxies=self.proxy)
        svg = response.text
        return self.bypass_captcha(svg)

    def generate_request_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) + '|' + str(int(datetime.datetime.now().timestamp()))

    def get_entities_and_accounts(self):
        self.request_id = self.generate_request_id()
        params = {
            'lang': self.lang,
            'requestId': self.request_id
        }
        headers = self.header_null()
        body = self.make_body_request_json(params)
        response = requests.post(self.url['getEntitiesAndAccounts'], headers=headers, data=body, timeout=self.timeout, proxies=self.proxy)
        return response.json()

    def doLogin(self):
        '''
        {'requestId': '6L80MAFJPLKW|1699204285', 'sessionId': 'EQCU32H70B', 'error': False, 'systemDate': '20231106001128', 'status': 'SUCCESS', 'customerNumber': '3023562597', 'ipayId': 'EDANKZAO', 'unreadMessages': [], 'addField2': 'Available###3023562597######huyendtt8###22/02/2023 00:00:00', 'addField3': '68038', 'tokenId': 'GWQ5JG2W', 'customerEkyc': 'N'}
        '''
        self.request_id = self.generate_request_id()
        try:
            captcha_code = self.get_captcha()
        except:
            return
        params = {
            'accessCode': self.access_code,
            'browserInfo': self.browser_info,
            'captchaCode': captcha_code,
            'captchaId': self.captcha_id,
            'clientInfo': self.client_info,
            'lang': self.lang,
            'requestId': self.request_id,
            'userName': self.username,
            'screenResolution': '554x559'
        }
        headers = self.header_null()
        body = self.make_body_request_json(params)
        response = requests.post(self.url['login'], headers=headers, data=body, timeout=self.timeout, proxies=self.proxy)
        login_josn = response.json()
        print('login_josn:', login_josn)
        if not login_josn.get('error'):
            return login_josn
        return

    def getBalance(self):
        '''
        {'requestId': 'LOTH9KZ31AAE|1699204407', 'sessionId': 'EQCU32H70B', 'error': False, 'customerType': 'P', 'customerNumber': '3023562597', 'totalAmount': 44004, 'accounts': [{'number': '106878083403', 'bsb': '68038', 'type': 'DDA', 'currencyCode': 'VND', 'status': '0', 'openDate': '22-02-2023', 'accountState': {'serviceLimits': [{'service': 'Billpay', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Closeaccount', 'transactionLimit': 0, 'dailyLimit': 0, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Eztransfer', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'Lrfrom', 'transactionLimit': 99999999999999900, 'dailyLimit': 99999999999999900, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Openda', 'transactionLimit': 0, 'dailyLimit': 0, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'Pfromtobillauto', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Pfromtocard', 'transactionLimit': 499999999, 'dailyLimit': 3000000000, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'Pfromtoext', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'Pfromtoint', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'Pstockpayment', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'Qrpay', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Repaycard', 'transactionLimit': 99999999999999900, 'dailyLimit': 99999999999999900, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Schedulefromtoext', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Schedulefromtoint', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}, {'service': 'Sellfx', 'transactionLimit': 500000000, 'dailyLimit': 3000000000, 'transactionAmountMin': 1000, 'dailyLimitUsed': 0}, {'service': 'VisaQRpay', 'transactionLimit': 100100000, 'dailyLimit': 500500000, 'transactionAmountMin': 1, 'dailyLimitUsed': 0}], 'availableBalance': 44004, 'balance': 44004}, 'relationshipType': 'A', 'relationshipTypeName': 'A|Individual', 'title': 'PHAM VAN TAN', 'entityNumber': 'CU3023562597', 'productId': '1015', 'branchName': 'CN DONG NAI - PGD LONG KHANH', 'alias': 'TANPHAM99', 'aliasStatus': '0', 'aliasStatusDesc': 'Đang hoạt động', 'aliasType': '01', 'aliasProduct': '1', 'holdAmt': '0', 'restrictionCode': 'false', 'packageAccountName': 'Smart năng động'}], 'entities': [{'title': 'PHAM VAN TAN', 'isDefault': False, 'emailAddress': '', 'number': 'CU3023562597', 'mobileNumber': '0387794341', 'type': 'P', 'defaultAccount': None, 'segmentId': 'CN01', 'segmentName': 'Khách hàng thân thiết'}]}
        '''
        if not self.session_id:
            result_json = self.doLogin()
            if not result_json:
                return False, '登录失败！'
            self.updateUserInfo(result_json)

        for c in range(2):
            result_json = self.get_entities_and_accounts()
            if not result_json.get('error') and result_json.get('accounts'):
                balance = 0
                totalBalance = 0
                for v in result_json.get('accounts'):
                    if v['number'] == self.account_number:
                        balance = int(v.get('accountState').get('availableBalance'))
                        totalBalance = int(v.get('accountState').get('balance'))
                        break

                result = {
                    # 可用余额
                    "balance": balance,
                    # 总余额
                    "totalBalance": totalBalance,
                }
                return True, result

            if c == 1:
                return False, '余额获取失败！'

            result_json = self.doLogin()
            if not result_json:
                return False, '登录失败！'
            self.updateUserInfo(result_json)

        return False, '余额获取失败！'

    def getHistories(self, start_date, end_date):
        if not self.session_id:
            result_json = self.doLogin()
            if not result_json:
                return False, '登录失败！'
            self.updateUserInfo(result_json)

        for c in range(2):
            self.request_id = self.generate_request_id()
            params = {
                'accountNumber': self.account_number,
                'endDate': end_date,
                'lang': 'vi',
                'maxResult': str(self.limit),
                'pageNumber': 0,
                'requestId': self.request_id,
                'searchFromAmt': '',
                'searchKey': '',
                'searchToAmt': '',
                'startDate': start_date,
                'tranType': ''
            }
            headers = self.header_null()
            body = self.make_body_request_json(params)
            response = requests.post(self.url['getHistTransactions'], headers=headers, data=body, timeout=self.timeout, proxies=self.proxy)
            result_json =  response.json()
            if not result_json.get('error') and 'transactions' in result_json:
                transactions = result_json.get('transactions')
                return True, transactions

            if c == 1:
                return False, ''

            result_json = self.doLogin()
            if not result_json:
                return False, '登录失败！'
            self.updateUserInfo(result_json)

        return False, ''


BANK_ICB = VTB


# username = '0387794341'
# password = 'Tan242424'
# account_number = '106878083403'
# start_date="2023-10-24"
# end_date="2023-10-26"
# vtb = VTB(username, password, account_number, limit=10)
# # response = vtb.do_login()
# # print('login :', response)
# # response = vtb.getBalance()
# # print('login :', response)
# response = vtb.getHistories(start_date, end_date)
# print('result :', response)


# clss = BANK_ICB(username='0387794341', password='Tan242424', account_number='106878083403')
# print(clss.getBalance())
# exit()
# dd = [{'currency': 'VND', 'remark': 'CT DEN:329009689629 J2257038', 'amount': '20000.00', 'balance': '46000.00', 'trxId': '680S23A0T017V41H', 'processDate': '17-10-2023 16:56:26', 'dorC': 'C', 'refType': 'HistoryRecordSequence', 'refId': '1126', 'tellerId': '1000819', 'corresponsiveAccount': '6020400661', 'corresponsiveName': 'TRAN HUU LIEM', 'channel': '28 - Transware (TWO) Switch via Banknet VPG (VTB Payment Gateway)', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGSIN - Chuyển tiền nhanh', 'sendingBankId': '970488', 'sendingBranchId': '', 'sendingBranchName': 'BIDV_NHTMCP DT va PT VN', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': 'Phi quan ly the thang 09/23 cua the 5594***7326:24.09.2023:DOCNO=2513216442:TK=106878083403', 'amount': '22000.00', 'balance': '26000.00', 'trxId': '1125', 'processDate': '25-09-2023 04:26:18', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1125', 'tellerId': None, 'corresponsiveAccount': None, 'corresponsiveName': None, 'channel': None, 'serviceBranchId': '33398', 'serviceBranchName': 'TRUNG TAM THE', 'pmtType': 'DW - Chuyển tiền trong hệ thống', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': 'Phi quan ly the thang 08/23 cua the 5594***7326:24.08.2023:DOCNO=2487980886:TK=106878083403', 'amount': '22000.00', 'balance': '48000.00', 'trxId': '1124', 'processDate': '24-09-2023 11:44:37', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1124', 'tellerId': None, 'corresponsiveAccount': None, 'corresponsiveName': None, 'channel': None, 'serviceBranchId': '33398', 'serviceBranchName': 'TRUNG TAM THE', 'pmtType': 'DW - Chuyển tiền trong hệ thống', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': 'CT DI:326703918451 anan11', 'amount': '10000.00', 'balance': '70000.00', 'trxId': '680S239157PFLLVD', 'processDate': '24-09-2023 03:18:10', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1123', 'tellerId': 'ZES', 'corresponsiveAccount': '6505217593', 'corresponsiveName': 'LIEU CAM HUNG', 'channel': '78 - Retail Internet Banking', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGS - Chuyển tiền nhanh', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '970418', 'receivingBranchId': '', 'receivingBranchName': 'BIDV_NHTMCP DT va PT VN'}, {'currency': 'VND', 'remark': 'CT DEN:326719920160 LIEU CAM HUNG Chuyen tien', 'amount': '80000.00', 'balance': '80000.00', 'trxId': '680S239156VVWXTE', 'processDate': '24-09-2023 02:57:17', 'dorC': 'C', 'refType': 'HistoryRecordSequence', 'refId': '1122', 'tellerId': '1000819', 'corresponsiveAccount': '6505217593', 'corresponsiveName': 'LIEU CAM HUNG', 'channel': '28 - Transware (TWO) Switch via Banknet VPG (VTB Payment Gateway)', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGSIN - Chuyển tiền nhanh', 'sendingBankId': '970488', 'sendingBranchId': '', 'sendingBranchName': 'BIDV_NHTMCP DT va PT VN', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': 'CT DI:326622807117 PHAM VAN TAN Chuyen tien', 'amount': '20000.00', 'balance': '0.00', 'trxId': '680S2391397UWEDP', 'processDate': '23-09-2023 22:47:03', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1121', 'tellerId': 'mobile', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'LE THI THU HUONG', 'channel': '78 - Retail Internet Banking', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGS - Chuyển tiền nhanh', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '970407', 'receivingBranchId': '', 'receivingBranchName': 'TCB_NH TMCP Ky Thuong VN'}, {'currency': 'VND', 'remark': 'CT DI:326621719268 haha2', 'amount': '10000.00', 'balance': '20000.00', 'trxId': '680S239135VXEAU2', 'processDate': '23-09-2023 21:20:47', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1120', 'tellerId': 'ZES', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'LE THI THU HUONG', 'channel': '78 - Retail Internet Banking', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGS - Chuyển tiền nhanh', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '970407', 'receivingBranchId': '', 'receivingBranchName': 'TCB_NH TMCP Ky Thuong VN'}, {'currency': 'VND', 'remark': 'CT DI:326621710978 haha2', 'amount': '10000.00', 'balance': '30000.00', 'trxId': '680S239135MJTZSU', 'processDate': '23-09-2023 21:14:27', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1119', 'tellerId': 'ZES', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'LE THI THU HUONG', 'channel': '78 - Retail Internet Banking', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGS - Chuyển tiền nhanh', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '970407', 'receivingBranchId': '', 'receivingBranchName': 'TCB_NH TMCP Ky Thuong VN'}, {'currency': 'VND', 'remark': 'CT DI:326621709932 haha', 'amount': '10000.00', 'balance': '40000.00', 'trxId': '680S239135LL5MUK', 'processDate': '23-09-2023 21:13:43', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1118', 'tellerId': 'ZES', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'LE THI THU HUONG', 'channel': '78 - Retail Internet Banking', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGS - Chuyển tiền nhanh', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '970407', 'receivingBranchId': '', 'receivingBranchName': 'TCB_NH TMCP Ky Thuong VN'}, {'currency': 'VND', 'remark': 'CT DEN:326614060535 LE THI THU HUONG chuyen FT23268129765054', 'amount': '50000.00', 'balance': '50000.00', 'trxId': '680S239135GD09TW', 'processDate': '23-09-2023 21:10:32', 'dorC': 'C', 'refType': 'HistoryRecordSequence', 'refId': '1117', 'tellerId': '1000819', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'VND-TGTT-LE THI THU HUONG', 'channel': '28 - Transware (TWO) Switch via Banknet VPG (VTB Payment Gateway)', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGSIN - Chuyển tiền nhanh', 'sendingBankId': '888899', 'sendingBranchId': '', 'sendingBranchName': 'TCB_NH TMCP Ky Thuong VN', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': 'CT DI:326522293044 PHAM VAN TAN Chuyen tien', 'amount': '50000.00', 'balance': '0.00', 'trxId': '680S23911L2VWF72', 'processDate': '22-09-2023 22:15:44', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1116', 'tellerId': 'mobile', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'LE THI THU HUONG', 'channel': '78 - Retail Internet Banking', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGS - Chuyển tiền nhanh', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '970407', 'receivingBranchId': '', 'receivingBranchName': 'TCB_NH TMCP Ky Thuong VN'}, {'currency': 'VND', 'remark': 'CT DEN:326513244874 LE THI THU HUONG chuyen FT23265648964121', 'amount': '50000.00', 'balance': '50000.00', 'trxId': '680S23911FRBPNPX', 'processDate': '22-09-2023 20:24:00', 'dorC': 'C', 'refType': 'HistoryRecordSequence', 'refId': '1115', 'tellerId': '1000819', 'corresponsiveAccount': '19050013833018', 'corresponsiveName': 'VND-TGTT-LE THI THU HUONG', 'channel': '28 - Transware (TWO) Switch via Banknet VPG (VTB Payment Gateway)', 'serviceBranchId': '68038', 'serviceBranchName': 'CN DONG NAI - PGD LONG KHANH', 'pmtType': 'RTGSIN - Chuyển tiền nhanh', 'sendingBankId': '888899', 'sendingBranchId': '', 'sendingBranchName': 'TCB_NH TMCP Ky Thuong VN', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': 'Phi quan ly the thang 07/23 cua the 5594***7326:24.07.2023:DOCNO=2462963029:TK=106878083403', 'amount': '5.00', 'balance': '0.00', 'trxId': '1113', 'processDate': '25-07-2023 04:22:43', 'dorC': 'D', 'refType': 'HistoryRecordSequence', 'refId': '1113', 'tellerId': None, 'corresponsiveAccount': None, 'corresponsiveName': None, 'channel': None, 'serviceBranchId': '33398', 'serviceBranchName': 'TRUNG TAM THE', 'pmtType': 'DW - Chuyển tiền trong hệ thống', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}, {'currency': 'VND', 'remark': '', 'amount': '5.00', 'balance': '5.00', 'trxId': '1112', 'processDate': '23-07-2023 00:40:11', 'dorC': 'C', 'refType': 'HistoryRecordSequence', 'refId': '1112', 'tellerId': None, 'corresponsiveAccount': None, 'corresponsiveName': None, 'channel': None, 'serviceBranchId': '0', 'serviceBranchName': 'Back Office Operations', 'pmtType': 'IIPD', 'sendingBankId': '', 'sendingBranchId': '', 'sendingBranchName': '', 'receivingBankId': '', 'receivingBranchId': '', 'receivingBranchName': ''}]
# for f in dd:
#     print(f)

