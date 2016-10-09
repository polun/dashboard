# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

auth_url = 'https://api.weibo.com/oauth2/authorize?client_id=4177092657\
    &response_type=code&redirect_uri=http://123.56.226.235:8090/weibo/redirectURI'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/weibo_favorite')
def weibo_favorite():
    return redirect(auth_url, code=302)
    return render_template('weibo_favorite.html')

@app.route('/weibo/redirectURI')
def weibo_redirectURI():
    code = request.args.get('code')
    print code
    return render_template("weibo_favorite.html")

if __name__ == '__main__':
    app.run(debug=True, port=8090, host='0.0.0.0')
