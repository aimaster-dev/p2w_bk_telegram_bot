# -*- coding: utf-8 -*-
from flask import Blueprint
from constants import URL_PREFIX

bp = Blueprint('common', __name__, url_prefix=URL_PREFIX.COMMON_PREFIX)
