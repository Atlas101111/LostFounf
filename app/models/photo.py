from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Photo(Base):
    photoID = Column(Integer, primary_key=True, autoincrement=True)
    photoURL = Column(String(256), nullable=False)    # Url of this photo
    info = relationship('Info', backref='photo')
    info_id = Column(Integer, ForeignKey('info.id'))

    @property
    def data(self):
        URL_data = []
        for url in self.photoURL:
            URL_data.append(url)
        return URL_data
        pass

    def keys(self):
        return ['photoURL']








