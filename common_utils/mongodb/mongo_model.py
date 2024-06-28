# -*- coding: UTF-8 -*-
import datetime, shortuuid
from copy import copy
from site_exts import db
from common_utils.lqredis import SiteRedis
from .field_cls import FieldHelpres


class dbModel(FieldHelpres):

    database = db.database
    project_name = db.project_name
    __tablename__ = ''

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, db_field):
        return ''

    @classmethod
    def add_field_sort(cls):
        return []

    @classmethod
    def edit_field_sort(cls):
        return []

    @classmethod
    def field_search(cls):
        return []

    @classmethod
    def field_sort(cls):
        return []

    @classmethod
    def ForeignKey(cls, db_field, target_field):
        dbref = {}
        if hasattr(db, 'dbref'):
            dbref = getattr(db, 'dbref')
        if db_field.count('.') <= 1:
            return
        table_name = dbref.split('.')
        l = {db_field: [target_field]}

    @classmethod
    def fields_name(cls):
        """获取全部的字段名"""
        arr = dir(cls)
        for c in dir(dbModel):
            arr.remove(c)
        return arr

    @classmethod
    def fields(cls):
        """获取字段实例化"""
        res = {}
        for name in cls.fields_name():
            try:
                res[name] = getattr(cls, name)
            except:
                raise ValueError('class has no this field name:%s' % name)
        return res

    @classmethod
    def remove_primarykey(cls, db_field):
        """清除当前字段历史主键"""
        current_key = '%s_%s_%s_%s_field' % (cls.project_name, cls.database._Database__name, cls.table_name(), db_field)
        SiteRedis.dele(current_key)

    @classmethod
    def get_primarykey_latest(cls, db_field, default=None):
        """获取字段历史主键"""
        current_key = '%s_%s_%s_%s_field' % (cls.project_name, cls.database._Database__name, cls.table_name(), db_field)
        if not SiteRedis.get(current_key):
            current_id = SiteRedis.incrby(current_key, int(default))
        else:
            current_id = SiteRedis.incrby(current_key)
        return int(current_id)

    @classmethod
    def insert_one_handle(cls, data):
        if 'uuid' not in data:
            data['uuid'] = shortuuid.uuid()
        if 'create_time' not in data:
            data['create_time'] = datetime.datetime.now()
        for db_field in cls.fields_name():
            k_cls = getattr(cls, db_field)
            if not k_cls or not hasattr(k_cls, 'field_type'):
                continue
            if data.get(db_field):
                continue
            if k_cls.primary_key:
                data[db_field] = cls.get_primarykey_latest(db_field, k_cls.default)
            elif not k_cls.nullable:
                if k_cls.field_type == 'DateTimeField':
                    data[db_field] = datetime.datetime.now()
                elif k_cls.field_type == 'UUIDField':
                    data[db_field] = shortuuid.uuid()
                elif k_cls.field_type == 'BooleanField':
                    if isinstance(data.get(db_field), bool):
                        continue
                    if data.get(db_field) is None:
                        data[db_field] = k_cls.default
                else:
                    data[db_field] = k_cls.default
            else:
                pass
        return data

    @classmethod
    def table_name(cls):
        return cls.__tablename__ or cls.__name__.lower()

    @classmethod
    def collection(cls):
        return getattr(cls.database, cls.table_name())

    @classmethod
    def create_index(cls, keys, **kwargs):
        return cls.collection().create_index(keys, background=True, **kwargs)

    @classmethod
    def index_information(cls):
        return cls.collection().index_information()

    @classmethod
    def save(cls,data_dict):
        uuid = data_dict.get('uuid')
        if not uuid:
            uuid = shortuuid.uuid()
            data_dict['uuid'] = uuid
        if data_dict.get('_id'):
            cls.collection().update_one({"uuid": data_dict['uuid']}, {"$set": data_dict})
        else:
            cls.insert_one(data_dict)
        return uuid

    @classmethod
    def count(cls,filter=None, session=None, **kwargs):
       return cls.collection().count_documents(filter=filter, session=session, **kwargs)

    @classmethod
    def query_one(cls,data, **kwargs):
        data = cls.find_one(data,**kwargs)
        if not data:
            return None
        return copy(cls)(**data)

    @classmethod
    def query_many(cls,data, **kwargs):
        res = cls.collection().find(data, **kwargs)
        arr = []
        for d in res:
            arr.append(copy(cls)(**d))
        return arr

    @classmethod
    def insert_one(cls, data):
        uuid = data.get('uuid')
        if not uuid:
            uuid = shortuuid.uuid()
            data['uuid'] = uuid
        data = cls.insert_one_handle(data)
        cls.collection().insert_one(data)
        return uuid

    @classmethod
    def distinct(cls, key, filter=None,**kwargs):
        return cls.collection().distinct(key, filter=filter, session=None, **kwargs)

    @classmethod
    def insert_many(cls, data_list):
        uuids = []
        for d in data_list:
            uuids.append(cls.insert_one(d))
        return uuids

    @classmethod
    def find_one(cls, data={}, **kwargs):
        res = cls.collection().find_one(data, **kwargs)
        return res or {}

    @classmethod
    def find_many(cls, data={}, **kwargs):
        res = cls.collection().find(data, **kwargs)
        return [d for d in res]

    @classmethod
    def update_one(cls, data_update, data_options, upsert=False):
        res = cls.collection().update_one(data_update, data_options, upsert=upsert)
        return res

    @classmethod
    def update_many(cls, data_update, data_options):
        res = cls.collection().update_many(data_update, data_options)
        return res

    @classmethod
    def replace_one(cls, data_replace, data_options):
        res = cls.collection().replace_one(data_replace, data_options)
        return res

    @classmethod
    def delete_one(cls, data):
        if data.get('_id'):
            data = {'_id':data.get('_id')}
        res = cls.collection().delete_one(data)
        return res

    @classmethod
    def delete_many(cls, data={}):
        if isinstance(data,list):
            for d in data:
                cls.delete_one(d)
            return True
        res = cls.collection().delete_many(data)
        return res

    @classmethod
    def find_all(cls):
        res = cls.collection().find()
        return [r for r in res]

    @classmethod
    def query_all(cls,**kwargs):
        res = cls.collection().find(**kwargs)
        arr = []
        for d in res:
            arr.append(copy(cls)(**d))
        return arr

    @classmethod
    def relationship(cls, table_name):
        pass

