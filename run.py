# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

redirect_uri = 'http://123.56.226.235:8090/weibo/redirectURI'
auth_url = 'https://api.weibo.com/oauth2/authorize?client_id=4177092657\
    &response_type=code&redirect_uri=' + redirect_uri
token_url = 'https://api.weibo.com/oauth2/access_token?client_id=4177092657&\
    client_secret=1bf707cc2ae50bf6ab342987a0fb6769&\
    grant_type=authorization_code&\
    redirect_uri=' + redirect_uri + '&code='

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/weibo_favorite')
def weibo_favorite():
    return redirect(auth_url, code=302)

@app.route('/weibo/redirectURI')
def weibo_redirectURI():
    code = request.args.get('code')
    token_url = token_url + code
    return redirect(token_url, code=302)

if __name__ == '__main__':
    app.run(debug=True, port=8090, host='0.0.0.0')
