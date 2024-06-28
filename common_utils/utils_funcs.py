# -*- coding: UTF-8 -*-
import re
import os
import time
import uuid
import shortuuid
import random
import hashlib
import zlib
import base64
import qrcode
import datetime
import json
import psutil
import datetime
import socket
import uuid
import subprocess
from io import BytesIO
from flask import request
from flask_paginate import Pagination
from .captcha.xtcaptcha import Captcha
from .lqredis import SiteRedis
from .encrypt.RC4_CLS import Rc4
from PIL import Image

from constants import CMS_LANGUAGE_JSON, LANGUAGE

def update_language(target_language, text):
    for crr_la in LANGUAGE.name_arr:
        if target_language != crr_la:
            continue
        if crr_la == LANGUAGE.en_US:
            for la in CMS_LANGUAGE_JSON:
                if not la.get('en'):
                    continue
                text = text.replace(la.get('zh'), la.get('en'))
        elif crr_la == LANGUAGE.vi_VN:
            for la in CMS_LANGUAGE_JSON:
                if not la.get('vi'):
                    continue
                text = text.replace(la.get('zh'), la.get('vi'))
        elif crr_la == LANGUAGE.ba_IDN:
            for la in CMS_LANGUAGE_JSON:
                if not la.get('idn'):
                    continue
                text = text.replace(la.get('zh'), la.get('idn'))
        elif crr_la == LANGUAGE.bx_Pr:
            for la in CMS_LANGUAGE_JSON:
                if not la.get('Pt'):
                    continue
                text = text.replace(la.get('zh'), la.get('Pt'))
        elif crr_la == LANGUAGE.ja:
            for la in CMS_LANGUAGE_JSON:
                if not la.get('ja'):
                    continue
                text = text.replace(la.get('zh'), la.get('ja'))
        elif crr_la == LANGUAGE.ko:
            for la in CMS_LANGUAGE_JSON:
                if not la.get('ko'):
                    continue
                text = text.replace(la.get('zh'), la.get('ko'))
        else:
            for la in CMS_LANGUAGE_JSON:
                if not la.get(crr_la):
                    continue
                text = text.replace(la.get('zh'), la.get(crr_la))
    return text


def create_order_num():
    """生成流水订单号"""
    res_id = ''.join(list(str(int(time.time()*1000 + random.choice(range(10000, 99999))))[2:])[::-1])
    crr_date = datetime.datetime.now().strftime('%Y%m%d')
    perf_counter = str(int(time.perf_counter()*10000))
    return res_id + crr_date + perf_counter

def create_secret_key():
    """生成唯一的秘钥"""
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, shortuuid.uuid()))

def generate_filename():
    """生成文件名"""
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    res = '%s%s' % (filename_prefix, str(random.randrange(1, 10000)))
    return res

def get_content_md5(content):
    """计算内容MD5"""
    myhash = hashlib.md5()
    while True:
        b = content[0:4096]
        if not b:
            break
        content = content[4096:]
        myhash.update(b)
    return myhash.hexdigest()

def get_file_md5(file_name):
    """计算文件md5值"""
    if not isinstance(file_name, bytes):
        file_name = file_name.encode()
    if not os.path.exists(file_name):
        return False, '文件不存在!'
    m = hashlib.md5()
    with open(file_name, 'rb') as fobj:
        while True:
            f = fobj.read(4096)
            if not f:
                break
            m.update(f)
    return True, m.hexdigest()

def get_file_sha1(fineName, block_size=4 * 1024):
    """文件sha1"""
    if not isinstance(fineName, bytes):
        fineName = fineName.encode()
    if not os.path.exists(fineName):
        return False, '文件不存在!'
    sha1 = hashlib.sha1()
    with open(fineName, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            sha1.update(data)
    retsha1 = base64.b64encode(sha1.digest())
    return True, retsha1

def check_telephone(telephone):
    """检测手机号"""
    if not telephone or not telephone.strip():
        return False, u'手机号不能为空！'
    if len(telephone.strip()) != 11:
        return False, u'手机号为11位哦！'
    p2 = re.compile('^1[3578]\d{9}$|^147\d{8}$')
    if not p2.match(telephone.strip()):
        return False, u'手机号格式不对！'
    return True, telephone.strip()

def is_valid_url(url):
    """检测URL"""
    _URL_REGEX = re.compile(
        r"^(?:[a-z0-9\.\-]*)://"  # scheme is validated separately
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-_]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}(?<!-)\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ...or ipv4
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # ...or ipv6
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    _URL_SCHEMES = ["http", "https", "ftp", "ftps"]
    scheme = url.split("://")[0].lower()
    if scheme not in _URL_SCHEMES:
        return False, '无效的协议!'
    if not _URL_REGEX.match(url):
        return False, '无效的URL!'
    return True, ''

def zlib_encry(a):
    """压缩字符串"""
    aa = zlib.compress(a)
    return base64.b64encode(aa)

def zlib_decry(d):
    """解压字符串"""
    dd = base64.b64decode(d)
    return zlib.decompress(dd)

def encry_md5(data):
    """MD5加密"""
    md5_object = hashlib.md5()
    md5_object.update(data.encode('utf8'))
    md5_result = md5_object.hexdigest()
    return md5_result

def get_file_size(file_path, types='KB'):
    """
    获取文件大小
    :param file_path: 文件类型
    :param types: 文件大小格式（KB, MB, T）
    :return:
    """
    if types == 'MB':
        fsize = os.path.getsize(file_path)
        fsize = fsize / float(1024 * 1024)
        return round(fsize, 3)
    fsize = os.path.getsize(file_path)
    fsize = fsize / 1024
    return round(fsize, 3)

def is_wap():
    """判断是否是移动端"""
    ua = str(request.user_agent).lower()
    for w in ['iphone','android']:
        if w in ua:
            return True
    return False

def check_ip(ip):
    """判断ip"""
    ep = re.compile('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)')
    if not ep.match(ip.strip()):
        return False, u'ip格式不对！'
    return True, ip.strip()

def get_ip():
    """获取真实ip"""
    cf_ip = request.headers.get('CF-Connecting-IP') # 获取cloudflare代理后的真实IP
    if cf_ip:
        return cf_ip
    ip = request.headers.get('X-Real-Ip')
    if ip:
        return ip
    ip = request.headers.get('X-Forwarded-For')
    if ip:
        return ip
    ip_list = list(request.access_route)
    return ', '.join(ip_list)

def get_all_ip():
    allips = []
    cf_ip = request.headers.get('CF-Connecting-IP') # 获取cloudflare代理后的真实IP
    if cf_ip:
        allips.append(cf_ip)
    ip = request.headers.get('X-Real-Ip')
    if ip:
        allips.append(ip)
    ip = request.headers.get('X-Forwarded-For')
    if ip:
        allips.append(ip)
    ip_list = list(request.access_route)
    allips += ip_list
    ips = list(set(allips))
    return ips

def graph_captcha():
    """图片验证码"""
    text, image = Captcha.gene_code()
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    SiteRedis.set(text.lower(), text.lower(), expire=60)
    img = 'data:image/png;base64,%s' % base64.b64encode(out.read()).decode()
    return img

def checkcap(cap):
    """检测图片验证码"""
    if Captcha.check_captcha(cap):
        return True
    return False

def generate_qrcode(data):
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

def get_random_time():
    """获取随机时间"""
    crr_date = datetime.datetime.now()
    if crr_date.hour < 6:
        a1 = (crr_date.year, crr_date.month, crr_date.day-1, 6, 0, 0, 0, 0, 0)
        a2 = (crr_date.year, crr_date.month, crr_date.day-1, crr_date.hour, crr_date.minute, crr_date.second, 0, 0, 0)
    else:
        a1 = (crr_date.year, crr_date.month, crr_date.day, 6, 0, 0, 0, 0, 0)
        a2 = (crr_date.year, crr_date.month, crr_date.day, crr_date.hour, crr_date.minute, crr_date.second, 0, 0, 0)
    start = time.mktime(a1)
    end = time.mktime(a2)
    t = random.randint(int(start), int(end))
    date_touple = time.localtime(t)
    date_str = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)
    rand_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return rand_date


def getDayDateSilce():
    '''
    获取今日时间区间
    '''
    crr_time = datetime.datetime.now()
    time_start = datetime.datetime(crr_time.year, crr_time.month, crr_time.day, 0, 0, 0)
    time_end = datetime.datetime(crr_time.year, crr_time.month, crr_time.day, 23, 59, 59)
    return time_start, time_end


def getMonthDateSilce():
    '''
    获取本月时间区间
    '''
    today = datetime.date.today()
    if today.month == 12:
        last_day = datetime.date(today.year, 12, 31)
    else:
        last_day = datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(days=1)
    time_start = datetime.datetime(last_day.year, last_day.month, 1, 0, 0, 0)
    time_end = datetime.datetime(last_day.year, last_day.month, last_day.day, 23, 59, 59)
    return time_start, time_end


def img_base4_save(img_base64, savePath):
    '''
    Base64图片保存本地
    '''
    if not img_base64.startswith('data:image/png;base64,'):
        return

    # 去除前缀信息（如'data:image/png;base64,'）
    if img_base64.startswith('data:'):
        _, data = img_base64.split(',', maxsplit=1)
    else:
        data = img_base64

    # 解码Base64数据
    decoded_data = base64.b64decode(data)
    # 创建BytesIO对象来读取二进制数据
    buffered_io = BytesIO()
    buffered_io.write(decoded_data)
    buffered_io.seek(0)
    # 打开图像文件
    img = Image.open(buffered_io)
    # 指定保存路径及名称
    # 保存图像到本地
    img.save(savePath)
    return True


def img_to_base64(imgUrl):
    '''
    图片转Base64
    '''
    if not os.path.exists(imgUrl):
        return
    with open(imgUrl, "rb") as file:
        image_data = file.read()

    # 将图片数据编码为Base64格式
    encoded_data = base64.b64encode(image_data)

    # 将Base64编码的数据写入字节流
    image_stream = BytesIO(encoded_data)

    # 输出Base64编码的图片数据
    fff = image_stream.read().decode()
    bbb = 'data:image/png;base64,' + fff
    return bbb



class PagingCLS(object):

    @classmethod
    def by_silce(cls, startendstr):
        if startendstr and '|' not in startendstr:
            raise ValueError(u'区间搜索必须以“|”分割')
        start_str, end_str = startendstr.split("|")
        if start_str.isdigit() or end_str.isdigit():
            if start_str and end_str:
                return int(start_str),int(end_str)
            if start_str and not end_str:
                return int(start_str),None
            return None,int(end_str)
        else:
            if start_str:
                try:
                    start_time = datetime.datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
                except:
                    try:
                        start_time = datetime.datetime.strptime(start_str, '%Y-%m-%d')
                    except Exception as e:
                        raise ValueError(u'起始时间转换出错: %s' % str(e))
            else:
                start_time = None
            if end_str:
                try:
                    end_time = datetime.datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
                except:
                    try:
                        end_time = datetime.datetime.strptime(end_str, '%Y-%m-%d')
                    except Exception as e:
                        raise ValueError(u'结束时间转换出错: %s' % str(e))
            else:
                end_time = None
            return start_time, end_time

    @classmethod
    def pagination(cls, page, per_page, total, **kwargs):
        return Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4', alignment='center', **kwargs)

    @classmethod
    def ustom_pagination(cls, page, data_count, PAGE_NUM=None):
        # page:当前页面
        # data_count:数据总数
        # PAGE_NUM：每页的显示数据数量
        if not PAGE_NUM:
            PAGE_NUM = 10
        total_page = data_count // PAGE_NUM
        if data_count % PAGE_NUM > 0:
            total_page += 1

        pages = []
        tmp_page = page - 1
        while tmp_page >= 1:
            if tmp_page % 5 == 0:
                break
            pages.append(tmp_page)
            tmp_page -= 1
        tmp_page = page
        while tmp_page <= total_page:
            if tmp_page % 5 == 0:
                pages.append(tmp_page)
                break
            else:
                pages.append(tmp_page)
                tmp_page += 1

        pages.sort()
        return pages, total_page



class RC4CLS(object):

    @classmethod
    def encrypt(cls, data, secret_key=''):
        try:
            mi = Rc4(secret_key + '666999' if secret_key else '').encrypt(data)
            return mi
        except Exception as e:
            return False

    @classmethod
    def decrypt(cls, data, secret_key=''):
        try:
            mg = Rc4(secret_key + '666999' if secret_key else '').decrypt(data)
            return mg
        except:
            return False



class ServerFunc:

    # 获取Mac地址
    @classmethod
    def get_mac_address(cls):
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    # 磁盘 磁盘的使用量等等
    @classmethod
    def get_my_computer(cls):
        # 获取主机名
        hostname = socket.gethostname()
        # 获取IP
        ip = socket.gethostbyname(hostname)
        # 系统用户
        users_list = ",".join([u.name for u in psutil.users()])
        # print(u"当前有%s个用户，分别是%s" % (users_count, users_list))
        # 系统启动时间
        start_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        sys_info = {"hostname": hostname, "ip": ip, "mac": cls.get_mac_address(), "user": users_list,"start_time": start_time}

        # 01.cpu信息
        cpu1 = psutil.cpu_count()
        cpu2 = str(psutil.cpu_percent(interval=1)) + '%'
        # print(u"物理CPU个数 %s" % psutil.cpu_count(logical=False))
        cpu = {"amount": cpu1, "rate": cpu2}

        # 02.内存信息
        mem = psutil.virtual_memory()
        mem_total = round(mem.total / 1024 / 1024 / 1024, 2)
        mem_free = round(mem.free / 1024 / 1024 / 1024, 2)
        mem_percent = str(mem.percent) + '%'
        mem_used = round(mem.used / 1024 / 1024 / 1024, 2)
        ddr = {"total": mem_total, "free": mem_free, "rate": mem_percent, "used": mem_used}

        # 03.磁盘信息(磁盘空间使用占比)
        io = psutil.disk_partitions()
        disk = []
        for i in io:
            # print(i.device)
            o = psutil.disk_usage(i.device)
            disk_data = {"disk_name": i.device,
                         "total": round(o.total / (1024.0 * 1024.0 * 1024.0), 1),
                         "used": round(o.used / (1024.0 * 1024.0 * 1024.0), 1),
                         "surplus": round(o.free / (1024.0 * 1024.0 * 1024.0), 1),
                         "rate": psutil.disk_usage(i.device).percent}
            disk.append(disk_data)

        # 04.网卡，可以得到网卡属性，连接数，当前流量等信息
        net_info = psutil.net_io_counters()
        bytes_sent = '{0:.2f}'.format(net_info.bytes_recv / 1024 / 1024)  # mb
        bytes_rcvd = '{0:.2f}'.format(net_info.bytes_sent / 1024 / 1024)
        net = {"bytes_sent": bytes_sent, "bytes_rcvd": bytes_rcvd}

        # 数据字典
        data = {"sys": sys_info, "cpu": cpu, "ddr": ddr, "disk": disk, "net": net}
        return data
