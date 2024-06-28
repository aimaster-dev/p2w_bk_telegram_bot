import os
import time
import json
import ftplib
from common_utils.lqredis import SiteRedis


class FtpCls:

    def __init__(self, host, user, pwd, port=21, dataKey='', total_count=''):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.dataKey = dataKey
        self.total_count = total_count
        self.ftp = ftplib.FTP()
        self.is_login = False

    def login(self):
        try:
            self.ftp.connect(host=self.host, port=self.port)
            self.ftp.login(user=self.user, passwd=self.pwd)
            self.is_login =True
            return True, ''
        except:
            return False, 'FTP连接失败！'

    def ftp_path_exists(self, remote_path, crr_path='/'):
        """ 判断是否存在 ftp 路径，同 os.path.exists()，但是只能判断 dir，不能判断 file。"""
        try:
            self.ftp.cwd(remote_path)  # 能切换给定路径，说明存在
            self.ftp.cwd(crr_path)
            return True
        except:
            return False

    def check_link(self, remote_path):
        if not self.is_login:
            statu, res = self.login()
            if not statu:
                return statu, res

        if self.ftp_path_exists(remote_path):
            return True, ''

        return False, '远程文件夹不存在！'

    def ftp_file_exists(self, remote_file):
        """ 判断是否存在 ftp 文件，同 os.path.exists()，但是只能判断 file，不能判断 dir。"""
        try:
            self.ftp.size(remote_file)
            return True
        except:
            return False

    def create_mkd_folder(self, new_path):
        ''' 远程创建文件夹 '''
        if not self.is_login:
            statu, res = self.login()
            if not statu:
                return statu, res

        if not new_path.startswith('/'):
            new_path = '/' + new_path

        if self.ftp_path_exists(new_path):
            return True, ''

        try:
            self.ftp.mkd(new_path)
        except Exception as e:
            return False, '文件夹创建失败：' + str(e)

        return True, ''

    def delete_rmd_folder(self, file_path):
        ''' 远程删除文件夹 '''
        if not self.is_login:
            statu, res = self.login()
            if not statu:
                return statu, res

        if not file_path or not file_path.strip() or not file_path.strip('/'):
            return False, '文件夹路径错误！'

        if not file_path.startswith('/'):
            file_path = '/' + file_path

        if not self.ftp_path_exists(file_path):
            return True, ''

        try:
            self.ftp.rmd(file_path)
        except Exception as e:
            return False, '文件夹删除失败:' + str(e)

        return True, ''

    def delete_file(self, file_path):
        ''' 远程删除文件 '''
        if not self.is_login:
            statu, res = self.login()
            if not statu:
                return statu, res

        if not file_path or not file_path.strip() or not file_path.strip('/'):
            return False, '文件夹路径错误！'

        if not file_path.startswith('/'):
            file_path = '/' + file_path

        if not self.ftp_path_exists(file_path):
            return True, ''

        try:
            self.ftp.delete(file_path)
        except Exception as e:
            return False, '文件删除失败:' + str(e)

        return True, ''

    def get_remote_path(self, remote_path, file_list=None):
        """ 给定一个 ftp 文件夹路径，获取路径下的所有文件。"""
        file_infos = []
        self.ftp.cwd(remote_path.replace('\\', '/'))  # 切换到下载目录
        self.ftp.dir(remote_path.replace('\\', '/'), file_infos.append)  # 列出文件夹内容，存入列表
        for file_info in file_infos:
            if file_info.startswith('-'):  # 以 - 开始，为文件
                file_list.append(remote_path + '\\' + file_info.split(' ')[-1])
            if file_info.startswith('d'):  # 以 d 开始，为文件夹
                folder = file_info.split(' ')[-1]
                self.get_remote_path(remote_path + '\\' + folder, file_list)
        return file_list

    def download_tracker(self, block, f, dst):
        """ 下载回调函数，实现上传进度。"""
        f.write(block)
        global write_size, total_size
        write_size += 64 * 1024
        progress = round((write_size / total_size) * 100)
        if progress >= 100:
            # print('\rDownload ' + dst + ' ' + '100%', end='')
            if self.dataKey:
                _pdata = {
                    'statu': 'success',
                    'total_count': self.total_count,
                    'msg': '备份ftp远程下载完成！'
                }
                SiteRedis.set(self.dataKey, json.dumps(_pdata), expire=60*10)
        else:
            # print('\rDownload ' + dst + ' ' + '%3s%%' % str(progress or ''), end='')
            if self.dataKey:
                _pdata = {
                    'statu': 'jxz',
                    'total_count': self.total_count,
                    'msg': '备份ftp远程下载中：'+ '%3s%%' % str(progress or '')
                }
                SiteRedis.set(self.dataKey, json.dumps(_pdata), expire=60 * 10)

    def download_func(self, src, dst):
        """ 下载文件。"""
        global write_size, total_size
        write_size = 0
        total_size = self.ftp.size(src.replace('\\', '/'))
        blocksize = 64 * 1024
        with open(dst, 'wb') as f:
            self.ftp.retrbinary('RETR ' + src.replace('\\', '/'), lambda block: self.download_tracker(block, f, dst), blocksize)

    def downLoadFile(self, localpath, remotepath):
        ''' 下载文件 '''
        if not self.is_login:
            statu, res = self.login()
            if not statu:
                return statu, res

        if not self.ftp_file_exists(remotepath):
            return False, '远程文件不存在！'

        # bufsize = 1024
        # with open(localpath, 'wb') as wf:
        #     self.ftp.retrbinary('RETR ' + remotepath, wf.write, bufsize)
        # self.ftp.set_debuglevel(0)
        # try:
        self.download_func(remotepath, localpath)
        # except:
        #     return False, '文件下载失败！'

        return True, '文件下载成功！'

    def upload_tracker(self, block, dst):
        """ 上传回调函数，实现上传进度。"""
        global write_size, total_size
        write_size += 64 * 1024  # 文件每次写入的大小，用来实现进度条，必须和 blocksize 大小一样
        progress = round((write_size / total_size) * 100)
        if progress >= 100:
            # print('\rUpload ' + dst + ' ' + '100%', end='')
            if self.dataKey:
                _pdata = {
                    'statu': 'jxz',
                    'msg': '备份ftp远程上传完成！'
                }
                SiteRedis.set(self.dataKey, json.dumps(_pdata), expire=60*10)
        else:
            # print('\rUpload ' + dst + ' ' + '%3s%%' % str(progress or ''), end='')
            if self.dataKey:
                _pdata = {
                    'statu': 'jxz',
                    'msg': '备份ftp远程上传中， 上传进度：%3s%%' % str(progress)
                }
                SiteRedis.set(self.dataKey, json.dumps(_pdata), expire=60*20)

    def upload_func(self, src, dst):
        global write_size, total_size
        write_size = 0  # 文件每次写入的大小，初始为 0
        total_size = os.path.getsize(src.replace('\\', '/'))
        blocksize = 64 * 1024  # 文件每次写入缓冲区的大小，64 KB
        with open(src, "rb") as f:
            self.ftp.storbinary('STOR ' + dst.replace('\\', '/'), f, blocksize, lambda block: self.upload_tracker(block, dst))

    def uploadFile(self, localpath, remotepath):
        ''' 上传文件 '''
        if not self.is_login:
            statu, res = self.login()
            if not statu:
                return statu, res
        try:
            self.upload_func(localpath, remotepath)
        except:
        #     _pdata = {
        #         'statu': 'error',
        #         'msg': '备份还原失败！'
        #     }
        #     SiteRedis.set(self.dataKey, json.dumps(_pdata), expire=60 * 20)
            return False, '文件上传失败！'

        return True, '文件上传成功！'

    def test_run(self):
        ftpcls = FtpCls(
            host='202.92.4.97',
            user='mnnqywkdhosting',
            pwd='iN3@TxLbupVR66A'
        )
        print(ftpcls.uploadFile('', ''))
        # print(ftpcls.downLoadFile('./2030809.zip', '/project_analysis_backup/20230809.zip'))

