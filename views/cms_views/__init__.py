# -*- coding: utf-8 -*-
from flask import Blueprint
from functools import wraps

bp = Blueprint('admin', __name__, url_prefix='/pay2Admin')


def front_login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
            return func(*args,**kwargs)
    return wrapper
