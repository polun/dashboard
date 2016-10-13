# -*- coding: utf-8 -*-

from dao.weiboinfo_dao import WeiboInfoDao
from models.weiboinfo import WeiboInfo, Base
from datetime import datetime

# weibo_info_dao = WeiboInfoDao()
# entity = WeiboInfo(access_token="2.00RSk2CCNcegYE6f521e9f9bxfAqaE", remind_in=157679999,expires_in=157679999, uid='1867001181')
# print weibo_info_dao.get(1)

format = '%a %b %d %H:%M:%S %z %Y'
print datetime.strptime('Wed Oct 12 10:46:55 +0800 2016', format)
# print datetime.strptime('Wed Oct 12 10:46:55 2016', format)