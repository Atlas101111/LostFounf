from flask import jsonify, request
from flask_login import login_required

from app.api import api
from app.forms.query_form import QueryForm
from app.models.found_info import FoundInfo
from app.models.infos import Info
from app.models.lost_info import LostInfo
from app.view_models.query_model import QueryModelCollection


@api.route('/query', methods=['GET'])
#@login_required
def query():
    form = QueryForm()
    keyword = form.q.data
    kind = form.kind.data

    result = Info.query_by_keyword(keyword)

    if result is None:
        result = "No result"
        return jsonify(result)

    query_model = QueryModelCollection()
    query_model.fill(result, form.q.data)

    return jsonify(query_model)
    pass


@api.route('/recent', methods=['GET'])
def recent_info():

    result = Info.recent()

    if result is None:
        result = "No result"
        return jsonify(result)

    query_model = QueryModelCollection()
    query_model.fill(result, 'recent')

    return jsonify(query_model)


@api.route('/my', methods=['GET'])
@login_required
def my_post():

    result = Info.my()

    if result is None:
        result = "No result"
        return jsonify(result)

    query_model = QueryModelCollection()
    query_model.fill(result, 'my')

    return jsonify(query_model)
    pass
