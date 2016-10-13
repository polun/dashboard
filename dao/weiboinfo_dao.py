# -*- coding: utf-8 -*-

from models import weiboinfo
from dao import session

class WeiboInfoDao():
    def get(self, id):
        return session.query(weiboinfo.WeiboInfo).filter_by(id=1).first()
        
    def add(self, entity):
        if not entity:
            raise Exception("entity 不能为空")

        session.add(entity)
        return session.commit()