import base64, pyotp, qrcode
from python_authentiator import TOTP
from urllib.parse import urlencode
from io import BytesIO


class GooleVerifyCls():

    def __init__(self, pwd='', s_label='', account=''):
        if not pwd:
            pwd = '123456@!#$$%%&*&.......'
        self.s_label = s_label # 名称
        self.account = account # 标签/账户
        self.pwd = pwd
        self.base_uri = 'otpauth://totp/{prefix}?{ends}'

    def create_secret(self):
        g_auth = TOTP(
            origin_secret=self.pwd,
            label=self.s_label,
            account=self.account,
        )
        # 生成密钥
        secret = g_auth.generate_secret()
        return secret

    def check_goole_code(self, verifycode):
        secret_key = self.create_secret()
        t = pyotp.TOTP(str(secret_key))
        result = t.verify(verifycode)
        msg = result if result is True else False
        return msg

    def generate_qrcode(self, data):
        """二维码"""
        qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
        qr.add_data(data)
        qr.make(fit=True)
        imagel = qr.make_image()
        out = BytesIO()
        imagel.save(out, 'png')
        out.seek(0)
        qr_img = u'data:image/png;base64,%s' % base64.b64encode(out.read()).decode()
        return qr_img

    def secret_generate_qrcode(self):
        """
        生成 TOTP 配置 URI, 将其转换为二维码;
        可通过 Google Authenticator 扫码添加

        :returns: 二维码图片url
        """
        secret = self.create_secret()
        prefix = ''
        ends = {
            'secret': secret,
        }

        if self.s_label:
            prefix += self.s_label
            ends['issuer'] = self.s_label

        if self.account:
            prefix += f':{self.account}'

        totp_uri = self.base_uri.format(prefix=prefix, ends=urlencode(ends))

        # qr = qrcode.QRCode()
        # # 调用add_data，指定url。
        # qr.add_data(totp_uri)
        # # 生成二维码图像
        # img = qr.make_image()
        # # 显示图像，这个会打开一个临时文件
        # img.show()
        return self.generate_qrcode(totp_uri)

