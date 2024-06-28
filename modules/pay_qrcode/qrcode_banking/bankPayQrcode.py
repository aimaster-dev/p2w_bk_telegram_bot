import requests, json
from PIL import Image
from pyzbar.pyzbar import decode
import base64
from io import BytesIO
from .qrcode_styled import ERROR_CORRECT_Q, QRCodeStyled,ERROR_CORRECT_L
from .qrcode_styled.pil.image import PilStyledImage

def decode_qr_code_from_url(url):
    try:
        response = requests.get(url, timeout=20)
    except:
        return
    if response.status_code != 200:
        return
    image = Image.open(BytesIO(response.content))
    decoded_objects = decode(image)
    if decoded_objects:
        return decoded_objects[0].data.decode()

    
# def mapping_bank_code(bank_code):
#     with open('banks.json','r', encoding='utf-8') as f:
#         data = json.load(f)
#     for bank in data['data']:
#         if bank['bin'] == bank_code:
#             return bank['short_name']
#     return None  # Bank code not found

def generate_qrcode(short_name,account_number,amount,desc='',account_name=''):
    if not account_name:
         param = f"{short_name}/{account_number}/{amount}/{desc}/qr_only.jpg"
    else:
        param = f"{short_name}/{account_number}/{amount}/{desc}/qr_only.jpg?accountName={account_name}"
    image_url = 'https://api.vietqr.io/'+(param)
    try:
        payload = decode_qr_code_from_url(image_url)
    except:
        return
    if not payload:
        return
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



# bank_code = "970403"
# account_number = "060282953067"
# account_name = "TRAN DUY QUANG"
# amount = "50000"
# desc = "testnd"
# qrcode_base64 = generate_qrcode(bank_code,account_number,account_name,amount,desc)
# print(qrcode_base64)
