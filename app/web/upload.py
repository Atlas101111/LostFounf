from flask import request, jsonify, flash, current_app
from flask_login import login_required, current_user

from app import photos, db
from app.forms.info_form import InfoForm
from app.libs.save_images import SaveImages
from app.models.infos import Info
from app.models.photo import Photo
from app.web import web


@web.route('/web/upload', methods=['POST'])
#@login_required
def upload():
    response = {'code': 200, 'msg': '上传成功', 'data': {}}
    form = InfoForm()
    if form.validate():
        with db.auto_commit():
            info = Info()
            info.upload(form)
            db.session.add(info)
        with db.auto_commit():
            if request.files:
                urls = SaveImages.save_images(request.files.getlist('photo'))
            else:
                if form.kind.data == 'Lost':
                    urls = [current_app.config['DEFAULT_PHOTO_LOST']]
                else:
                    urls = [current_app.config['DEFAULT_PHOTO_FOUND']]
            for url in urls:
                photo = Photo()
                photo.info = info
                photo.photoURL = url
                db.session.add(photo)

    else:
        response['data'] = {'errors': form.errors}
        response['code'] = 1023
        response['msg'] = '表格参数验证失败'

    return jsonify(response)



# elif request_value['kind'] == 'Found':
        #     with db.auto_commit():
        #         found_info = FoundInfo()
        #         found_info.upload(form)
        #         db.session.add(found_info)
        #     with db.auto_commit():
        #         if request.files:
        #             urls = SaveImages.save_images(request.files.getlist('photo'))
        #         else:
        #             urls = [current_app.config['DEFAULT_PHOTO_LOST']]
        #         for url in urls:
        #             photo = PhotoFound()
        #             photo.found_info = found_info
        #             photo.photoURL = url
        #             db.session.add(photo)
