from datetime import datetime

from flask import current_app
from sqlalchemy import Column, Integer, Boolean, desc

from app.models import db


class Base(db.Model):
    __abstract__ = True
    status = Column(Boolean, nullable=False, default=True)  # deleted or not
    create_time = Column('create_time', Integer)     # timestamp

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):  # this method is to use dict to set attr for every class
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):  # create_datetime records the time using original date form
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None


