# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dashboard.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class WeiboInfo(Base):
    """微博信息表"""

    __tablename__ = 'weiboinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    access_token = Column(String(50))
    remind_in = Column(Integer)
    expires_in = Column(Integer)
    uid = Column(String(20))

    def __repr__(self):
        return "<WeiboInfo(access_token='%s', remind_in='%s', expires_in='%s', expires_in='%s')>" % (self.access_token, self.remind_in, self.expires_in, self.uid)

session = Session()
weibo_infos = session.query(WeiboInfo).filter_by(id=1).first()
print weibo_infos
# weibo_info = WeiboInfo(access_token="2.00RSk2CCNcegYE6f521e9f9bxfAqaE", remind_in=157679999,expires_in=157679999, uid='1867001181')
# session.add(weibo_info)
# session.commit()