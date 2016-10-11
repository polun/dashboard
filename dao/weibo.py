# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'
db = SQLAlchemy(app)

class Weibo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    access_token = db.Column(db.String(80), unique=True)
    remind_in = db.Column(db.Integer, unique=False)
    expires_in = db.Column(db.Integer, unique=False)
    uid = db.Column(db.String(20), unique=True)

    def __init__(self, access_token, remind_in, expires_in, uid):
        self.access_token = access_token
        self.remind_in = remind_in
        self.expires_in = expires_in
        self.uid = uid


class WeiboDao(object):
    """ 表crud """

    def add(self, weibo):
        weibo = Weibo('2.00RSk2CCNcegYE6f521e9f9bxfAqaE', 157679999, 157679999, '1867001181')
        db.session.add(weibo)
        db.session.commit()

    def get(self, id):
        return Weibo.query.filter_by(id=1).first()
        # print db
        
        # return None
