from flask import request, jsonify
from flask_login import login_user

from app import db
from app.models.user import User
from app.models.user_bind import UserBind
from app.spider.login_spider import LoginSpider
from app.web import web


@web.route('/web/login', methods=['POST'])
def login():
    response = {'code': 200, 'msg': '登录成功', 'data': {}}
    request_value = request.values
    code = request_value['code'] if 'code' in request_value else ''
    if not code or len(code) < 1:
        response['code'] = -1
        response['msg'] = '登录失败, 未得到code凭证'
        return jsonify(response)

    # spider = LoginSpider()   # spider is loaded with openid
    # spider.get_openid(code)
    # result = UserBind.in_table(spider.openID)  # result is a record
    Test_openid = '119'
    result = UserBind.in_table(Test_openid)

    if result:   # user's openid has been bound
        # login procedure
        login_user(result.user, remember=True)
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
        with db.auto_commit():
            user_bind = UserBind()
            #user_bind.openid = spider.openID          ################
            user_bind.openid = Test_openid
            user_bind.user = user
            # Mind this statement, not sure if it can work
            db.session.add(user_bind)

        login_user(user, remember=True)
        response['data'] = {    # response after the register procedure
            'gender': user.gender,
            'nickName': user.nickname,
            'id': user.id,
            'avatarUrl': user.avatarUrl
        }
    return jsonify(response)











