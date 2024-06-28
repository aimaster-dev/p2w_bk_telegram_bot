from flask import session, abort
from constants import MERCHANT_USER_SESSION_KEY
from models.cms_user import CmsUserTable
from models.pay_table import MerchantTable


def current_user_data_dict():
    ''' 获取当前登录用户数据 '''
    uuid = session.get(MERCHANT_USER_SESSION_KEY)
    if not uuid:
        return {}
    user_dict = MerchantTable.find_one({'uuid': uuid})
    return user_dict


