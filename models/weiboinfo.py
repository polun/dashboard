# -*- coding: utf-8 -*-

from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class WeiboInfo(Base):
    """微博信息表"""

    __tablename__ = 'weiboinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    access_token = Column(String(50))
    remind_in = Column(Integer)
    expires_in = Column(Integer)
    uid = Column(String(20))
    create_time = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<WeiboInfo(access_token='%s', remind_in='%s', expires_in='%s', expires_in='%s', create_time='%s')>" \
            % (self.access_token, self.remind_in, self.expires_in, self.uid, self.create_time)
