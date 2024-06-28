# -*- coding:utf-8 -*-
import os
from pymongo import MongoClient


class Roles(object):
    """数据库角色权限"""
    root = 'root'
    dbOwner = 'dbOwner'
    readWrite = 'readWrite'
    read = 'read'

    explain_dict = {
        root : u'超级用户权限',
        dbOwner : u'当前db执行操作',
        readWrite : u'允许读写指定数据库',
        read : u'允许读指定数据库'
    }


class CONFIG(object):
    """配置"""
    db_name = 'admin'
    root_username = 'root'
    root_password = 'wlanan@root_251275'


class MongoManage(object):

    def __init__(self, username='root', password='', host='127.0.0.1:27017', db_name='admin', uri=None):
        """
        :param username: 用户名
        :param password: 密码
        :param host: 数据库地址
        :param db_name: 要进行身份验证的数据库
        :param uri: 数据库URL链接地址
        """
        self.host = [host]
        self.db_name = db_name
        self.username = username
        self.password = password
        self.db_admin = None
        self.admin_collection = None
        if uri:
            self.connect = MongoClient(uri)
        elif self.username and self.password:
            self.connect = MongoClient(self.host, authSource=db_name, username=username, password=password)
        else:
            self.connect = MongoClient(self.host)
        if db_name == 'admin' and username == 'root':
            self.db_admin = getattr(self.connect, db_name)
            self.admin_collection = getattr(self.db_admin, 'system.users')

    def find_many(self, match, **kwargs):
        """
        数据查询：更多数据
        :param match: 查询条件
        :param kwargs:
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户！')
        res = self.admin_collection.find(match, **kwargs)
        return res

    def database_info(self, db_name):
        """
        获取所有的数据库列表，并判断该数据库是否存在
        :param db_name: 数据库名称
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户!')
        for d in self.connect.list_databases():
            if db_name == d.get('name'):
                return d
        return None

    def database_names(self):
        """
        获取数据库名称
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户！')
        try:
            return self.connect.list_database_names()
        except Exception as e:
            return str(e)

    def drop_database(self, db_name):
        """
        删除数据库
        :param db_name: 数据库名称
        :return:
        """
        if self.db_name == db_name:
            return self.connect.drop_database(db_name)
        if self.db_admin is None:
            raise ValueError(u'非root用户！')
        self.connect.drop_database(db_name)
        for u in self.find_many({'db': db_name}):
            self.dropUser(db_name, u.get('user'))
        return 'success'

    def list_collections(self, db_name):
        """
        获取数据库内的所有表
        :param db_name: 数据库名称
        :return:
        """
        return getattr(self.connect, db_name).list_collections()

    def get_collection(self, db_name, name):
        """获取数据表对象"""
        return getattr(self.connect, db_name).get_collection(name)

    def drop_collection(self, db_name, name):
        """
        删除数据表
        :param db_name: 数据库名称
        :param name: 数据表名称
        :return:
        """
        if self.db_name == db_name:
            return getattr(self.connect, db_name).drop_collection(name)
        if self.db_admin is None:
            raise ValueError(u'非root用户!')
        try:
            return getattr(self.connect, db_name).drop_collection(name)
        except Exception as e:
            return str(e)

    def initRootAdmin(self, password=''):
        """
        初始化：root用户
        :param password: ROOT用户密码
        :return:
        """
        if self.password:
            raise ValueError(u'初始化root用户, 禁止传 password!')
        if self.db_admin is None:
            raise ValueError(u'非root用户!')
        if not password:
            password = 'admin'
        try:
            return self.db_admin.command('createUser', 'root', pwd=password, roles=[Roles.root])
        except Exception as e:
            return str(e)

    def createUser(self, db_name, username, password, role=[]):
        """
        创建指定数据库用户
        :param db_name: 数据库名称
        :param username: 用户名称
        :param password: 密码
        :param role: 角色权限
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户!')
        if not role:
            role = [Roles.dbOwner]
        db = getattr(self.connect, db_name)
        if not self.database_info(db_name):
            db.default.insert_one({'creatr_statu': 'ok'})
        try:
            return db.command('createUser', username, pwd=password, roles=role)
        except Exception as e:
            return str(e)

    def dropUser(self, db_name, username):
        """
        删除用户
        :param db_name: 数据库名称
        :param username: 用户名
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户!')
        db = getattr(self.connect, db_name)
        try:
            return db.command('dropUser', username)
        except Exception as e:
            return str(e)

    def updateUsert(self, db_name, username, nowpassword):
        """
        更新用户
        :param db_name: 数据库名称
        :param username: 用户名
        :param nowpassword: 新密码
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户!')
        db = getattr(self.connect, db_name)
        try:
            return db.command('updateUser', username, pwd=nowpassword)
        except Exception as e:
            return str(e)

    def updateUserRoles(self, db_name, username, roles=Roles.dbOwner):
        """
        更新用户权限
        :param db_name: 数据库名称
        :param username: 用户名称
        :param roles: 角色权限
        :return:
        """
        if self.db_admin is None:
            raise ValueError(u'非root用户！')
        if not isinstance(roles, list):
            raise ValueError(u'参数类型错误!')
        db = getattr(self.connect, db_name)
        try:
            return db.command('updateUser', username, roles=roles)
        except Exception as e:
            return str(e)

    def mongodump(self, mongodump_path, goal_path):
        """
        数据库备份
        :param mongodump_path:
        :param goal_path:
        :return:
        """
        try:
            if not os.popen('%s --help' % mongodump_path):
                print(u'mongodump文件错误!')
                exit()
        except Exception as e:
            print(str(e))
            exit()
        if not os.path.exists(goal_path):
            print(u'%s 路径错误!'%goal_path)
            exit()
        try:
            cmd = ''
            cmd += mongodump_path
            cmd += ' -h ' + self.host[0]
            cmd += ' -u ' + self.username
            cmd += ' -p ' + self.password
            cmd += ' -d ' + self.db_name
            cmd += ' -o ' + goal_path
            results = os.popen(cmd).read()
            print('results:', results)
            cmd = mongodump_path
            if cmd.endswith('/'):
                cmd += self.db_name
            else:
                cmd+= '/' + self.db_name
            if not results or not os.path.exists(cmd):
                print(u'备份失败!')
                exit()
            print(u'备份成功，文件路径：' + cmd)
        except Exception as e:
            print(str(e))
            exit()

    def mongorestore(self, mongorestore_path, dump_path, drop_current=False):
        """
        数据库数据备份恢复
        :param mongorestore_path:
        :param dump_path:
        :param drop_current:
        :return:
        """
        if drop_current not in [True, False]:
            raise ValueError('drop_current is True or False!')
        try:
            if not os.popen('%s -- help' % mongorestore_path):
                print(u'mongorestore 文件错误!')
                exit()
            if not os.path.exists(dump_path):
                print(u'备份文件路径错误!')
                exit()
            cmd = ''
            cmd += mongorestore_path
            cmd += ' -h ' + self.host[0]
            cmd += ' -u ' + self.username
            cmd += ' -p ' + self.password
            cmd += ' -d ' + self.db_name
            if drop_current:
                cmd += ' --drop '
            cmd += dump_path
            results = os.popen(cmd).read()
            if not results:
                print(u'恢复数据失败!')
                exit()
            print(u'恢复数据成功!')
        except Exception as e:
            print(str(e))


# import sys
# sys.path.append('/www/pay2world')
# from project_pay2world import ProjectConfig
# db = MongoManage(username=CONFIG.root_username)
# print(db.initRootAdmin(CONFIG.root_password))
# db = MongoManage(username=CONFIG.root_username, password=CONFIG.root_password)
# print(db.createUser(ProjectConfig.MONGODB_DB, ProjectConfig.MONGODB_USERNAME, ProjectConfig.MONGODB_PASSWORD, role=[Roles.read]))
