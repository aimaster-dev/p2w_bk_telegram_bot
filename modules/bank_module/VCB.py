import hashlib
import requests
import json
import base64
import random
import string
import base64
import json
import os
import time
from common_utils.lqredis import SiteRedis
from models.pay_table import BankAccountCacheTable, BankCardTable


class BANK_VCB:

    def __init__(self, username, password, account_number, otpLogin=False, codekey='', is_proxy=None, login_lock=False):
        self.keyanticaptcha = "f3a44e66302c61ffec07c80f4732baf3"
        self.file = f"data/{username}.txt"
        self.url = {
            "getCaptcha": "https://digiapp.vietcombank.com.vn/utility-service/v1/captcha/",
            "login": "https://digiapp.vietcombank.com.vn/authen-service/v1/login",
            "authen-service": "https://digiapp.vietcombank.com.vn/authen-service/v1/api-",
            "getHistories": "https://digiapp.vietcombank.com.vn/bank-service/v1/transaction-history",
            "tranferOut": "https://digiapp.vietcombank.com.vn/napas-service/v1/init-fast-transfer-via-accountno",
            "genOtpOut": "https://digiapp.vietcombank.com.vn/napas-service/v1/transfer-gen-otp",
            "genOtpIn": "https://digiapp.vietcombank.com.vn/transfer-service/v1/transfer-gen-otp",
            "confirmTranferOut": "https://digiapp.vietcombank.com.vn/napas-service/v1/transfer-confirm-otp",
            "confirmTranferIn": "https://digiapp.vietcombank.com.vn/transfer-service/v1/transfer-confirm-otp",
            "tranferIn": "https://digiapp.vietcombank.com.vn/transfer-service/v1/init-internal-transfer",
            "getBanks": "https://digiapp.vietcombank.com.vn/utility-service/v1/get-banks",
            "getAccountDeltail": "https://digiapp.vietcombank.com.vn/bank-service/v1/get-account-detail",
            "getlistAccount": "https://digiapp.vietcombank.com.vn/bank-service/v1/get-list-account-via-cif",
            "getlistDDAccount": "https://digiapp.vietcombank.com.vn/bank-service/v1/get-list-ddaccount"
        }
        self.lang = 'vi'
        self._timeout = 60
        self.DT = "Windows"
        self.OV = "10"
        self.PM = "Chrome 122.0.0.0"
        self.checkAcctPkg = "1"
        self.captcha1st = ""
        self.defaultPublicKey = "-----BEGIN PUBLIC KEY-----\n\
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAikqQrIzZJkUvHisjfu5Z\n\
CN+TLy//43CIc5hJE709TIK3HbcC9vuc2+PPEtI6peSUGqOnFoYOwl3i8rRdSaK1\n\
7G2RZN01MIqRIJ/6ac9H4L11dtfQtR7KHqF7KD0fj6vU4kb5+0cwR3RumBvDeMlB\n\
OaYEpKwuEY9EGqy9bcb5EhNGbxxNfbUaogutVwG5C1eKYItzaYd6tao3gq7swNH7\n\
p6UdltrCpxSwFEvc7douE2sKrPDp807ZG2dFslKxxmR4WHDHWfH0OpzrB5KKWQNy\n\
zXxTBXelqrWZECLRypNq7P+1CyfgTSdQ35fdO7M1MniSBT1V33LdhXo73/9qD5e5\n\
VQIDAQAB\n\
-----END PUBLIC KEY-----"
        self.clientPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCg+aN5HEhfrHXCI/pLcv2Mg01gNzuAlqNhL8ojO8KwzrnEIEuqmrobjMFFPkrMXUnmY5cWsm0jxaflAtoqTf9dy1+LL5ddqNOvaPsNhSEMmIUsrppvh1ZbUZGGW6OUNeXBEDXhEF8tAjl3KuBiQFLEECUmCDiusnFoZ2w/1iOZJwIDAQAB"
        self.clientPrivateKey = "-----BEGIN RSA PRIVATE KEY-----\n\
MIICXQIBAAKBgQCg+aN5HEhfrHXCI/pLcv2Mg01gNzuAlqNhL8ojO8KwzrnEIEuq\n\
mrobjMFFPkrMXUnmY5cWsm0jxaflAtoqTf9dy1+LL5ddqNOvaPsNhSEMmIUsrppv\n\
h1ZbUZGGW6OUNeXBEDXhEF8tAjl3KuBiQFLEECUmCDiusnFoZ2w/1iOZJwIDAQAB\n\
AoGAEGDV7SCfjHxzjskyUjLk8UL6wGteNnsdLGo8WtFdwbeG1xmiGT2c6eisUWtB\n\
GQH03ugLG1gUGqulpXtgzyUYcj0spHPiUiPDAPY24DleR7lGZHMfsnu20dyu6Llp\n\
Xup07OZdlqDGUm9u2uC0/I8RET0XWCbtOSr4VgdHFpMN+MECQQDbN5JOAIr+px7w\n\
uhBqOnWJbnL+VZjcq39XQ6zJQK01MWkbz0f9IKfMepMiYrldaOwYwVxoeb67uz/4\n\
fau4aCR5AkEAu/xLydU/dyUqTKV7owVDEtjFTTYIwLs7DmRe247207b6nJ3/kZhj\n\
gsm0mNnoAFYZJoNgCONUY/7CBHcvI4wCnwJBAIADmLViTcjd0QykqzdNghvKWu65\n\
D7Y1k/xiscEour0oaIfr6M8hxbt8DPX0jujEf7MJH6yHA+HfPEEhKila74kCQE/9\n\
oIZG3pWlU+V/eSe6QntPkE01k+3m/c82+II2yGL4dpWUSb67eISbreRovOb/u/3+\n\
YywFB9DxA8AAsydOGYMCQQDYDDLAlytyG7EefQtDPRlGbFOOJrNRyQG+2KMEl/ti\n\
Yr4ZPChxNrik1CFLxfkesoReXN8kU/8918D0GLNeVt/C\n\
-----END RSA PRIVATE KEY-----"
        # if not os.path.exists(self.file):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.sessionId = ""
        self.mobileId = ""
        self.clientId = ""
        self.cif = ""
        self.res = ""
        self.browserToken = ""
        self.browserId = ""
        self.E = ""
        self.tranId = ""
        self.browserId = hashlib.md5(self.username.encode()).hexdigest()
        #     self.save_data()
        # else:
        #     self.parse_data()
        self.bank_code = 'VCB'
        self.codekey = codekey
        self.otpLogin = otpLogin
        self.login_lock = login_lock
        self.proxy = None
        if is_proxy:
            self.proxy = self.getProxy(is_proxy)
        self.getUserToken()

    def getProxy(self, is_proxy_str):
        ip, port, username, password = is_proxy_str.replace(' ','').split(':')
        proxies = {
            "http": f"http://{username}:{password}@{ip}:{port}",
            "https": f"http://{username}:{password}@{ip}:{port}",
        }
        return proxies

    def getUserToken(self):
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            return {}
        _data_json = json.loads(_data.get('token') or '{}')
        self.username = _data_json.get('username', '')
        self.password = _data_json.get('password', '')
        self.account_number = _data_json.get('account_number', '')
        self.sessionId = _data_json.get('sessionId', '')
        self.mobileId = _data_json.get('mobileId', '')
        self.clientId = _data_json.get('clientId', '')
        self.token = _data_json.get('token', '')
        self.accessToken = _data_json.get('accessToken', '')
        self.authToken = _data_json.get('authToken', '')
        self.cif = _data_json.get('cif', '')
        self.res = _data_json.get('res', '')
        self.tranId = _data_json.get('tranId', '')
        self.browserToken = _data_json.get('browserToken', '')
        self.browserId = _data_json.get('browserId', '')
        self.E = _data_json.get('E', '')

    def updateUserInfo(self):
        _data_json = {
            'username': self.username,
            'password': self.password,
            'account_number': self.account_number,
            'sessionId': self.sessionId,
            'mobileId': self.mobileId,
            'clientId': self.clientId,
            'cif': self.cif,
            'E': self.E,
            'res': self.res,
            'tranId': self.tranId,
            'browserToken': self.browserToken,
            'browserId': self.browserId,
        }
        _data = BankAccountCacheTable.find_one({'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code})
        if not _data:
            _d = {
                'username': self.username, 'account': self.account_number, 'bank_code': self.bank_code,
                'token': json.dumps(_data_json),
            }
            BankAccountCacheTable.insert_one(_d)
        else:
            BankAccountCacheTable.update_one({'uuid': _data.get('uuid')},{'$set': {
                'token': json.dumps(_data_json),
            }})

    def createTaskCaptcha(self, base64_img):
        url = "https://api.anti-captcha.com/createTask"
        payload = json.dumps({
        "clientKey": self.keyanticaptcha,
        "task": {
            "type": "ImageToTextTask",
            "body": base64_img,
            "phrase": False,
            "case": False,
            "numeric": 0,
            "math": False,
            "minLength": 0,
            "maxLength": 0
        },
        "softId": 0
        })
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, timeout=15)
        return response.text

    def checkProgressCaptcha(self, task_id):
        url = 'https://api.anti-captcha.com/getTaskResult'
        data = {
            "clientKey": self.keyanticaptcha,
            "taskId": task_id
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_json = json.loads(response.text)
        if response_json["status"] != "ready":
            time.sleep(1)
            return self.checkProgressCaptcha(task_id)
        return response_json["solution"]["text"]

    def solveCaptcha(self):
        captchaToken = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
        url = self.url['getCaptcha'] + captchaToken
        response = requests.get(url, timeout=15, proxies=self.proxy)
        base64_captcha_img = base64.b64encode(response.content).decode('utf-8')
        taskID = self.createTaskCaptcha(base64_captcha_img)
        captchaText = self.checkProgressCaptcha(json.loads(taskID)['taskId'])
        return {"status": True, "key": captchaToken, "captcha": captchaText}

    def encrypt_data(self, data):
        # url = "http://apigate.vn/vietcombank/encrypt"
        url = 'https://tcbcp.pay2world.org/vietcombank/encrypt'
        print('url:', url)
        payload = json.dumps(data)
        headers = {
        'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return json.loads(response.text)

    def decrypt_data(self, cipher):
        # url = "http://apigate.vn/vietcombank/decrypt"
        url = "https://tcbcp.pay2world.org/vietcombank/decrypt"
        payload = json.dumps(cipher)
        headers = {
        'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return json.loads(response.text)

    def curlPost(self, url, data):
        encryptedData = self.encrypt_data(data)
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'digiapp.vietcombank.com.vn',
            'Origin': 'https://vcbdigibank.vietcombank.com.vn',
            'Referer': 'https://vcbdigibank.vietcombank.com.vn/',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'X-Channel': 'Web'
        }
        response = requests.post(url, headers=headers, data=json.dumps(encryptedData), timeout=15, proxies=self.proxy)
        result = self.decrypt_data(response.json())
        return result

    def checkBrowser(self, type=1):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "mid": 3008,
            "cif": "",
            "clientId": "",
            "mobileId": "",
            "sessionId": "",
            "browserToken": self.browserToken,
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3008", param)
        if "tranId" in result["transaction"]:
            return self.chooseOtpType(result["transaction"]["tranId"], type)
        return {'success': False,'message': "checkBrowser failed","param": param,'data': result or ""}

    def chooseOtpType(self, tranID, type=1):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "mid": 3010,
            "cif": "",
            "clientId": "",
            "mobileId": "",
            "sessionId": "",
            "browserToken": self.browserToken,
            "tranId": tranID,
            "type": type,  # 1 la sms,5 la smart
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3010", param)
        if result["code"] == "00":
            self.tranId = tranID
            self.updateUserInfo()
            return {
                'success': True,
                'message': "ok",
                "result": {
                    "browserToken": self.browserToken,
                    "tranId": result.get("tranId", ""),
                    "challenge": result.get("challenge", "")
                },
                "param": param,
                'data': result or ""
            }
        return {'success': False,'message': result["des"],"param": param,'data': result or ""}

    def submitOtpLogin(self, otp):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "mid": 3011,
            "cif": "",
            "clientId": "",
            "mobileId": "",
            "sessionId": "",
            "browserToken": self.browserToken,
            "tranId": self.tranId,
            "otp": otp,
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3011", param)
        if result["code"] == "00":
            self.sessionId = result["sessionId"]
            self.mobileId = result["userInfo"]["mobileId"]
            self.clientId = result["userInfo"]["clientId"]
            self.cif = result["userInfo"]["cif"]
            session = {"sessionId": self.sessionId, "mobileId": self.mobileId, "clientId": self.clientId, "cif": self.cif}
            self.res = result
            self.updateUserInfo()
            sv = self.saveBrowser()
            if sv["code"] == "00":
                return {'success': True,'message': "success","d": sv,'session': session,'data': result or ""}
            return {'success': False,'message': sv["des"],"param": param,'data': sv or ""}
        return {'success': False,'message': result["des"],"param": param,'data': result or ""}

    def saveBrowser(self):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": "",
            "browserId": self.browserId,
            "browserName": "Chrome 111.0.0.0",
            "lang": self.lang,
            "mid": 3009,
            "cif": self.cif,
            "clientId": self.clientId,
            "mobileId": self.mobileId,
            "sessionId": self.sessionId,
            "user": self.username
        }
        result = self.curlPost(self.url['authen-service'] + "3009", param)
        return result

    def login1(self):
        solveCaptcha = self.solveCaptcha()
        if not solveCaptcha["status"]:
            return {'success': False,'message': "验证码获取失败！"}
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "captchaToken": solveCaptcha["key"],
            "captchaValue": solveCaptcha["captcha"],
            "checkAcctPkg": self.checkAcctPkg,
            "lang": self.lang,
            "mid": 6,
            "password": self.password,
            "user": self.username
        }
        result = self.curlPost(self.url['login'], param)
        if result["code"] == '00':
            self.sessionId = result["sessionId"]
            self.mobileId = result["userInfo"]["mobileId"]
            self.clientId = result["userInfo"]["clientId"]
            self.cif = result["userInfo"]["cif"]
            session = {"sessionId": self.sessionId, "mobileId": self.mobileId, "clientId": self.clientId, "cif": self.cif}
            self.updateUserInfo()
            return {'success': True,'message': "success",'session': session,'data': result or ""}
        elif result["code"] == '20231' and result["mid"] == '6':
            self.browserToken = result["browserToken"]
            return self.checkBrowser(5)
        return {'success': False,'message': result["des"],"param": param,'data': result or ""}

    def parseData(self):
        with open(f"data/{self.username}.txt", "r") as file:
            data = json.load(file)
            self.username = data["username"]
            self.password = data["password"]
            self.account_number = data.get("account_number", "")
            self.sessionId = data.get("sessionId", "")
            self.mobileId = data.get("mobileId", "")
            self.clientId = data.get("clientId", "")
            self.token = data.get("token", "")
            self.accessToken = data.get("accessToken", "")
            self.authToken = data.get("authToken", "")
            self.cif = data.get("cif", "")
            self.res = data.get("res", "")
            self.tranId = data.get("tranId", "")
            self.browserToken = data.get("browserToken", "")
            self.browserId = data.get("browserId", "")
            self.E = data.get("E", "")

    def getE(self):
        ahash = hashlib.md5(self.username.encode()).hexdigest()
        imei = '-'.join([ahash[i:i+4] for i in range(0, len(ahash), 4)])
        return imei.upper()

    def getCaptcha(self):
        captchaToken = ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
        url = self.url['getCaptcha'] + captchaToken
        response = requests.get(url)
        result = base64.b64encode(response.content).decode('utf-8')
        return result

    def getBalance(self):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "browserId": self.browserId,
            "E": self.getE() or "",
            "mid": 8,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        try:
            result = self.curlPost(self.url['getlistAccount'], param)
            if result and result.get('des') == 'Success':
                result = {
                    # 可用余额
                    "balance": float(result.get('DDAccounts')[0].get('availableBalance')) or 0,
                    # 总余额
                    "totalBalance": float(result.get('DDAccounts')[0].get('availableBalance')) or 0,
                }
                return True, result
        except:
            pass
        
        _res = self.doLogin()
        if not _res:
            return False, '登录失败！'
        try:
            result = self.curlPost(self.url['getlistAccount'], param)
            if result and result.get('des') == 'Success':
                result = {
                    # 可用余额
                    "balance": float(result.get('DDAccounts')[0].get('availableBalance')) or 0,
                    # 总余额
                    "totalBalance": float(result.get('DDAccounts')[0].get('availableBalance')) or 0,
                }
                return True, result
        except:
            pass
        return False, '余额获取失败！'

    def getlistDDAccount(self):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "browserId": self.browserId,
            "E": self.getE() or "",
            "mid": 35,
            "cif": self.cif,
            "serviceCode": "0551",
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['getlistDDAccount'], param)
        return result

    def getAccountDeltail(self):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "accountNo": self.account_number,
            "accountType": "D",
            "mid": 13,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['getAccountDeltail'], param)
        return result

    def getHistories(self, fromDate="16/06/2023", toDate="16/06/2023", account_number='', page=0):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "accountNo": account_number or self.account_number,
            "accountType": "D",
            "fromDate": fromDate,
            "toDate": toDate,
            "lang": self.lang,
            "pageIndex": page,
            "lengthInPage": 100,
            "stmtDate": "",
            "stmtType": "",
            "mid": 14,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        try:
            result = self.curlPost(self.url['getHistories'], param)
            if result and result.get('des') == 'success':
                return True, result.get('transactions')
        except:
            pass

        _res = self.doLogin()
        if not _res:
            return False, '登录失败！'

        try:
            result = self.curlPost(self.url['getHistories'], param)
            if result and result.get('des') == 'success':
                return True, result.get('transactions')
        except:
            pass
        return False, '历史订单获取失败！'

    def getBanks(self):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "fastTransfer": "1",
            "mid": 23,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['getBanks'], param)
        return result

    def createTranferOutVietCombank(self, bankCode, account_number, amount, message):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": self.getE() or "",
            "browserId": self.browserId,
            "lang": self.lang,
            "debitAccountNo": self.account_number,
            "creditAccountNo": account_number,
            "creditBankCode": bankCode,
            "amount": amount,
            "feeType": 1,
            "content": message,
            "ccyType": "1",
            "mid": 62,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['tranferOut'], param)
        return result

    def createTranferInVietCombank(self, account_number, amount, message):
        param = {
            "DT": self.DT,
            "OV": self.OV,
            "PM": self.PM,
            "E": "",
            "browserId": self.browserId,
            "lang": self.lang,
            "debitAccountNo": self.account_number,
            "creditAccountNo": account_number,
            "amount": amount,
            "activeTouch": 0,
            "feeType": 1,
            "content": message,
            "ccyType": "",
            "mid": 16,
            "cif": self.cif,
            "user": self.username,
            "mobileId": self.mobileId,
            "clientId": self.clientId,
            "sessionId": self.sessionId
        }
        result = self.curlPost(self.url['tranferIn'], param)
        return result

    def genOtpTranFer(self, tranId, type="OUT", otpType=5):
        if otpType == 1:
            solveCaptcha = self.solveCaptcha()
            if not solveCaptcha["status"]:
                return solveCaptcha
            param = {
                "DT": self.DT,
                "OV": self.OV,
                "PM": self.PM,
                "E": self.getE() or "",
                "lang": self.lang,
                "tranId": tranId,
                "type": otpType,  # 1 là SMS,5 là smart otp
                "captchaToken": solveCaptcha["key"],
                "captchaValue": solveCaptcha["captcha"],
                "browserId": self.browserId,
                "mid": 17,
                "cif": self.cif,
                "user": self.username,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }
        else:
            param = {
                "DT": self.DT,
                "OV": self.OV,
                "PM": self.PM,
                "E": self.getE() or "",
                "lang": self.lang,
                "tranId": tranId,
                "type": otpType,  # 1 là SMS,5 là smart otp
                "mid": 17,
                "browserId": self.browserId,
                "cif": self.cif,
                "user": self.username,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }

        if type == "IN":
            result = self.curlPost(self.url['genOtpIn'], param)
        else:
            result = self.curlPost(self.url['genOtpOut'], param)
        return result

    def confirmTranfer(self, tranId, challenge, otp, type="OUT", otpType=5):
        if otpType == 5:
            param = {
                "DT": self.DT,
                "OV": self.OV,
                "PM": self.PM,
                "E": self.getE() or "",
                "lang": self.lang,
                "tranId": tranId,
                "otp": otp,
                "challenge": challenge,
                "mid": 18,
                "cif": self.cif,
                "user": self.username,
                "browserId": self.browserId,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }
        else:
            param = {
                "DT": self.DT,
                "OV": self.OV,
                "PM": self.PM,
                "E": self.getE() or "",
                "browserId": self.browserId,
                "lang": self.lang,
                "tranId": tranId,
                "otp": otp,
                "challenge": challenge,
                "mid": 18,
                "cif": self.cif,
                "user": self.username,
                "mobileId": self.mobileId,
                "clientId": self.clientId,
                "sessionId": self.sessionId
            }

        if type == "IN":
            result = self.curlPost(self.url['confirmTranferIn'], param)
        else:
            result = self.curlPost(self.url['confirmTranferOut'], param)
        return result

    def doLogin(self):
        try:
            get_otp = self.login1()
        except:
            return
        if "data" in get_otp and 'mid' in get_otp.get('data') and get_otp.get('data').get('mid') == '3010':
            if not self.login_lock:
                BankCardTable.update_one({'username': self.username, 'account': self.account_number}, {'$set': {'login_lock': True}})
                self.login_lock = True
            if not self.otpLogin:
                return
            challenge = get_otp.get('data').get('challenge')
            if not challenge:
                return
            data_json = SiteRedis.get(self.codekey)
            if not data_json:
                return
            data_json = json.loads(data_json.decode())
            data_json['state'] = 'getOtpcode'
            data_json['challenge'] = str(challenge).replace(' ','').replace('/t','')
            SiteRedis.set(self.codekey, json.dumps(data_json), expire=60)
            tryCount = 60
            while tryCount:
                time.sleep(1)
                tryCount -= 1
                data_json = SiteRedis.get(self.codekey)
                if not data_json:
                    return
                data_json = json.loads(data_json.decode())
                otpcode = data_json.get('otpcode')
                if data_json.get('state') != 'sendOtpcode' or not otpcode:
                    continue
                verify_otp = self.submitOtpLogin(otpcode)
                if "success" in verify_otp and verify_otp["success"] == True and 'd' in verify_otp:
                    self.updateUserInfo()
                    data_json['state'] = 'success'
                    SiteRedis.set(self.codekey, json.dumps(data_json), expire=60)
                    BankCardTable.update_one({'username': self.username, 'account': self.account_number}, {'$set': {'login_lock': False}})
                    self.login_lock = False
                    return True
                data_json['state'] = 'error'
                data_json['msg'] = f"OTP verification failed: {verify_otp.get('des')}"
            data_json['state'] = 'error'
            data_json['msg'] = f"OTP 登录超时！"
            SiteRedis.set(self.codekey, json.dumps(data_json), expire=60)
            return

        _cc = {}
        _cc['state'] = 'success'
        SiteRedis.set(self.codekey, json.dumps(_cc), expire=60)
        if self.login_lock:
            BankCardTable.update_one({'username': self.username, 'account': self.account_number},{'$set': {'login_lock': False}})
        return True



# username = '0393512807'
# password = 'Dieng2299@'
# account_number="1039434719"
# vcb = BANK_VAB(username, password, account_number)
#
# # OTP is required first login only, then youn can call action without it after login
# get_otp = vcb.login1()
# print('get_otp:', get_otp)
# if "data" in get_otp and 'mid' in get_otp["data"] and get_otp["data"]['mid'] == '3010':
#     otp = input("challenge_CODE:" + get_otp["data"]['challenge'] + " | Enter SMART OTP: ")
#     verify_otp = vcb.submitOtpLogin(otp)
#     print(verify_otp)
#     if "success" in verify_otp and verify_otp["success"] == True and 'd' in verify_otp:
#         print('ACTIVE SUCCESSFULL')
#     else:
#         print(f"OTP verification failed: {verify_otp['des']}")
#
# # OTP is required first login only, then youn can call action without it after login
# result = vcb.getHistories("05/01/2024", "14/01/2024", account_number, 0)
# print('12:', result)

# print(vcb.getlistAccount())
# print(vcb.getHistories())
