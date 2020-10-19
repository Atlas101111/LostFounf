from flask import current_app
from werkzeug import http

from app.libs.http import Http


class LoginSpider:   # LoginSpider can use the login code of the user to get his or her openid
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'

    def __init__(self):
        self.openID = ''
        self.session_key = ''
        self.unionID = ''
        self.errcode = 0
        self.errmsg = ''

    def get_openid(self, code):
        url = self.url.format(current_app.config['APP_ID'], current_app.config['SECRET'], code)
        # print(url)
        result = Http.get(url)
        print(result)
        try:
            self.fill(result)
        except KeyError:
            print("Invalid response form WeChat Server")

    def fill(self, data):
        if data:
            if data.__contains__('openid'):
                self.openID = data['openid']
                self.session_key = data['session_key']
            #self.openID = '110'
            elif data.__contains__('errcode'):
                self.errcode = data['errcode']
                self.errmsg = data['errmsg']
                print(self.errcode)
                print(self.errmsg)
            else:
                raise KeyError


