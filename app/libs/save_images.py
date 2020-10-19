import hashlib
import time
from flask_login import current_user

from app import photos


class SaveImages:

    @classmethod
    def save_images(cls, files):  # this will return a list of url of photos
        images = []
        for img in files:
            # filename = hashlib.md5(current_user.username + str(time.time())).encode('UTF-8')
            # print(img)
            filename = hashlib.md5(str(time.time()).encode('UTF-8')).hexdigest()[:15]
            print(filename)
            name = photos.save(img, name=filename+'.')
            file_url = photos.url(name)
            print(file_url)
            images.append(file_url)
        return images
    pass



