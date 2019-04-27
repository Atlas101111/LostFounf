from flask import request

from app.web import web


@web.route('/query/cluster', methods=['POST', 'GET'])
def query_cluster():
    response = {'code': 200, 'msg': '查询成功', 'data': {}}
    request_value = request.values
    if request.method == 'GET':
        request_value
        pass


@web.route('/query/single', methods=['POST', 'GET'])
def query_cluster():
    response = {'code': 200, 'msg': '查询成功', 'data': {}}
    request_value = request.values
    if request.method == 'GET':
        request_value
        pass


