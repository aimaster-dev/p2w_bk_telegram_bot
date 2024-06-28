# -*- coding: utf-8 -*-
import os
import base64
import shortuuid
from flask_cors import CORS
from importlib import import_module
from flask import Flask, request, abort, make_response, send_file, render_template
from site_exts import db
from constants import ASSETS_FOLDER, MAX_CONTENT_LENGTH, PUBLIC_FOLDER
from common_utils import xtjson


def create_app(config):
    app = Flask(__name__, static_folder=None)
    app.static_folder = "static"
    CORS(app, supports_credentials=True, cors_allowed_origins="*")
    app.config.update({'DEBUG': True, 'WTF_CSRF_ENABLED': True, 'PROJECT_NAME': config.PROJECT_NAME, 'MAIN_DOMAIN': config.MAIN_DOMAIN, 'MAX_CONTENT_LENGTH': MAX_CONTENT_LENGTH})

    db.init_app(config)

    SCHEDULER_API_ENABLED = True
    app.config.update({'SCHEDULER_API_ENABLED': SCHEDULER_API_ENABLED})

    def init_data():
        SiteConfig = getattr(db.database, 'site_config_table')
        site_data = SiteConfig.find_one({'project_name': config.PROJECT_NAME}) or {}
        if not site_data:
            site_data['uuid'] = shortuuid.uuid()
            site_data['project_name'] = config.PROJECT_NAME
            site_data['secret_key'] = base64.b64encode(os.urandom(66)).decode()
            site_data['cms_prefix'] = ''
            site_data['site_domain'] = ''
            SiteConfig.insert_one(site_data)
        result_config = {
            'PROJECT_UUID': site_data.get('uuid'),
            'SECRET_KEY': site_data.get('secret_key'),
            'PROJECT_NAME': site_data.get('project_name'),
        }
        return result_config
    app.config.update(init_data())

    project_static_root = '%s/%s/%s' % (app.static_folder, config.PROJECT_NAME, ASSETS_FOLDER)
    if not os.path.exists(project_static_root):
        os.makedirs(project_static_root)

    registed_view = import_module(f'{config.PROJECT_NAME}.register_view')
    if not hasattr(registed_view, 'front_bp'):
        print('无前端视图模块！')
        exit()
    if not hasattr(registed_view, 'cms_bp'):
        print('无后端视图模块！')
        exit()
    if not hasattr(registed_view, 'common_bp'):
        print('无公共视图模块！')
        exit()
    if not hasattr(registed_view, 'api_bp'):
        print('无API视图模块！')
        exit()
    if not hasattr(registed_view, 'merchant_bp'):
        print('无MERCHANT视图模块！')
        exit()

    app.register_blueprint(getattr(registed_view, 'front_bp'))
    app.register_blueprint(getattr(registed_view, 'common_bp'))
    app.register_blueprint(getattr(registed_view, 'cms_bp'))
    app.register_blueprint(getattr(registed_view, 'api_bp'))
    app.register_blueprint(getattr(registed_view, 'merchant_bp'))

    @app.route('/static/<path:filename>')
    def static(filename=None):
        if not filename or not filename.strip():
            return abort(403)
        if 'private' in filename or 'project_' in filename:
            return abort(403)
        project_static_file = os.path.join(app.static_folder, filename)
        if os.path.isdir(project_static_file.encode()):
            return abort(403)
        if os.path.exists(project_static_file.encode()):
            return make_response(send_file(project_static_file))
        return abort(404)

    @app.route('/assets/<path:filename>')
    def assets(filename):
        if not filename or not filename.strip():
            return abort(403)
        if 'private' in filename or 'project_' in filename:
            return abort(403)
        project_static_file = os.path.join(app.static_folder, config.PROJECT_NAME, ASSETS_FOLDER, filename)
        if os.path.exists(project_static_file):
            return make_response(send_file(project_static_file))
        return abort(403)

    @app.route('/public/<path:filename>')
    def public(filename):
        if not filename or not filename.strip():
            return abort(403)
        if 'private' in filename or 'project_' in filename:
            return abort(403)
        project_static_file = os.path.join(app.static_folder, config.PROJECT_NAME, PUBLIC_FOLDER, filename)
        if os.path.exists(project_static_file):
            return make_response(send_file(project_static_file))
        return abort(403)

    @app.route('/assets/world/<path:filename>')
    def assetsChat(filename):
        if not filename or not filename.strip():
            return abort(403)
        if 'private' in filename or 'project_' in filename or 'backup' in filename:
            return abort(403)
        project_static_file = os.path.join(app.static_folder, 'pay2world', ASSETS_FOLDER, filename)
        if os.path.exists(project_static_file):
            return make_response(send_file(project_static_file))
        return abort(403)

    @app.route('/public/world/<path:filename>')
    def publicChat(filename):
        if not filename or not filename.strip():
            return abort(403)
        if 'private' in filename or 'project_' in filename:
            return abort(403)
        project_static_file = os.path.join(app.static_folder, 'pay2world', PUBLIC_FOLDER, filename)
        if os.path.exists(project_static_file):
            return make_response(send_file(project_static_file))
        return abort(403)

    @app.route('/favicon.ico')
    def icon():
        return ''

    def is_xhr():
        X_Requested_With = request.headers.get('X-Requested-With')
        if not X_Requested_With or X_Requested_With.lower() != 'xmlhttprequest':
            return
        return True

    @app.errorhandler(401)
    def cms_no_auth(error):
        if is_xhr():
            return xtjson.json_unauth_error('401,没有权限！')
        return '401,没有权限', 401

    @app.errorhandler(403)
    def cms_not_file(error):
        if is_xhr():
            return xtjson.json_params_error()
        return '403,资源不可用！', 403

    @app.errorhandler(404)
    def cms_not_fount(error):
        if is_xhr():
            return xtjson.json_params_error('404')
        # if hasattr(SITE_CONFIG_CACHE,'html_404'):
        #     return render_template_string(SITE_CONFIG_CACHE.html_404), 404
        return render_template('common/404.html'), 404

    @app.errorhandler(405)
    def error_method(error):
        if is_xhr():
            return xtjson.json_method_error('405, 请求方法错误！')
        return '405,请求方法错误', 405

    @app.errorhandler(500)
    def error_method500(error):
        if is_xhr():
            return xtjson.json_method_error('500, 服务器出错！')
        return '500,服务器出错!', 500

    return app
