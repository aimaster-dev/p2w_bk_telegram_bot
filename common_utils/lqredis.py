#coding:utf8
import json
from site_exts import mc


class SiteRedis(object):

    # string操作
    @classmethod
    def get_keys(cls,key=''):
        if key:
            return mc.keys(key)
        return mc.keys()

    @classmethod
    def get(cls,name):
        return mc.get(name)

    @classmethod
    def set(cls,name,value,expire=None):
        if isinstance(value,dict):
            data_str = cls.dicttojson(value)
        else:
            data_str = value
        mc.set(name,data_str,expire)
        return True

    @classmethod
    def dele(cls, name):
        if '*' == name:
            for key in mc.keys(name):
                mc.delete(key)
        mc.delete(name)

    @classmethod
    def rename(self,name, rename):
        return mc.rename(name, rename)

    @classmethod
    def incrby(cls,name, amount=None):
        if not amount:
            return mc.incr(name)
        return mc.incr(name, amount)

    @classmethod
    def incrby_float(self, name, value='', amount=1.0):
        if not value:
            return mc.incr(name)
        return mc.incr(name,value)

    @classmethod
    def decr(self, name, value, amount=1):
        if not value:
            return mc.decr(name)
        return mc.decr(name,value)

    @classmethod
    def add_append(self, name, value):
        return mc.append(name, value)

    @classmethod
    def expire(cls, name, time):
        mc.expire(name=name, time=time)


    # Hash操作
    @classmethod
    def hset(cls, name, key, value):
        return mc.hset(name, key, value)

    @classmethod
    def hget(cls, name, key):
        return mc.hget(name, key)

    @classmethod
    def hmset(cls, name, data_dict):
        if not isinstance(data_dict,dict):
            return
        return mc.hmset(name, data_dict)

    @classmethod
    def hgetall(cls, name):
        return mc.hgetall(name)

    @classmethod
    def hlen(cls, name):
        return mc.hlen(name)

    @classmethod
    def hkeys(cls,name):
        """
        获取所有的key
        :return: []
        """
        return mc.hkeys(name)

    @classmethod
    def hvals(cls,name):
        """
        获取所有的value
        :return: []
        """
        return mc.hvals(name)

    @classmethod
    def hexists(cls, name, key):
        """
        判断name中是否存在 key
        :return: True or False
        """
        return mc.hexists(name, key)

    @classmethod
    def hdel(cls, name, key):
        """
        删除name中对应的key
        :return: 返回删除数量 或 0
        """
        return mc.hdel(name, key)

    @classmethod
    def hincrby(cls, name, key, amount_coun='', amount=1):
        if not amount_coun:
            return mc.amount(name, key)
        return mc.amount(name, key, amount_coun)

    @classmethod
    def hincrbyfloat(cls, name, key, amount_coun='', amount=1.0):
        if not amount_coun:
            return mc.amount(name, key)
        return mc.amount(name, key, amount_coun)

    @classmethod
    def hscan(cls, name, cursor=0, match=None, count=None):
        """
        增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
        :param name:
        :param cursor: 游标（基于游标分批取获取数据）
        :param match: 匹配指定key，默认None 表示所有的key
        :param count: 每次分片最少获取个数，默认None表示采用Redis的默认分片个数
        :return:
        """
        if not count:
            count = 10
        return mc.hscan(name, cursor=cursor, match=match, count=count)


    # List操作
    @classmethod
    def list_lpush(cls, name, value):
        """
        在name对应的list中添加元素，每个新的元素都添加到列表的最左边
        :return: 返回插入后的列表长度
        """
        if isinstance(value,list):
            for l in value:
                mc.lpush(name, l)
            return True
        return mc.lpush(name, value)

    @classmethod
    def list_lpushx(cls, name, value):
        """
        只有在name存在时添加
        :return: 列表长度
        """
        return mc.lpushx(name, value)

    @classmethod
    def list_lpop(cls, name):
        """
        rpop(name) 表示从右向左操作,在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
        :return:
        """
        return mc.lpop(name)

    @classmethod
    def list_blpop(cls, name, timeout=None):
        # 移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
        # brpop(keys, timeout)，从右向左获取数据
        return mc.blpop(name)

    @classmethod
    def list_llen(cls, name):
        """获取列表的长度"""
        return mc.llen(name)

    @classmethod
    def list_linsert(cls, name, where, refvalue, value):
        """
        在name对应的列表的某一个值前或后插入一个新值
        :param name:
        :param where: BEFORE或AFTER
        :param refvalue: 标杆值，即：在它前后插入数据
        :param value:
        :return:
        """
        return mc.linsert(name, where=where, refvalue=refvalue, value=value)

    @classmethod
    def list_lset(cls, name, index, value):
        """给键为name的列表中index位置的元素赋值，越界则报错"""
        return mc.lset(name, index, value)

    @classmethod
    def list_lrem(cls, name, value, num):
        """
        在name对应的list中删除指定的值
        :param num:num=0，删除列表中所有的指定值；num=2,从前到后，删除2个； num=-2,从后向前，删除2个
        :return:
        """
        return mc.lrem(name, value, num)

    @classmethod
    def lindex(self, name, index):
        return mc.lindex(name, index)

    @classmethod
    def list_ltrim(cls, name, start, end):
        """在name对应的列表中移除没有在start-end索引之间的值"""
        return mc.ltrim(name, start, end)

    @classmethod
    def list_rpoplpush(cls, src, dst):
        # 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
        # src，要取数据的列表的name
        # dst，要添加数据的列表的name
        return mc.rpoplpush(src, dst)

    @classmethod
    def lrange(cls, name, sta, end):
        """
        切片，获取区间内的数据，传入索引
        :return: []
        """
        return mc.lrange(name, sta, end)


    # 其他操作
    @classmethod
    def flushall(cls):
        """删除所有的键"""
        mc.flushall()

    @classmethod
    def getlist(cls,mcname):
        models = []
        for post in mc.lrange(mcname,0,-1):
            models.append(json.loads(post))
        return models

    @classmethod
    def jsontodict(cls, jsons):
        if jsons:
            try:
                return json.loads(jsons)
            except:
                return {}
        return {}

    @classmethod
    def json2todict(cls, jsons):
        if jsons:
            try:
                tmp_dict = {}
                for key, value in cls.jsontodict(jsons).iteritems():
                    try:
                        tmp_dict[key] = cls.jsontodict(value)
                    except:
                        tmp_dict[key] = value
                return tmp_dict
            except:
                return {}
        return {}

    @classmethod
    def dicttojson(cls, dic):
        if dic:
            return json.dumps(dic)
        return


