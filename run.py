# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

redirect_uri = 'http://e777737c.ngrok.io/weibo/redirectURI'
auth_url = 'https://api.weibo.com/oauth2/authorize?client_id=4177092657&response_type=code&redirect_uri=' + redirect_uri
token_url = 'https://api.weibo.com/oauth2/access_token?client_id=4177092657&client_secret=1bf707cc2ae50bf6ab342987a0fb6769&grant_type=authorization_code&redirect_uri=' + redirect_uri + '&code='
weibo_favorite_api = 'https://api.weibo.com/2/favorites.json?access_token=2.00RSk2CCNcegYE6f521e9f9bxfAqaE&count=20&page=1'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/weibo_favorite')
def weibo_favorite():
    global weibo_favorite
    res = requests.get(weibo_favorite_api)
    res.text

    return render_template('weibo_favorite.html', favorites=res.text)

@app.route('/weibo/redirectURI')
def weibo_redirectURI():
    global token_url
    code = request.args.get('code')
    token_url = token_url + code

    print token_url
    res = requests.post(token_url)
    print res.text
    return render_template('weibo_favorite.html')

if __name__ == '__main__':
    app.run(debug=True, port=8090, host='0.0.0.0')
