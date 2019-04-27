from flask import request, jsonify

from app.spider.login_spider import LoginSpider
from . import api


@api.route("/api/user_info?code={}")
def user_info():   # user_info() is an api, which can return user's data using json format
    spider = LoginSpider()
    spider.get_openid(request.args)


