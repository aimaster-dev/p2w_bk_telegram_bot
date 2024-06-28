# -*- coding: utf-8 -*-
CMS_USER_SESSION_KEY = 'cms_user_session_@13141152099'
FRONT_USER_SESSION_KEY = 'front_user_session_@13141152099'
MERCHANT_USER_SESSION_KEY = 'merchant_user_session_@13141152099'
SELECET_COLS_SESSION_KEY = 'select_cols_session_@131411520099'

# 静态文件夹名称
STATIC_FOLDER = 'static'
# 静态文件夹名称
ASSETS_FOLDER = 'assets'
# 私有目录
PRIVATE_FOLDER = 'private'
# 公开目录
PUBLIC_FOLDER = 'public'
# 导出文件夹名称
EXPORT_FOLDER = 'export_data'
# 上传文件夹
UPLOAD_FOLDER = 'upload'
# 备份文件夹
DATA_BACKUP_FOLDER = 'backup'
# 图片文件夹名称
IMAGES_FOLDER = 'images'
# 限制项目文件大小
MAX_CONTENT_LENGTH = 100 * 1024 * 1024

# 图片类型限制
IMAGES_EXTENSIONS = ['png', 'jpeg', 'jpg', 'svg', 'gif']
# 文件类型格式
FIEL_EXTENSIONS = ['txt', 'xlsx', 'csv', 'word', 'doc', 'dot']
# 音频类型格式
AUDIO_EXTENSIONS = ['wav', 'flac', 'ape', 'alac', 'mp3', 'aac', 'vorbis', 'opus']
# 视频类型格式
VIDEO_EXTENSIONS = ['wmv', 'saf', 'rm', 'rmvb', 'mp4', '3gp', 'mov', 'm4v', 'avi', 'dat', 'mkv']
# 项目上传文件限制
ALLOWED_FILENAME_EXTENSIONS = IMAGES_EXTENSIONS + FIEL_EXTENSIONS + AUDIO_EXTENSIONS+ VIDEO_EXTENSIONS

CMS_LANGUAGE_JSON =[]
class URL_PREFIX:
    """URL前缀"""
    FRONT_PREFIX = '/'
    API_PREFIX = '/api'
    COMMON_PREFIX = '/common'
    CMS_PREFIX = '/site_admin'



class EXPORT_STATU:
    """导出状态"""
    successed = 'successed'
    failed = 'failed'
    ongoing = 'ongoing'
    name_arr = (successed, failed, ongoing,)
    name_dict = {
        successed: '导出成功', failed: '导出失败', ongoing: '导出中',
    }
    class_dict = {
        successed: 'btn-success', failed: 'btn-danger', ongoing: 'btn-warning',
    }



class CODING_TYPES:
    """编码类型"""
    UTF8 = 'UTF-8'
    GB2312 = 'GB2312'
    GBK = 'GBK'
    GB18030 = 'GB18030'
    name_arr = (UTF8, GB2312, GBK, GB18030,)
    name_dict = {UTF8: 'UTF-8', GB2312: 'GB2312', GBK: 'GBK', GB18030: 'GB18030',}



class PERMISSION_ALL:
    '''权限'''
    SUPERADMIN = 'superadmin'

    # 收款管理
    BANKCARD = 'bankCard'
    zaloManage = 'zaloManage'
    viettelPayManage = 'viettelPayManage'
    momoyManage = 'momoyManage'

    tunnleManage = 'tunnleManage'
    conBankManage = 'conBankManage'
    bankScriptManage = 'bankScriptManage'

    # 商家管理
    merchantMange = 'merchantMange'
    collectionOrderMageer = 'collectionOrderMageer'
    merchantReview = 'merchantReview'
    rechargeMoney = 'rechargeMoney'
    reduceMoney = 'reduceMoney'
    loseOrderManage = 'loseOrderManage'
    withdrawManage = 'withdrawManage'
    callbackLogManage = 'callbackLogManage'

    # 财务管理
    reconciliationForm = 'reconciliationForm'
    merchantTunnleTotal = 'merchantTunnleTotal'
    bankcardForm = 'bankcardForm'
    unknownIncome = 'unknownIncome'
    merchantForm = 'merchantForm'

    # 用户管理
    adminUserManage = "adminUserManage"

    # 系统管理
    settingMange = 'settingMange'
    systemLogMange = 'systemLogMange'
    vpnManage = 'vpnManage'
    ExportFilesManage = 'ExportFilesManage'
    ApiLogView = 'ApiLogView'


    # 代付
    behalfPayOrderList = 'behalfPayOrderList'
    behalfPayCallbackLog = 'behalfPayCallbackLog'
    behalfPayScriptConfig = 'behalfPay_scriptConfig'
    behalfPayTaskList = 'behalfPayTaskList'
    behalfPayConfig = 'behalfPayConfig'
    CnBankCard = 'CnBankCard'
    WithdrawalCard = 'WithdrawalCard'
    TransactionFlow = 'TransactionFlow'

    name_arr = (
        SUPERADMIN,

        BANKCARD,
        zaloManage,
        viettelPayManage,
        momoyManage,

        merchantMange,
        collectionOrderMageer,
        merchantReview,
        rechargeMoney,
        reduceMoney,
        loseOrderManage,
        withdrawManage,
        callbackLogManage,

        reconciliationForm,
        merchantTunnleTotal,
        bankcardForm,
        unknownIncome,
        merchantForm,

        settingMange,
        systemLogMange,
        adminUserManage,
        ExportFilesManage,
        ApiLogView,

        behalfPayOrderList,
        behalfPayCallbackLog,
        behalfPayScriptConfig,
        behalfPayTaskList,
        behalfPayConfig,
        CnBankCard,
        WithdrawalCard,
        TransactionFlow,
    )
    name_dict = {
        "ROOT": {
            SUPERADMIN: '[系统]管理员权限',
        },
        "收款管理": {
            BANKCARD: "银行卡管理权限",
            zaloManage: "zalo账户管理权限",
            viettelPayManage: "viettelPay管理权限",
            momoyManage: "MOMO管理权限",
            tunnleManage: "总闸管理",
            conBankManage: "收款银行管理",
            bankScriptManage: "银行脚本管理",
        },
        "商家管理": {
            merchantMange: "商户管理权限",
            merchantReview: "商户审核管理权限",
            collectionOrderMageer: "收款订单管理权限",
            rechargeMoney: "内充管理权限",
            reduceMoney: "减少管理权限",
            loseOrderManage: "掉单管理权限",
            withdrawManage: "提现申请管理权限",
            callbackLogManage: "回调记录管理权限",
        },
        "财务管理": {
            reconciliationForm: "对账日报管理",
            merchantTunnleTotal: "商户通道报表管理",
            bankcardForm: "银行卡报表管理",
            unknownIncome: "不明收入管理",
            merchantForm: "商户报表",
        },
        "账户管理": {
            adminUserManage: "系统账户管理权限",
        },
        "系统管理": {
            settingMange: "系统设置管理权限",
            systemLogMange: "系统操作日志管理",
            vpnManage: "VPN 管理权限",
            ExportFilesManage: "导出文件管理",
            ApiLogView: "API请求日志",
        },
        "代付管理": {
            behalfPayOrderList: "代付订单",
            behalfPayCallbackLog: "代付回调记录",
            behalfPayScriptConfig: "代付脚本配置",
            behalfPayTaskList: "代付任务列表",
            behalfPayConfig: "代付配置",
            CnBankCard: "姓名检测管理",
            WithdrawalCard: "出款卡管理",
            TransactionFlow: "交易流程管理",
        },
        

    }



class OPERATION_TYPES:
    LOGIN = 'login'
    OUTLOG = 'outlog'
    ADD = 'add'
    DEL = 'del'
    UPDATE = 'update'
    ACCESS = 'access'
    ONLINE = 'online'
    BEBUSY = 'bebusy'
    OFFLINE = 'offline'
    name_arr = (LOGIN, OUTLOG, ADD, DEL, UPDATE, ACCESS, ONLINE, BEBUSY, OFFLINE)
    name_dict = {
        LOGIN: '登录',
        OUTLOG: '退出登录',
        ADD: '添加数据',
        DEL: '删除数据',
        UPDATE: '更新数据',
        ACCESS: '访问页面',
    }


class ROlE_ALL:
    SUPERADMIN = 'superadmin'
    AGENTADMIN = 'agentadmin'
    SYSTEMUSER = 'systemuser'
    ADMINISTRATOR = 'administrator'
    SYS_OUT_MONEY_USER = 'sys_out_money_user'
    OUT_MONEY_USER = 'out_money_user'

    name_arr = (
        SUPERADMIN,
        AGENTADMIN,
        SYSTEMUSER,
        ADMINISTRATOR,
        OUT_MONEY_USER,
        SYS_OUT_MONEY_USER,
    )

    name_dict = {
        SUPERADMIN: 'ROOT管理员',
        AGENTADMIN: '代理商',
        SYSTEMUSER: '代理子账户',
        ADMINISTRATOR: '普通管理员',
        SYS_OUT_MONEY_USER: '系统出款人员',
        OUT_MONEY_USER: '出款人员',
    }


# 银行卡类型
class BankCardType:
    SYSTEM_CARD = 'system_card'
    AGENTADMIN_CARD = 'agentadmin_card'

    name_arr = (SYSTEM_CARD, AGENTADMIN_CARD)

    name_dict = {
        SYSTEM_CARD: '系统卡',
        AGENTADMIN_CARD: '代理卡'
    }



# 支付通道
class PAY_METHOD:
    VNBANK = 'VNBANK'
    VNDIRECT = 'VNDIRECT'
    VNBANKQR = 'VNBANKQR'
    VNZALO = 'VNZALO'
    VNMOMO = 'VNMOMO'
    VNVTPAY = 'VNVTPAY'
    VNMO2MO = 'VNMO2MO'
    VNZA2LO = 'VNZA2LO'
    VNVT2PAY = 'VNVT2PAY'
    VNBANKQR2 = 'VNBANKQR2'
    name_arr = (VNBANKQR, VNZALO, VNMOMO, VNVTPAY, VNMO2MO, VNZA2LO, VNVT2PAY, VNBANKQR2)
    name_dict = {
        VNBANK: '越南银行转卡',
        VNDIRECT: '越南网银直连',
        VNBANKQR: '越南网银扫码',
        VNZALO: '越南ZALO pay',
        VNMOMO: '越南MOMO pay',
        VNVTPAY: '越南ViettelPay',
        VNBANKQR2: '世界付支付(网银扫码)自定义',
        VNMO2MO: '世界付支付(momopay)自定义',
        VNZA2LO: '世界付支付(zalopay)自定义',
        VNVT2PAY: '世界付支付(viettelpay)自定义',
    }



class TUNNLE_METHOD:
    '''
    通道模式
    '''
    collection = 'collection'
    name_arr = (collection)
    name_dict = {
        collection: '代收',
    }



class STATU_ALL:
    SUCCESS = 'SUCCESS'
    FAIL = 'fail'



class REQUEST_METHOD:
    GET = 'get'
    POST = 'psot'



class BILL_STATEMEN_TYPES:
    '''
    账单流水类型
    '''
    INCOME_ORDER = 'income_order'
    INCOME_ORDER_GOBACK = 'incomeOrder_goback'
    RECHARGE = 'recharge'
    REDUCE = 'reduce'
    SETTLEMENT = 'settlement'
    GOBACK_SETTLEMENT = 'gobackSettlEment'
    PAY_BEHALF = 'pay_behalf'
    PAY_BEHALF_GOBACK = 'payBehalf_goback'
    name_arr = (INCOME_ORDER, PAY_BEHALF, RECHARGE, SETTLEMENT, GOBACK_SETTLEMENT, REDUCE, INCOME_ORDER_GOBACK, PAY_BEHALF_GOBACK)
    name_dict = {
        INCOME_ORDER: '代收',
        RECHARGE: '内充',
        SETTLEMENT: '结算',
        REDUCE: '减金额',
        GOBACK_SETTLEMENT: '退回结算',
        PAY_BEHALF: "代付",
        PAY_BEHALF_GOBACK: "代付退回",
        INCOME_ORDER_GOBACK: "代收退回",
    }



class BankBillTypes:
    '''
    银行流水账单类型
    '''
    INCOME_ORDER = 'income_order'
    OUT_ORDER = 'out_order'
    name_arr = (INCOME_ORDER, OUT_ORDER)
    name_dict = {
        INCOME_ORDER: '入款',
        OUT_ORDER: '出款',
    }



class PayStatus:
    ispay = 'ispay'
    notpay = 'notpay'
    pay_timeout = 'pay_timeout'
    name_arr = (ispay, notpay, pay_timeout)
    name_dict = {
        ispay: '已支付',
        notpay: '未支付',
        pay_timeout: '支付超时',
    }


# 结算申请状态
class WITHDRAW_STATUS:
    review = 'review'
    reject = 'reject'
    success = 'success'
    name_arr = (review, reject, success)
    name_dict = {
        review: '待审核',
        reject: '拒绝',
        success: '成功',
    }



# 验证码识别模块儿
CAPTCHA_PREDICT= {
    'a7a3cc43-e35b-4c81-b961-0094a3606bcf': {
        'name': '越南VCB银行验证码',
        'pthPath': '/modules/machine_code/vietcombank.pth'
    },
    'c50033ae-e713-40b4-af55-118957eb97a4': {
        'name': 'BIDV',
        'pthPath': '/modules/machine_code/BIDV.pth',
        "content_range": "abcdefghjklmnpqrstuvwxyz123456789",
        "range_len": 33,
        "IMG_WIDTH": 145,
        "IMG_HEIGHT": 50,
        "PIC_NAME_LEN": 5,
    },
}


# 银行CODE
BANK_CODE = [
    'ACB',
    'TPB',
    'SEAB',
    'ICB',
    'MB',
    'NAB',
    'MSB',
    'VAB',
    'BAB',
    'VIETBANK',

    'VPB',
    'VCB',

    # 'BIDV',
    # 'VCB',
]
OTP_BANK_CODE = [
    'VPB',
    'VCB',
]

SC_OTP_BANK_CODE = [
    'VCB',
]

# 银行脚本
BANK_SCRIPT_ALL = {
    'pay2world_runACBtask': {
        'bank_name': 'Ngân hàng TMCP Á Châu', 'bank_code': 'ACB'
    },
    'pay2world_runTPBtask': {
        'bank_name': 'Ngân hàng TMCP Tiên Phong', 'bank_code': 'TPB'
    },
    'pay2world_runSEABtask': {
        'bank_name': 'Ngân hàng TMCP Đông Nam Á', 'bank_code': 'SEAB'
    },
    'pay2world_runICBtask': {
        'bank_name': 'Ngân hàng TMCP Công thương Việt Nam', 'bank_code': 'ICB'
    },
    'pay2world_runMBtask': {
        'bank_name': 'Ngân hàng TMCP Quân đội', 'bank_code': 'MB'
    },
    'pay2world_runNABtask': {
        'bank_name': 'Ngân hàng TMCP Nam Á', 'bank_code': 'NAB'
    },
    'pay2world_runMSBtask': {
        'bank_name': 'Ngân hàng TMCP Hàng Hải', 'bank_code': 'MSB'
    },
    'pay2world_runVABtask': {
        'bank_name': 'Ngân hàng TMCP Việt Á', 'bank_code': 'VAB'
    },
    'pay2world_runBABtask': {
        'bank_name': 'Ngân hàng TMCP Bắc Á', 'bank_code': 'BAB'
    },
    'pay2world_runVIETBANKtask': {
        'bank_name': 'Ngân hàng TMCP Việt Nam Thương Tín', 'bank_code': 'VIETBANK'
    },
    'pay2world_runVPBtask': {
        'bank_name': 'Ngân hàng TMCP Việt Nam Thịnh Vượng', 'bank_code': 'VPB'
    },
    'pay2world_runVCBtask': {
        'bank_name': 'Ngân hàng TMCP Ngoại Thương Việt Nam', 'bank_code': 'VCB'
    },
}



class ExportStatu:
    """导出状态"""
    successed = 'successed'
    failed = 'failed'
    ongoing = 'ongoing'
    name_arr = (successed, failed, ongoing,)
    name_dict = {
        successed: '导出成功', failed: '导出失败', ongoing: '导出中',
    }
    class_dict = {
        successed: 'btn-success', failed: 'btn-danger', ongoing: 'btn-warning',
    }



class CallbackState:
    '''
    回调状态
    '''
    SUCCESS = 'success'
    FAILED = 'failed'
    NOT_CALLEDBACK = 'not_calledback'
    name_arr = (SUCCESS, FAILED, NOT_CALLEDBACK)
    name_dict = {
        SUCCESS: '成功',
        FAILED: '失败',
        NOT_CALLEDBACK: '未回调',
    }


class CallbankType:
    '''
    回调类型
    '''
    MANUAL = 'manual'
    AUTOMATIC = 'automatic'
    name_arr = (MANUAL, AUTOMATIC)
    name_dict = {
        MANUAL: '手动',
        AUTOMATIC: '自动',
    }


class unusualTypes:
    '''
    异常类型
    '''
    # 重复
    REPEAT = 'repeat'
    # 实付不一致
    DIFFERENT = 'different'
    # 没订单
    NOT_NUMBER = 'not_number'
    # 收到订单未回调
    NOT_CALLEDBACK = 'not_calledback'
    # 收款卡与绑定卡不一致
    BANKCARD_DIFFERENT = 'bankcard_different'



class taskStatus:
    successed = 'successed'
    processing = 'processing'
    failed = 'failed'
    name_arr = (successed, processing, failed)
    name_dict = {
        successed: '成功',
        processing: '进行中',
        failed: '失败',
    }


# 自动脚本状态
class automaticDeviceStatus:
    d1 = 'd1'
    d2 = 'd2'
    d3 = 'd3'
    d4 = 'd4'
    name_arr = (d1, d2, d3, d4)
    name_dict = {
        d1: '空闲中',
        d2: '转账中',
        d3: '转账后余额异常',
        d4: '其它操作异常',
    }


# 支付二维码生成方式
class PAY_QRCODE_CREATE_WAY:
    OFFLINE = 'offline'
    LOCAL = 'local'
    ONLINE = 'online'
    name_all = (OFFLINE, LOCAL, ONLINE)
    name_dict = {
        OFFLINE: '离线生成',
        LOCAL: '本地生成',
        ONLINE: '在线生成',
    }



# 收款姓名检测状态
class CHECK_ANAME_STATES:
    C1 = 'c1' # 未检测
    C2 = 'c2' # 成功
    C3 = 'c3' # 失败


# 商户角色
class MERCHANT_ROLES:
    MERCHANT = 'merchat'
    SUBMERCHANT = 'submerchat'


class LOCATION_TYPE:
    TRANSIT = 'transit'
    WITHDRAW = 'withdraw'
    DEPOSIT = 'deposit'
    OTHER = 'other'
    ANOTHER = 'another'
    
    name_arr = (TRANSIT, WITHDRAW, DEPOSIT, OTHER, ANOTHER)
    name_dict = {
        TRANSIT : '中转卡',
        WITHDRAW : '出款卡',
        DEPOSIT : '入款卡',
        OTHER : '其他卡',
        ANOTHER : '另一张卡',
    }


class ORDER_STATUS:
    ORDERED = "ordered"
    COMPLETED = "completed"
    INCOMPLETED = "incompleted"

    name_arr = (ORDERED, COMPLETED, INCOMPLETED)
    name_dict = {
        ORDERED : '已订单',
        COMPLETED : '已支付',
        INCOMPLETED : '未完全支付',
    }

class ACCEPTED_STATUS:
    ACCEPTED = "accepted"
    NOT_ACCEPTED = "not_accepted"
    NOT_PROCESSED = "not_processed"
    CANCELLED = "cancalled"
    name_dict = [
        ACCEPTED, NOT_ACCEPTED, NOT_PROCESSED, CANCELLED
    ]

    name_arr = (ACCEPTED, NOT_ACCEPTED, NOT_PROCESSED, CANCELLED)
    name_dict = {
        ACCEPTED : '已接受',
        NOT_ACCEPTED : '没接受',
        NOT_PROCESSED : '未处理',
        CANCELLED : '取消了',
    }

class BEHAVIOR_TYPE:
    TRANSFER_IN = 'transfer_in'
    TRANSFER_OUT = 'transfer_out'
    OTHER_TRANSFER_IN = 'other_transfer_in'
    OTHER_TRANSFER_OUT = 'other_transfer_out'
    ISSUED = 'issued'
    name_arr = (TRANSFER_IN, TRANSFER_OUT, OTHER_TRANSFER_IN, OTHER_TRANSFER_OUT, ISSUED)
    name_dict = {
        TRANSFER_IN : "转入",
        TRANSFER_OUT : "转出",
        OTHER_TRANSFER_IN : "其他转入",
        OTHER_TRANSFER_OUT : "其他转出",
        ISSUED : "下发",
    }
class LANGUAGE:
    zh_CN = 'zh_CN' # 中文
    en_US = 'en_US' # 英文
    vi_VN = 'vi_VN' # 越南
    ba_IDN = 'ba_IDN' # 印尼
    bx_Pr = 'bx_Pr' # 巴西-葡萄牙语
    ja = 'ja' # 日语
    ko = 'ko' # 韩语
    ms = 'ms' # 马来语

    name_arr = (zh_CN, en_US, vi_VN, ba_IDN, bx_Pr, ja, ko, ms)

    name_dict = {
        zh_CN: '中文简体',
        en_US: 'English',
        vi_VN: 'Tiếng Việt',
        ba_IDN: 'bahasa Indonesia',
        bx_Pr: 'Brasil-Português',
        ja: '日本語',
        ko: '한국인',
        ms: 'Melayu',
    }
    lang_code = {
        zh_CN: "zh-CN",
        vi_VN: "vi",
        bx_Pr: "pt",
        ba_IDN: "id",
        en_US: "en",
        ja: "ja",
        ko: "ko",
        ms: "ms",
    }

LANGUAGE_HINT_ALL = [
    {
        'title': '更新语言',
        'text': '您确定要将语言更新为中文简体吗?',
        'code': LANGUAGE.zh_CN,
    },
    {
        'title': 'update language',
        'text': 'Are you sure you want to update the language to English？',
        'code': LANGUAGE.en_US,
    },
    {
        'title': 'cập nhật ngôn ngữ',
        'text': 'Bạn có chắc chắn muốn cập nhật ngôn ngữ sang tiếng Việt không?',
        'code': LANGUAGE.vi_VN,
    },
    {
        'title': 'memperbarui bahasa',
        'text': 'Apakah Anda yakin ingin memperbarui bahasa ke bahasa Indonesia?',
        'code': LANGUAGE.ba_IDN,
    },
    {
        'title': 'atualizar idioma',
        'text': 'Tem certeza de que deseja atualizar o idioma para português?',
        'code': LANGUAGE.bx_Pr,
    },
    {
        'title': '言語を更新する',
        'text': '言語を日本語に更新してもよろしいですか?',
        'code': LANGUAGE.ja,
    },
    {
        'title': '언어 업데이트',
        'text': '언어를 중국어 간체로 업데이트하시겠습니까?',
        'code': LANGUAGE.ko,
    },
    {
        'title': '马来语',
        'text': '언어를 중국어 간체로 업데이트하시겠습니까?',
        'code': LANGUAGE.ms,
    },
]