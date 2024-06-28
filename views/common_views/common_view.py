# -*- coding: utf-8 -*-
from . import bp
from common_utils.utils_funcs import graph_captcha



@bp.route('/img_cap/')
def img_cap():
    return graph_captcha()

