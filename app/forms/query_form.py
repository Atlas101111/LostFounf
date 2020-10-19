from flask import request
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from app.forms.baseform import BaseForm


class QueryForm(BaseForm):
    q = StringField(validators=[
        DataRequired(),
        Length(1, 15)
    ])

    kind = StringField(validators=[
        Length(1, 5)
    ])
    pass


