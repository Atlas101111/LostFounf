from wtforms import StringField, FileField, Form
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LostInfoForm(Form):
    title = StringField(validators=[
        DataRequired(message='No title'),
        Length(1, 30)])

    category = StringField(validators=[
        DataRequired(message='No category'),
        Length(1, 10)])

    location = StringField(validators=[
        DataRequired(message='No location'),
        Length(4, 10)])

    description = StringField(validators=[
        Length(0, 256)])

    contact = StringField(validators=[
        Length(0, 20)])

    picture = FileField(validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'])
    ])


