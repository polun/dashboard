# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    return '主页'

if __name__ == '__main__':
    app.run(debug=True, port=8090)
