import datetime
import hashlib, requests, re, random, shortuuid


# 生成支付二维码
def im():
    url = 'https://api.vietqr.io/v2/generate'
    header = {
        'x-client-id': '2b500bc7-ec20-44c1-807e-6f2a6213d9c4',
        'x-api-key': '04a0e117-c330-4baa-8814-639e49689b98',
    }
    accountName = 'Ngân hàng số Timo by Ban Viet Bank (Timo by Ban Viet Bank)'
    if '(' in accountName:
        accountName = str(accountName).split('(', 1)[0].strip()
    print('accountName:', accountName)
    data = {
        "accountNo": '0983147559',
        "accountName": accountName,
        "acqId": '963388',
        "amount": '',
        "addInfo": "123789",
        "format": "text",
        "template": "compact"
    }
    res = requests.post(url, data=data, headers=header)
    d = res.json()
    print(d)
    print(d.get('data').get('qrDataURL'))


def encry_md5(data):
    """MD5加密"""
    md5_object = hashlib.md5()
    md5_object.update(data.encode('utf8'))
    md5_result = md5_object.hexdigest()
    return md5_result


# 请求订单
def testOrderApi():
    url = 'https://paytest.0242.bet/api/pay'
    # url = 'https://pay2world.co/api/pay'
    data = {
        "amount":"10016",
        # "mchId":"1681954",
        "mchId":"1682499",
        "payMethod":"VNBANKQR2",
        "notifyUrl":"https://www.google.com",
        "mchOrderId":"0c9562626gfegergrgwfregreg6515656456b186a70bda4",
        # 'bankCode':'ACB',
    }
    # _sign = 'fafd95f601a80dd8f4b3bfca393dbe75'
    _sign = '0c4c9e9f521329e7578cfb186a70bda4'
    reqks = list(data.keys())
    reqks.sort()
    dataStr = ''
    for k in reqks:
        if k == 'sign':
            continue
        _v = data.get(k) or ''
        dataStr += f'&{k}={_v}'
    dataStr += '&sign=' + _sign
    print('dataStr:', dataStr)
    mtext = encry_md5(dataStr.strip('&'))
    data['sign'] = mtext
    print('data:', data)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    print(res.json())


# 代付订单
def behalfPay_func():
    url = 'https://paytest.0242.bet/api/behalfPay/bill'
    # url = 'https://pay2world.co/api/behalfPay/bill'
    data = {
        "amount":"10002","mchId":"1682499",
        "notifyUrl":"https://www.google.com","mchOrderId":"R8989greg955959595962616565258838954519",
        "bankCode":"ACB","bankAccount":"111111111","bankOwner":"ceshi"}
    _sign = '0c4c9e9f521329e7578cfb186a70bda4'
    reqks = list(data.keys())
    reqks.sort()
    dataStr = ''
    for k in reqks:
        if k == 'sign':
            continue
        _v = data.get(k) or ''
        dataStr += f'&{k}={_v}'
    dataStr += '&sign=' + _sign
    mtext = encry_md5(dataStr.strip('&'))
    data['sign'] = mtext
    print('data:', data)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    print(res.json())



def behalfPayQuery():
    url = 'https://test.pay2world.co/api/behalfPay/Query/bill'
    data = {"mchId":"1681954","mchOrderId":"WORLDPAYVN204861623888251"}
    _sign = 'fafd95f601a80dd8f4b3bfca393dbe75'
    reqks = list(data.keys())
    reqks.sort()
    dataStr = ''
    for k in reqks:
        if k == 'sign':
            continue
        _v = data.get(k) or ''
        dataStr += f'&{k}={_v}'
    dataStr += '&sign=' + _sign
    mtext = encry_md5(dataStr.strip('&'))
    data['sign'] = mtext
    print('data:', data)
    req = requests.post(url, data=data)
    print(req.text)


# 请求代付任务
def testRequets():
    url = 'https://pay2world.me/api/behalfPay/task/getTask'
    data = {
        "desktop_id":"D74435",
        "device_id":"S50115",
        "sign":"9467F2C87F3D2C939035255E0AF3EB92".lower()
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    print(res.json())


# 提交任务
def subTask():
    url = 'https://pay2world.me/api/behalfPay/task/subTask'
    data = {
        "desktop_id":"D74435",
        "device_id":"S50115",
        "sign":"9467f2c87f3d2c939035255e0af3eb92",
        "task_id": "RUyi4DPpsPjjY6tnJReP7S",
        "balanceAmount": 5000000,
        "state": "1"
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    print(res.json())


# 提交账户余额
def subBalanceAmount():
    url = 'https://pay2world.me/api/behalfPay/task/updateBalance'
    data = {
        "desktop_id":"D74435",
        "device_id":"S50115",
        "sign":"9467f2c87f3d2c939035255e0af3eb92",
        "balanceAmount": "2000",
        "bankcardAccount": "0213546887",
        "bankcardState": "1",
        'task_id': "D5Tp6XHA2uCkUCBiM29VvV",
        "msg": "",
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.text)
    print(res.json())


# testOrderApi()
behalfPay_func()
# behalfPayQuery()
# im()
# testRequets()k
# subTask()

# testOrderApi()

