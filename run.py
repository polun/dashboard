# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/weibo_favorite')
def weibo_favorite():
    return render_template('weibo_favorite.html')

if __name__ == '__main__':
    app.run(debug=True, port=8090)
