import requests
from PIL import Image
from .qrcode_styled import ERROR_CORRECT_Q, QRCodeStyled, ERROR_CORRECT_L
from .qrcode_styled.pil.image import PilStyledImage
from pyzbar.pyzbar import decode
import base64
from .qrcode_algorithm import QRPay
from io import BytesIO


def decode_qr_code_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve image"
    image = Image.open(BytesIO(response.content))
    decoded_objects = decode(image)
    if decoded_objects:
        return decoded_objects[0].data.decode()
    else:
        return None


def mapping_bank_code(bank_code):
    import json
    with open('banks.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for bank in data['data']:
        if bank['bin'] == bank_code:
            return bank['code']
    return None


def generate_qrcode(bank_code, account_number, account_name, amount, desc):
    qr_pay = QRPay.initVietQR({
        'bankBin': bank_code,
        'bankNumber': account_number,
        'amount': amount,
        'purpose': desc,
    })
    content = qr_pay.build()
    payload = content
    qr = QRCodeStyled(
        version=None,
        error_correction=ERROR_CORRECT_L,
        mask_pattern=None,
        image_factory=PilStyledImage,
    )
    logo = None
    qrcode = qr.get_buffer(payload, image=logo, _format='WEBP')
    base64_encoded = base64.b64encode(qrcode.getvalue())
    base64_string = base64_encoded.decode()
    base64_string = 'data:image/png;base64,%s' % base64_string
    return base64_string


# bank_code = "970436"
# account_number = "0621000456871"
# account_name = "TRAN DUY QUANG"
# amount = "555555"
# desc = "testndck"
# qrcode_base64 = generate_qrcode(bank_code, account_number, account_name, amount, desc)
# print(qrcode_base64)
