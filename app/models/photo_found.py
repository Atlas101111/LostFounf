from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class PhotoFound(Base):
    photoID = Column(Integer, primary_key=True, autoincrement=True)
    photoURL = Column(String(256), nullable=False)    # Url of this photo in file system
    found_info = relationship('FoundInfo', backref='photo')
    info_id = Column(Integer, ForeignKey('found_info.id'))

    @property
    def data(self):
        URL_data = []
        for url in self.photoURL:
            URL_data.append(url)
        return URL_data
        pass

    def keys(self):
        return ['photoURL']








