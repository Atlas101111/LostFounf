from flask import current_app
from werkzeug import http

from app.libs.http import Http


class LoginSpider:   # LoginSpider can use the login code of the user to get his or her openid
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code'

    def __init__(self):
        self.openID = ''
        self.session_key = ''
        self.unionID = ''
        self.errcode = 0
        self.errmsg = ''

    def get_openid(self, code):
        url = self.url.format(current_app.config['APPID'], current_app.config['SECRET'], code)
        result = Http.get(url)
        self.fill(result)

    def fill(self, data):
        if data:
            self.openID = data['openid']
            self.session_key = data['session_key']
            self.unionID = data['unionid']
            self.errcode = data['errcode']
            self.errmsg = data['errmsg']

