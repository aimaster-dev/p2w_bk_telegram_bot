# -*- coding: utf-8 -*-
import os, datetime, random
from flask import current_app, request


class UploadCls(object):
    uploaddir = 'upload'                # 上传的文件夹名称
    foldername = ''                     # 上传文件的父级文件夹名称
    filename = ''                       # 文件名
    limit_types = []                    # 文件类型限制
    static_folder = 'static'            # 项目静态文件夹地址（相对地址）
    host = ''                           # host地址

    def gen_rnd_filename(self):
        filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return '%s%s' % (filename_prefix, str(random.randrange(0, 100)))

    def upload_file_func(self):
        """文章保存处理"""
        if 'upload' not in request.files:
            return False, u'上传失败!'
        error, url = '', ''
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        static_folder_path = os.path.join(current_app.root_path, self.static_folder.strip('/'))
        if not os.path.exists(static_folder_path):
            error = u'目录不存在！'
        else:
            upload_path = static_folder_path
            if self.uploaddir:
                upload_path = '%s/%s' % (static_folder_path, self.uploaddir)
                if not os.path.exists(upload_path):
                    try:
                        os.mkdir(upload_path)
                    except:
                        error = u'创建一级目录失败！'
            if not error:
                if self.limit_types.count(fext.lower()) == 1:
                    if not self.filename:
                        self.filename = '%s%s' % (self.gen_rnd_filename(), fext)
                    else:
                        if self.filename == 'customname':
                            self.filename = fname.replace(',','').replace('/','').replace('\\','')
                        self.filename = '%s%s' % (self.filename, fext)
                    if not self.foldername:
                        self.foldername = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                    if self.foldername[0] == '/':
                        self.foldername = self.foldername[1:]
                    if '/' in self.foldername:
                        tmp_arr = self.foldername.split('/')
                        for i in range(len(tmp_arr)):
                            if tmp_arr[i]:
                                tmp_folder1 = upload_path + '/' + '/'.join(tmp_arr[0:i])
                                if not os.path.exists(tmp_folder1):
                                    try:
                                        os.makedirs(tmp_folder1)
                                    except:
                                        error = u'创建多级目录失败'
                                        break
                    file_folder = upload_path + '/' + self.foldername
                    if not os.path.exists(file_folder):
                        try:
                            os.makedirs(file_folder)
                        except:
                            error = u'创建二级目录失败'
                    if not os.access(file_folder, os.W_OK):
                        error = u'目录不可写'
                    if not error:
                        filepath = file_folder + '/' + self.filename
                        if os.path.exists(filepath):
                            error = u'文件已存在！'
                        else:
                            fileobj.save(filepath)
                            url = filepath.replace(current_app.root_path + '/' + self.static_folder, '')
                            if self.host:
                                url = self.host + url
                else:
                    error = u'文件名不允许！'
        if error:
            return False, error
        return True, url

    def upload_way_run(self):
        editor_callback = request.args.get("CKEditorFuncNum")
        statu, res = self.upload_file_func()
        if editor_callback:
            kw = { "uploaded": 1, "fileName": self.filename, "url": res}
            ew = { "uploaded": 0, "error": { "message": res}}
            if statu:
                return True, kw
            return False, ew
        if statu:
            return True, res
        return False, res

