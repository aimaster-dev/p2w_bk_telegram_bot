# -*- coding: utf-8 -*-
import six, re, datetime, shortuuid
from werkzeug.security import generate_password_hash
from site_exts import db


__all__ = (
    'FieldHelpres',
    'StringField',
    'URLField',
    'EmailField',
    'IPField',
    'PasswordField',
    'FloatField',
    'BooleanField',
    'DateTimeField',
    'UUIDField',
    'TelephoneField',
    'IntegerField',
    'IDField',
    'RelationField',
    'FileField',
    'DictField',
    'ImagesField',
    'TextField',
)


class LazyRegexCompiler(object):

    def __init__(self, pattern, flags=0):
        self._pattern = pattern
        self._flags = flags
        self._compiled_regex = None

    @property
    def compiled_regex(self):
        if self._compiled_regex is None:
            self._compiled_regex = re.compile(self._pattern, self._flags)
        return self._compiled_regex

    def __get__(self, instance, owner):
        return self.compiled_regex


class FieldBase(object):

    def __init__(
        self,
        field_name,
        db_field=None,
        nullable=True,
        default=None,
        unique=False,
        primary_key=False,
        error_msg=None,
        field_type=None,
        show_total=False,

        readonly=None,
        disabled=False,
        placeholder=None,
        href=None,
        is_index=False,
        onclick=None,
        btn_show=False,
        btn_style=None,
        text_align = None,
        upload_progress=False,
        db_database=None,
        **kwargs
    ):
        """
        :param field_name:字段名(text)
        :param db_field:存储该字段的数据库字段（字段）
        :param default:默认值
        :param unique:是否唯一，True or False,Default: False
        :param nullable:字段是否可为空 True or False,Default: True
        :param primary_key: 主键(不可为空且唯一且自增长)
        :param error_msg:错误信息
        :param field_type:字段类型
        :param is_index: 字段索引

        :param readonly: input可读
        :param disabled: input禁用
        :param placeholder: input描述
        :param href: url链接
        :param onclick: 点击操作类型
        :param btn_show: 是否按钮显示
        :param btn_style: 按钮样式
        :param text_align: 居占位置
        :param upload_progress: 文件上传进度条
        :param show_total: 是否显示统计总数
        :param db_database: 数据库对象
        """
        self.db_field = db_field
        self.field_name = field_name
        self.nullable = nullable
        self.default = default
        self.unique = unique
        self.primary_key = primary_key
        self.error_msg = error_msg
        self.field_type = field_type or self.__class__.__name__
        self.is_index = is_index
        self.readonly = readonly
        self.disabled = disabled
        self.placeholder = placeholder or field_name
        self.href = href
        self.onclick = onclick
        self.btn_show = btn_show
        self.btn_style = btn_style
        self.text_align = text_align
        self.upload_progress = upload_progress
        self.show_total = show_total
        self.db_database = db_database
        if self.db_database is None:
            self.db_database = db.database
        
        # db_field 是一个字符串
        if self.db_field is not None and not isinstance(
            self.db_field, six.string_types
        ):
            raise TypeError("db_field should be a string.")

        # 确保db_field不包含任何禁止的字符
        if isinstance(self.db_field, six.string_types) and (
            "." in self.db_field
            or "\0" in self.db_field
            or self.db_field.startswith("$")
        ):
            raise ValueError(
                'field names cannot contain dots (".") or null characters '
                '("\\0"), and they must not start with a dollar sign ("$").'
            )

        conflicts = set(dir(self)) & set(kwargs)
        if conflicts:
            raise TypeError(
                "%s already has attribute(s): %s"
                % (self.__class__.__name__, ", ".join(conflicts))
            )

        self.__dict__.update(kwargs)

    def validate(self, value=''):
        """验证"""
        if not self.nullable and not value:
            return False, u'%s: 不能为空!' % self.field_name
        if value:
            return True, value.strip()
        return True, ''

    def search_validate(self, value=''):
        """搜索验证"""
        if value and value.strip():
            value = {'$regex': value.strip()}
        return True, value

    def transform(self, value=''):
        """转化处理"""
        if not value:
            return ''
        return str(value).strip()

    def default(self):
        """默认值"""
        return ''

    def owner_document(self):
        """下级成员"""
        pass

    def lookup_member(self):
        """上级成员"""
        pass


class StringField(FieldBase):
    def __init__(self, field_name, regex='', max_length=None, min_length=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.regex = re.compile(regex) if regex else None
        self.max_length = max_length
        self.min_length = min_length

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not isinstance(value, six.string_types):
            return False, u"%s: 应为字符串值" % self.field_name
        if self.max_length is not None and len(value) > self.max_length:
            return False, u'%s: 长度过长!' % self.field_name
        if self.min_length is not None and len(value) < self.min_length:
            return False, u'%s: 长度过短!' % self.field_name
        if self.regex is not None and self.regex.match(value) is None:
            return False, u'%s: 与验证正则表达式不匹配' % self.field_name
        return True, value.strip()

    def search_validate(self, value=''):
        if value:
            value = value.strip()
            value = value.replace('[','\[').replace(']','\]')
            return True, {'$regex': value}
        return True, value


class TextField(StringField):
    """文本字段"""
    def __init__(self, field_name, max_length=None,  **kwargs):
        super().__init__(field_name, max_length=max_length, **kwargs)


class URLField(StringField):
    _URL_REGEX = LazyRegexCompiler(
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

    def __init__(self, field_name, url_regex=None, schemes=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.url_regex = url_regex or self._URL_REGEX
        self.schemes = schemes or self._URL_SCHEMES

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not isinstance(value, six.string_types):
            return False, u"%s: 应为字符串值" % self.field_name
        scheme = value.split("://")[0].lower()
        if scheme not in self.schemes:
            return False, u'%s: 无效的协议!' % self.field_name
        if not self.url_regex.match(value):
            return False, u'%s: 无效的url!' % self.field_name
        return True, value.strip()


class EmailField(StringField):
    USER_REGEX = LazyRegexCompiler(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z" +
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)',
        re.IGNORECASE,
    )
    DOMAIN_REGEX = LazyRegexCompiler(
        r"((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))\Z",
        re.IGNORECASE,
    )
    def __init__(self, field_name, domain_whitelist=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.domain_whitelist = domain_whitelist or []

    def validate_user_part(self, user_part):
        return self.USER_REGEX.match(user_part)

    def validate_domain_part(self, domain_part):
        """验证电子邮件地址的域名部分。返回True,如果有效，否则为Flase; 跳过域验证，如果它在白名单中"""
        if domain_part in self.domain_whitelist:
            return True
        if self.DOMAIN_REGEX.match(domain_part):
            return True
        return False

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if "@" not in value:
            return False, u'%s: 格式错误!' % self.field_name
        user_part, domain_part = value.rsplit("@", 1)
        if not self.validate_user_part(user_part):
            return False, u'%s: 格式错误!' % self.field_name
        if not self.validate_domain_part(domain_part):
            return False, u'%s: 格式错误!' % self.field_name
        return True, value.strip()


class IPField(StringField):
    IP_REGEX = re.compile("(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)")

    def __init__(self, field_name, regex=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.ip_regex = regex or self.IP_REGEX

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not isinstance(value, six.string_types):
            return False, u"%s: 应为字符串值!" % self.field_name
        if not self.ip_regex.match(value):
            return False, u'%s: 无效的ip!' % self.field_name
        return True, value.strip()


class ImagesField(StringField):

    def __init__(self, field_name, width='50', height='50',  **kwargs):
        super().__init__(field_name, **kwargs)
        self.width = width
        self.height = height


class PasswordField(FieldBase):
    def __init__(self, field_name, max_length=None, min_length=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.max_length = max_length
        self.min_length = min_length

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not isinstance(value, six.string_types):
            return False, u"%s: 应为字符串值" % self.field_name
        if self.max_length is not None and len(value) > self.max_length:
            return False, u'%s: 长度过长!' % self.field_name
        if self.min_length is not None and len(value) < self.min_length:
            return False, u'%s: 长度过短!' % self.field_name
        raspwd = generate_password_hash(value.strip())
        return True, raspwd


class FloatField(FieldBase):
    def __init__(self, field_name, min_value=None, max_value=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.min_value, self.max_value = min_value, max_value

    def transform(self, msg=''):
        if isinstance(msg, float):
            return msg or 0
        try:
            return float(msg)
        except:
            return msg or 0

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not isinstance(value, float):
            try:
                value = float(value)
            except Exception as e:
                return False, u'%s: 类型错误!' % self.field_name
        if self.min_value is not None and value < self.min_value:
            return False, u'%s: 值太小！' % self.field_name
        if self.max_value is not None and value > self.max_value:
            return False, u'%s: 值太大' % self.field_name
        return True, value

    def search_validate(self, value=''):
        if '-' in value:
            try:
                start, end = value.split('-')
                start = float(start)
                end = float(end)
            except:
                return None, u'%s输入错误：请输入数字或小数，以“-”分割' % self.field_name
            if start > end:
                return None, u'%s输入错误：搜索起始值大小结束值' % self.field_name
            return True, {'$gt': start, '$lt': end}
        else:
            try:
                return True, float(value)
            except:
                return None, u'%s输入错误：请输入数字或小数！' % self.field_name


class BooleanField(FieldBase):
    def __init__(self, field_name, is_index=True, default=True, true_text='正常', false_text='异常', true_style='btn-success', false_style='btn-danger', **kwargs):
        super().__init__(field_name, is_index=is_index, default=default, **kwargs)
        self.true_text = true_text
        self.false_text = false_text
        self.true_style = true_style
        self.false_style = false_style
        self.choices = ((True, self.true_text, true_style), (False, self.false_text, self.false_style))

    def validate(self, value=''):
        if not self.nullable and (not value or not value.strip()):
            return False, '%s: 不可为空!' % self.field_name
        if not isinstance(value, bool):
            value = value.strip().lower()
            if value in ['1', 'true']:
                return True, True
            if value in ['0', 'false']:
                return True, False
            return False, '%s: 数值错误!' % self.field_name
        return True, value

    def search_validate(self, value=''):
        if not isinstance(value, bool):
            value = value.strip()
            if value in ['1', 'true']:
                return True, True
            if value in ['0', 'false']:
                return True, False
            return False, '%s: 数值错误!' % self.field_name
        return True, value

    def transform(self, value=''):
        if not value:
            return self.choices[-1][0]
        if not isinstance(value, bool):
            value = value.strip()
            if value not in ['1', '0', 'true', 'false']:
                return False
            if value in ['1', 'true']:
                value = True
            if value in ['0', 'false']:
                value = False
            return value
        return value


class DateTimeField(FieldBase):
    def __init__(self, field_name, to_date=True, to_time=False,  **kwargs):
        super().__init__(field_name, is_index=True, to_date=to_date, to_time=to_time, **kwargs)

    def by_silce(self,startendstr):
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
                        timedelay = datetime.timedelta(days=1)
                        end_time += timedelay
                    except Exception as e:
                        raise ValueError(u'结束时间转换出错: %s' % str(e))
            else:
                end_time = None
            return start_time, end_time

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not isinstance(value, datetime.datetime):
            try:
                value = value.strip()
                transform_data = datetime.datetime.strptime(value, u'%Y-%m-%d %H:%M:%S')
                return True, transform_data
            except Exception:
                return False, u'%s: 格式错误!' % self.field_name
        return True, value

    def search_validate(self, value=''):
        try:
            start, end = self.by_silce(value)
        except Exception as e:
            return None, u'%s选择错误：%s' % (self.field_name, str(e))
        return True, {'$gt': start, '$lt': end}

    def transform(self, value=''):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return value or ''


class UUIDField(FieldBase):
    def __init__(self, field_name=u'UUID', **kwargs):
        super().__init__(field_name, is_index=True, nullable=False, **kwargs)

    def default(self):
        return shortuuid.uuid()


class TelephoneField(FieldBase):
    def __init__(self, field_name='手机号', **kwargs):
        super().__init__(field_name, is_index=True, **kwargs)

    def is_telephone(self,telephone=None):
        if not telephone or not telephone.strip():
            return False, u'手机号不能为空！'
        if len(telephone.strip()) != 11:
            return False, u'手机号为11位哦！'
        p2 = re.compile('^1[356789]\d{9}$|^147\d{8}$')
        if not p2.match(telephone.strip()):
            return False, u'手机号格式不对！'
        return True, telephone.strip()

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s不能为空！' % self.field_name
        statu, value = self.is_telephone(value)
        if not statu:
            return False, value
        return True, value


class IntegerField(FieldBase):
    def __init__(self, field_name, min_value=None, max_value=None, default=1, **kwargs):
        super().__init__(field_name, default=default, **kwargs)
        self.min_value, self.max_value = min_value, max_value

    def validate(self, value=''):
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if not value:
            return True, self.default
        try:
            value = int(value.strip())
        except (TypeError, ValueError):
            return False, u'%s: 类型错误!' % self.field_name
        if self.min_value is not None and value < self.min_value:
            return False, u'%s: 整数值太小!' % self.field_name
        if self.max_value is not None and value > self.max_value:
            return False, u'%s: 整数值太大!' % self.field_name
        return True, value

    def search_validate(self, value=''):
        value = value.strip().replace(',','').replace('，','').replace(' ','')
        if '-' in value:
            try:
                start, end = value.split('-')
                start = int(start)
                end = int(end)
            except:
                return None, u'%s输入错误：请输入数字或小数，以“-”分割' % self.field_name
            if start > end:
                return None, u'%s输入错误：搜索起始值大小结束值' % self.field_name
            return True, {'$gt': start, '$lt': end}
        try:
            return True, int(value)
        except:
            return None, u'%s输入错误：请输入数字或小数！' % self.field_name

    def transform(self, value=''):
        try:
            if not value or not value.strip():
                return 0
            return int(value.strip())
        except:
            return value


class IDField(IntegerField):
    def __init__(self, field_name=u'ID', default=1, **kwargs):
        super().__init__(field_name, default=default, primary_key=True, is_index=True, **kwargs)


class RelationField(FieldBase):
    def __init__(self, field_name,
                 relation_collection='',
                 filter_dict={},
                 relation_show_field='',
                 relation_control_fields=[],
                 target_relation_collection='',
                 localField='',
                 foreignField='',
                 dbref=None,
                 **kwargs):
        super().__init__(field_name, field_type='RelationField', **kwargs)
        self.filter_dict = filter_dict  #查询筛选
        self.relation_collection = relation_collection  #数据表
        self.relation_show_field = relation_show_field  # 显示的字段
        self.relation_control_fields = relation_control_fields  # 控制查询输出的字段
        self.target_relation_collection = target_relation_collection  #关系表名（用户多对多查询）
        self.localField = localField # 关系表对比字段
        self.foreignField = foreignField # 绑定的表对比字段(关系表内绑定的表)
        self.dbref = dbref # 外键

    def relation_datas(self, filter_data={}):
        aggreg = []
        collection = getattr(self.db_database, self.relation_collection)
        self.filter_dict.update(filter_data)
        if self.filter_dict:
            aggreg.append({'$match': self.filter_dict})
        if self.relation_control_fields:
            _project = {'uuid': 1, self.relation_show_field: 1}
            for k in self.relation_control_fields:
                _project[k] = 1
            aggreg.append({'$project': _project})
        datas = collection.aggregate(aggreg)
        return list(datas)

    def relation_data(self, bind_uuid=None):
        if not bind_uuid or not bind_uuid.strip():
            return {}
        collection = getattr(self.db_database, self.relation_collection)
        match = {'uuid': bind_uuid.strip()}
        pipline = [{'$match':match}]
        pipline.append({'$limit':1})
        res = list(collection.aggregate(pipline))
        if res:
            return res[0]
        return {}

    def many_relation_datas(self, data_uuid, filter_data={}):
        if not data_uuid or not data_uuid.strip():
            return {}
        many_aggreg = []
        collection = getattr(self.db_database, self.target_relation_collection)
        if filter_data:
            many_aggreg.append({'$match': filter_data})
        many_aggreg.append({'$lookup': {'from': self.relation_collection, 'localField': self.localField, 'foreignField': self.foreignField, 'as': 'datas'}})
        datas = list(collection.aggregate(many_aggreg))
        return datas


class FileField(FieldBase):
    def __init__(self, field_name, upload_to='', **kwargs):
        super().__init__(field_name, **kwargs)
        self.upload_to = upload_to


class DictField(FieldBase):
    def __init__(self, field_name,  dict_cls=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.dict_cls = dict_cls

    def validate(self, value=''):
        if not isinstance(value, str):
            return value
        value = value.strip()
        if not self.nullable and not value:
            return False, u'%s: 不可为空!' % self.field_name
        if value and value not in self.dict_cls.name_arr:
            return False, '%s: 数据错误!' % self.field_name
        return True, value

class FieldHelpres(object):
    StringField = StringField
    URLField = URLField
    EmailField = EmailField
    IPField = IPField
    PasswordField = PasswordField
    FloatField = FloatField
    BooleanField = BooleanField
    DateTimeField = DateTimeField
    UUIDField = UUIDField
    TelephoneField = TelephoneField
    IntegerField = IntegerField
    IDField = IDField
    RelationField = RelationField
    FileField = FileField
    DictField = DictField
    ImagesField = ImagesField
    TextField = TextField

