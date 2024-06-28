# -*- coding: utf-8 -*-
from redis import StrictRedis
from common_utils.mongodb import MongoCLS


mc = StrictRedis(host='127.0.0.1', port=6379)
db = MongoCLS()

