import datetime
import json
from flask import session, current_app
from constants import CMS_USER_SESSION_KEY
from models.cms_user import CmsUserTable
from models.cms_table import SiteConfigTable
from common_utils.lqredis import SiteRedis



def current_admin_data_dict():
    ''' 获取后台当前登录用户数据 '''
    uuid = session.get(CMS_USER_SESSION_KEY)
    if not uuid:
        return {}
    user_dict = CmsUserTable.find_one({'uuid': uuid})
    return user_dict



def check_front_domain():
    ''' 检测网站前端域名 '''
    # if not hasattr(SITE_CONFIG_CACHE, 'front_domain'):
    #     return False, '网站前端域名未设置!'
    # front_domain = getattr(SITE_CONFIG_CACHE, 'front_domain')
    # if not front_domain:
    #     return False, '网站前端域名未设置'
    return True, ''


def check_ip():
    """检测黑名单"""
    # if hasattr(SITE_CONFIG_CACHE, 'cms_ip_whitelist'):
    #     cms_ip_whitelist = getattr(SITE_CONFIG_CACHE, 'cms_ip_whitelist')
    #     if cms_ip_whitelist or cms_ip_whitelist.strip():
    #         crr_ip = get_ip()
    #         for _ip in crr_ip.split(','):
    #             if _ip in crr_ip:
    #                 return True
    #         return

    return True


def front_risk_control():
    ''' 前端风控 '''
    return True, None


def cms_risk_control():
    ''' 后端风控 '''
    # if not check_ip():
    #     return abort(404)
    pass


def proejct_template_path(path):
    ''' 模板文件路径前缀 '''
    # if path.startswith('/'):
    #     return SITE_CONFIG_CACHE.project_name + path
    # return SITE_CONFIG_CACHE.project_name + '/' + path
    pass


# py类型dict, 转化纯JSON
def pymodel_to_json(mcls, data):
    if not data:
        return {}
    if not isinstance(data, dict):
        return data
    if '_id' in data:
        data.pop('_id')
    _fields = mcls.fields()
    for field, fcls in _fields.items():
        if not fcls or not hasattr(fcls, 'field_type'):
            continue
        if fcls.field_type == 'DateTimeField':
            _v = data.get(field) or ''
            if not _v:
                continue
            data[field] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return data


# 网站配置缓存获取
def site_config_cache(updateDict=None, updateData=False, expire=20 * 60):
    if updateDict is None:
        updateDict = {}
    _fields = SiteConfigTable.fields()
    kk = current_app.config.get('PROJECT_NAME')+'_'+'siteConfigCache'
    if updateDict:
        _updateDict = json.dumps(updateDict)
        SiteRedis.set(kk, _updateDict, expire=expire)
        return updateDict
    if updateData:
        SiteRedis.dele(kk)
    _vv = SiteRedis.get(kk)
    if not _vv:
        site_data = SiteConfigTable.find_one({})
        if not site_data:
            return {}
        _vv = pymodel_to_json(SiteConfigTable, site_data)
        _vv = json.dumps(_vv)
        SiteRedis.set(kk, _vv, expire=expire)
        return site_data
    _vv = json.loads(_vv.decode())
    _vv = pymodel_to_json(SiteConfigTable, _vv)
    return _vv


