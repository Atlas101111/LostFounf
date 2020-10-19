from flask import request
from wtforms import Form


class BaseForm(Form):
    def __init__(self):
        data = request.form
        args = request.args.to_dict()
        # print(data)
        super(BaseForm, self).__init__(data, **args)

    pass


