from wtforms import StringField, FileField, Form
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

from app import photos
from app.forms.baseform import BaseForm


class InfoForm(BaseForm):

    title = StringField(validators=[
        DataRequired(message='请输入标题'),
        Length(1, 30)])

    category = StringField(validators=[
        Length(0, 10)])

    location = StringField(validators=[
        DataRequired(message='请输入校区'),
        Length(4, 10, message='长度必须大于4小于10')
    ])

    description = StringField(validators=[
        Length(max=256, message='描述长度请不要256个字符')
    ])

    contact = StringField(validators=[  # the contact information the user left
        DataRequired(message='请输入联系人名称'),
        Length(2, 20, message='长度必须大于2小于20')
    ])

    contact_info = StringField(validators=[
        DataRequired(message='请输入联系方式'),
        Length(5, 20, message='长度必须大于5小于20')
    ])

    cardID = StringField(validators=[
        Length(0, 15, message='长度必须大于0小于15')
    ])

    kind = StringField(validators=[
        DataRequired(),
        Length(3, 6, message='未传入kind信息')
    ])

    photo = FileField(u'图片上传', validators=[
        FileAllowed(photos, message=u'只能上传图片！'),
        #FileRequired(message=u'文件未选择！')
    ])






