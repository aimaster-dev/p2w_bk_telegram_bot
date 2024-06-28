from enum import Enum
from typing import Optional

TABLE = [
  0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7, 0x8108, 0x9129, 0xa14a, 0xb16b,
  0xc18c, 0xd1ad, 0xe1ce, 0xf1ef, 0x1231, 0x0210, 0x3273, 0x2252, 0x52b5, 0x4294, 0x72f7, 0x62d6,
  0x9339, 0x8318, 0xb37b, 0xa35a, 0xd3bd, 0xc39c, 0xf3ff, 0xe3de, 0x2462, 0x3443, 0x0420, 0x1401,
  0x64e6, 0x74c7, 0x44a4, 0x5485, 0xa56a, 0xb54b, 0x8528, 0x9509, 0xe5ee, 0xf5cf, 0xc5ac, 0xd58d,
  0x3653, 0x2672, 0x1611, 0x0630, 0x76d7, 0x66f6, 0x5695, 0x46b4, 0xb75b, 0xa77a, 0x9719, 0x8738,
  0xf7df, 0xe7fe, 0xd79d, 0xc7bc, 0x48c4, 0x58e5, 0x6886, 0x78a7, 0x0840, 0x1861, 0x2802, 0x3823,
  0xc9cc, 0xd9ed, 0xe98e, 0xf9af, 0x8948, 0x9969, 0xa90a, 0xb92b, 0x5af5, 0x4ad4, 0x7ab7, 0x6a96,
  0x1a71, 0x0a50, 0x3a33, 0x2a12, 0xdbfd, 0xcbdc, 0xfbbf, 0xeb9e, 0x9b79, 0x8b58, 0xbb3b, 0xab1a,
  0x6ca6, 0x7c87, 0x4ce4, 0x5cc5, 0x2c22, 0x3c03, 0x0c60, 0x1c41, 0xedae, 0xfd8f, 0xcdec, 0xddcd,
  0xad2a, 0xbd0b, 0x8d68, 0x9d49, 0x7e97, 0x6eb6, 0x5ed5, 0x4ef4, 0x3e13, 0x2e32, 0x1e51, 0x0e70,
  0xff9f, 0xefbe, 0xdfdd, 0xcffc, 0xbf1b, 0xaf3a, 0x9f59, 0x8f78, 0x9188, 0x81a9, 0xb1ca, 0xa1eb,
  0xd10c, 0xc12d, 0xf14e, 0xe16f, 0x1080, 0x00a1, 0x30c2, 0x20e3, 0x5004, 0x4025, 0x7046, 0x6067,
  0x83b9, 0x9398, 0xa3fb, 0xb3da, 0xc33d, 0xd31c, 0xe37f, 0xf35e, 0x02b1, 0x1290, 0x22f3, 0x32d2,
  0x4235, 0x5214, 0x6277, 0x7256, 0xb5ea, 0xa5cb, 0x95a8, 0x8589, 0xf56e, 0xe54f, 0xd52c, 0xc50d,
  0x34e2, 0x24c3, 0x14a0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405, 0xa7db, 0xb7fa, 0x8799, 0x97b8,
  0xe75f, 0xf77e, 0xc71d, 0xd73c, 0x26d3, 0x36f2, 0x0691, 0x16b0, 0x6657, 0x7676, 0x4615, 0x5634,
  0xd94c, 0xc96d, 0xf90e, 0xe92f, 0x99c8, 0x89e9, 0xb98a, 0xa9ab, 0x5844, 0x4865, 0x7806, 0x6827,
  0x18c0, 0x08e1, 0x3882, 0x28a3, 0xcb7d, 0xdb5c, 0xeb3f, 0xfb1e, 0x8bf9, 0x9bd8, 0xabbb, 0xbb9a,
  0x4a75, 0x5a54, 0x6a37, 0x7a16, 0x0af1, 0x1ad0, 0x2ab3, 0x3a92, 0xfd2e, 0xed0f, 0xdd6c, 0xcd4d,
  0xbdaa, 0xad8b, 0x9de8, 0x8dc9, 0x7c26, 0x6c07, 0x5c64, 0x4c45, 0x3ca2, 0x2c83, 0x1ce0, 0x0cc1,
  0xef1f, 0xff3e, 0xcf5d, 0xdf7c, 0xaf9b, 0xbfba, 0x8fd9, 0x9ff8, 0x6e17, 0x7e36, 0x4e55, 0x5e74,
  0x2e93, 0x3eb2, 0x0ed1, 0x1ef0
]

def string_to_uint8_array(content):
    # Converts a string to an array of UTF-8 byte values
    return [ord(c) for c in content]

def crc16ccitt(content):
    current = string_to_uint8_array(content)
    crc = 0xffff
    for byte in current:
        crc = (TABLE[((crc >> 8) ^ byte) & 0xff] ^ (crc << 8)) & 0xffff
    return crc


class QRProvider(Enum):
    VIETQR = 'VIETQR'
    VNPAY = 'VNPAY'


class QRProviderGUID(Enum):
    VNPAY = 'A000000775'
    VIETQR = 'A000000727'


class FieldID(Enum):
    VERSION = '00'
    INIT_METHOD = '01'
    VNPAYQR = '26'
    VIETQR = '38'
    CATEGORY = '52'
    CURRENCY = '53'
    AMOUNT = '54'
    TIP_AND_FEE_TYPE = '55'
    TIP_AND_FEE_AMOUNT = '56'
    TIP_AND_FEE_PERCENT = '57'
    NATION = '58'
    MERCHANT_NAME = '59'
    CITY = '60'
    ZIP_CODE = '61'
    ADDITIONAL_DATA = '62'
    CRC = '63'


class ProviderFieldID(Enum):
    GUID = '00'
    DATA = '01'
    SERVICE = '02'


class VietQRService(Enum):
    BY_ACCOUNT_NUMBER = 'QRIBFTTA'
    BY_CARD_NUMBER = 'QRIBFTTC'


class VietQRConsumerFieldID(Enum):
    BANK_BIN = '00'
    BANK_NUMBER = '01'


class AdditionalDataID(Enum):
    BILL_NUMBER = '01'
    MOBILE_NUMBER = '02'
    STORE_LABEL = '03'
    LOYALTY_NUMBER = '04'
    REFERENCE_LABEL = '05'
    CUSTOMER_LABEL = '06'
    TERMINAL_LABEL = '07'
    PURPOSE_OF_TRANSACTION = '08'
    ADDITIONAL_CONSUMER_DATA_REQUEST = '09'


class Provider:
    def __init__(self):
        self.field_id = None
        self.name = None
        self.guid = None
        self.service = None


class AdditionalData:
    def __init__(self):
        self.bill_number = None
        self.mobile_number = None
        self.store = None
        self.loyalty_number = None
        self.reference = None
        self.customer_label = None
        self.terminal = None
        self.purpose = None
        self.data_request = None


class Consumer:
    def __init__(self):
        self.bank_bin = None
        self.bank_number = None


class Merchant:
    def __init__(self):
        self.id = None
        self.name = None

class QRPay:
    def __init__(self, content: Optional[str] = None):
        self.isValid = True
        self.version: Optional[str] = None
        self.initMethod: Optional[str] = None
        self.provider = Provider()
        self.merchant = Merchant()
        self.consumer = Consumer()
        self.category: Optional[str] = None
        self.currency: Optional[str] = None
        self.amount: Optional[str] = None
        self.tipAndFeeType: Optional[str] = None
        self.tipAndFeeAmount: Optional[str] = None
        self.tipAndFeePercent: Optional[str] = None
        self.nation: Optional[str] = None
        self.city: Optional[str] = None
        self.zipCode: Optional[str] = None
        self.additionalData = AdditionalData()
        self.crc: Optional[str] = None
        
        if content:
            self.parse(content)
    
    def parse(self, content: str) -> None:
        if len(content) < 4:
            self.invalid()
            return
        
        # verify CRC
        crcValid = QRPay.verifyCRC(content)
        if not crcValid:
            self.invalid()
            return
        
        # parse content
        self.parseRootContent(content)
    
    def build(self) -> str:
        version = QRPay.genFieldData(FieldID.VERSION, self.version) if self.version else QRPay.genFieldData(FieldID.VERSION, '01')
        
        initMethod = QRPay.genFieldData(FieldID.INIT_METHOD, self.initMethod) if self.initMethod else QRPay.genFieldData(FieldID.INIT_METHOD, '11')
        
        guid = QRPay.genFieldData(ProviderFieldID.GUID, self.provider.guid)
        
        providerDataContent = ''
        if self.provider.guid == QRProviderGUID.VIETQR.value:
            bankBin = QRPay.genFieldData(VietQRConsumerFieldID.BANK_BIN, self.consumer.bank_bin)
            bankNumber = QRPay.genFieldData(VietQRConsumerFieldID.BANK_NUMBER, self.consumer.bank_number)
            providerDataContent = (bankBin)+(bankNumber)
        elif self.provider.guid == QRProviderGUID.VNPAY.value:
            providerDataContent = self.merchant.id or ''
        
        provider = QRPay.genFieldData(ProviderFieldID.DATA, providerDataContent)
        service = QRPay.genFieldData(ProviderFieldID.SERVICE, self.provider.service)
        providerData = QRPay.genFieldData(self.provider.field_id, guid + provider + service)
        category = QRPay.genFieldData(FieldID.CATEGORY, self.category)
        currency = QRPay.genFieldData(FieldID.CURRENCY, self.currency) if self.currency else QRPay.genFieldData(FieldID.CURRENCY, '704')
        amountStr = QRPay.genFieldData(FieldID.AMOUNT, self.amount)
        tipAndFeeType = QRPay.genFieldData(FieldID.TIP_AND_FEE_TYPE, self.tipAndFeeType)
        tipAndFeeAmount = QRPay.genFieldData(FieldID.TIP_AND_FEE_AMOUNT, self.tipAndFeeAmount)
        tipAndFeePercent = QRPay.genFieldData(FieldID.TIP_AND_FEE_PERCENT, self.tipAndFeePercent)
        nation = QRPay.genFieldData(FieldID.NATION, self.nation) if self.nation else QRPay.genFieldData(FieldID.NATION, 'VN')
        merchantName = QRPay.genFieldData(FieldID.MERCHANT_NAME, self.merchant.name)
        city = QRPay.genFieldData(FieldID.CITY, self.city)
        zipCode = QRPay.genFieldData(FieldID.ZIP_CODE, self.zipCode)
        
        buildNumber = QRPay.genFieldData(AdditionalDataID.BILL_NUMBER, self.additionalData.bill_number)
        mobileNumber = QRPay.genFieldData(AdditionalDataID.MOBILE_NUMBER, self.additionalData.mobile_number)
        storeLabel = QRPay.genFieldData(AdditionalDataID.STORE_LABEL, self.additionalData.store)
        loyaltyNumber = QRPay.genFieldData(AdditionalDataID.LOYALTY_NUMBER, self.additionalData.loyalty_number)
        reference = QRPay.genFieldData(AdditionalDataID.REFERENCE_LABEL, self.additionalData.reference)
        customerLabel = QRPay.genFieldData(AdditionalDataID.CUSTOMER_LABEL, self.additionalData.customer_label)
        terminal = QRPay.genFieldData(AdditionalDataID.TERMINAL_LABEL, self.additionalData.terminal)
        purpose = QRPay.genFieldData(AdditionalDataID.PURPOSE_OF_TRANSACTION, self.additionalData.purpose)
        dataRequest = QRPay.genFieldData(AdditionalDataID.ADDITIONAL_CONSUMER_DATA_REQUEST, self.additionalData.data_request)
        
        additionalDataContent = buildNumber + mobileNumber + storeLabel + loyaltyNumber + reference + customerLabel + terminal + purpose + dataRequest
        additionalData = QRPay.genFieldData(FieldID.ADDITIONAL_DATA, additionalDataContent)
        
        content = f"{version}{initMethod}{providerData}{category}{currency}{amountStr}{tipAndFeeType}{tipAndFeeAmount}{tipAndFeePercent}{nation}{merchantName}{city}{zipCode}{additionalData}{FieldID.CRC.value}04"
        crc = QRPay.genCRCCode(content)
        
        return content + crc
    
    @staticmethod
    def initVietQR(options: dict):
        qr = QRPay()
        qr.initMethod = '12' if options.get('amount') else '11'
        qr.provider.field_id = FieldID.VIETQR
        qr.provider.guid = QRProviderGUID.VIETQR.value
        qr.provider.name = QRProvider.VIETQR.value
        qr.provider.service = options.get('service') or VietQRService.BY_ACCOUNT_NUMBER.value
        qr.consumer.bank_bin = options.get('bankBin')
        qr.consumer.bank_number = options.get('bankNumber')
        qr.amount = options.get('amount')
        qr.additionalData.purpose = options.get('purpose')
        return qr
    
    @staticmethod
    def initVNPayQR(options: dict):
        qr = QRPay()
        qr.merchant.id = options.get('merchantId')
        qr.merchant.name = options.get('merchantName')
        qr.provider.field_id = FieldID.VNPAYQR.value
        qr.provider.guid = QRProviderGUID.VNPAY.value
        qr.provider.name = QRProvider.VNPAY.value
        qr.amount = options.get('amount')
        qr.additionalData.purpose = options.get('purpose')
        qr.additionalData.bill_number = options.get('billNumber')
        qr.additionalData.mobile_number = options.get('mobileNumber')
        qr.additionalData.store = options.get('store')
        qr.additionalData.terminal = options.get('terminal')
        qr.additionalData.loyalty_number = options.get('loyaltyNumber')
        qr.additionalData.reference = options.get('reference')
        qr.additionalData.customer_label = options.get('customerLabel')
        return qr
    
    def parseRootContent(self, content: str) -> None:
        if len(content) < 4:
            self.invalid()
            return
        
        id = content[:2]
        length = int(content[2:4])
        value = content[4:4+length]
        nextValue = content[4+length:]
        
        if len(value) != length:
            self.invalid()
            return
        
        if id == FieldID.VERSION:
            self.version = value
        elif id == FieldID.INIT_METHOD:
            self.initMethod = value
        elif id == FieldID.VIETQR or id == FieldID.VNPAYQR:
            self.provider.fieldId = id
            self.parseProviderInfo(value)
        elif id == FieldID.CATEGORY:
            self.category = value
        elif id == FieldID.CURRENCY:
            self.currency = value
        elif id == FieldID.AMOUNT:
            self.amount = value
        elif id == FieldID.TIP_AND_FEE_TYPE:
            self.tipAndFeeType = value
        elif id == FieldID.TIP_AND_FEE_AMOUNT:
            self.tipAndFeeAmount = value
        elif id == FieldID.TIP_AND_FEE_PERCENT:
            self.tipAndFeePercent = value
        elif id == FieldID.NATION:
            self.nation = value
        elif id == FieldID.MERCHANT_NAME:
            self.merchant.name = value
        elif id == FieldID.CITY:
            self.city = value
        elif id == FieldID.ZIP_CODE:
            self.zipCode = value
        elif id == FieldID.ADDITIONAL_DATA:
            self.parseAdditionalData(value)
        elif id == FieldID.CRC:
            self.crc = value
        
        if len(nextValue) > 4:
            self.parseRootContent(nextValue)
    
    def parseProviderInfo(self, content: str) -> None:
        if len(content) < 4:
            return
        
        id = content[:2]
        value = content[2:]
        nextValue = content[4:]
        
        if id == ProviderFieldID.GUID:
            self.provider.guid = value
        elif id == ProviderFieldID.DATA:
            if self.provider.guid == QRProviderGUID.VNPAY.value:
                self.provider.name = QRProvider.VNPAY.value
                self.merchant.id = value
            elif self.provider.guid == QRProviderGUID.VIETQR.value:
                self.provider.name = QRProvider.VIETQR.value
                self.parseVietQRConsumer(value)
        
        if len(nextValue) > 4:
            self.parseProviderInfo(nextValue)
    
    def parseVietQRConsumer(self, content: str) -> None:
        if len(content) < 4:
            return
        
        id = content[:2]
        value = content[2:]
        nextValue = content[4:]
        
        if id == VietQRConsumerFieldID.BANK_BIN:
            self.consumer.bank_bin = value
        elif id == VietQRConsumerFieldID.BANK_NUMBER:
            self.consumer.bank_number = value
        
        if len(nextValue) > 4:
            self.parseVietQRConsumer(nextValue)
    
    def parseAdditionalData(self, content: str) -> None:
        if len(content) < 4:
            return
        
        id = content[:2]
        value = content[2:]
        nextValue = content[4:]
        
        if id == AdditionalDataID.PURPOSE_OF_TRANSACTION:
            self.additionalData.purpose = value
        elif id == AdditionalDataID.BILL_NUMBER:
            self.additionalData.bill_number = value
        elif id == AdditionalDataID.MOBILE_NUMBER:
            self.additionalData.mobile_number = value
        elif id == AdditionalDataID.REFERENCE_LABEL:
            self.additionalData.reference = value
        elif id == AdditionalDataID.STORE_LABEL:
            self.additionalData.store = value
        elif id == AdditionalDataID.TERMINAL_LABEL:
            self.additionalData.terminal = value
        
        if len(nextValue) > 4:
            self.parseAdditionalData(nextValue)
    
    @staticmethod
    def verifyCRC(content: str) -> bool:
        checkContent = content[:-4]
        crcCode = content[-4:].upper()
        
        genCrcCode = QRPay.genCRCCode(checkContent)
        return crcCode == genCrcCode
    
    @staticmethod
    def genCRCCode(content: str) -> str:
        crcCode = hex(crc16ccitt(content))[2:].upper()
        return f"0000{crcCode}"[-4:]
    
    @staticmethod
    def sliceContent(content: str) -> dict:
        id = content[:2]
        length = int(content[2:4])
        value = content[4:4+length]
        nextValue = content[4+length:]
        
        return {"id": id, "length": length, "value": value, "nextValue": nextValue}
    
    def invalid(self) -> None:
        self.isValid = False
    
    @staticmethod
    def genFieldData(id: Optional[str] = None, value: Optional[str] = None) -> str:
        fieldId = str(id) or ''
        fieldValue = value or ''
        idLen = len(fieldId.split('.'))
        if idLen != 2 or len(fieldValue) <= 0:
            return ''
        
        length = f"00{len(fieldValue)}"[-2:]
        
        return f"{id.value}{length}{fieldValue}"
