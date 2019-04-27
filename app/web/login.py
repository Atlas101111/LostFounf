from flask import request, jsonify

from app import db
from app.models.user import User
from app.models.user_bind import UserBind
from app.spider.login_spider import LoginSpider
from app.web import web


@web.route('/login', methods=['POST', 'GET'])
def login():
    response = {'code': 200, 'msg': '登录成功', 'data': {}}
    request_value = request.values
    code = request_value['code'] if 'code' in request_value else ''
    if not code or len(code) < 1:
        response['code'] = -1
        response['msg'] = '登录失败'
        return jsonify(response)

    spider = LoginSpider()   # spider is loaded with openid
    spider.get_openid(code)
    result = UserBind.in_table(spider.openID)  # result is a record
    if result:   # user's openid has been bound
        # login procedure
        response['data'] = {
            'gender': result.user.gender,
            'nickName': result.user.nickname,
            'id': result.user.id,
            'avatarUrl': result.user.avatarUrl
        }
    else:   # register procedure
        with db.auto_commit():
            user = User()
            user.nickname = request_value['nickName']
            user.gender = request_value['gender']
            user.avatarUrl = request_value['avatarUrl']
            db.session.add(user)

            user_bind = UserBind()
            user_bind.openid = spider.openID
            user_bind.uid = user.id   # Mind this statement, not sure if it can work
            user_bind.user = user
            db.session.add(user_bind)

        response['data'] = {
            'gender': user.gender,
            'nickName': user.nickname,
            'id': user.id,
            'avatarUrl': user.avatarUrl
        }
    return jsonify(response)











