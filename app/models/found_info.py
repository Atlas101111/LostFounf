from flask import current_app
from flask_login import current_user
from sqlalchemy import Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship

from app.models.base import Base


class FoundInfo(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category = Column(String(10), nullable=True, default='其他')  # not using now
    description = Column(String(256), nullable=True)
    location = Column(String(20), nullable=False)  # now it can only indicate the campus
    title = Column(String(30), nullable=False, default='未填写')
    contact = Column(String(10), nullable=False)  # the contact way user left
    contact_info = Column(String(20), nullable=False)
    cardID = Column(String(15), nullable=True, default='0')
    user = relationship('User', backref='found_info')
    uid = Column(Integer, ForeignKey('user.id'))  # foreign key

    @classmethod
    def recent(cls):  # pick up the latest 30 infos in the database
        recent_ = FoundInfo.query.fliter_by(status=True).group_by(
            FoundInfo.id
        ).order_by(desc(FoundInfo.create_time)).distinct().limit(
            current_app.config['RECENT_INFO_COUNT']).all()
        return recent_  # return a list of lost infos, each element is a LostInfo object

    def keys(self):  # for __dict__ to transform this class to a dict
        return ('description', 'location', 'contact', 'uid', 'contact',
                'contact_info', 'cardID')

    def upload(self, form):
        #self.uid = current_user.id
        #self.user = current_user
        self.description = form.description.data
        self.location = form.location.data
        self.title = form.title.data
        self.contact = form.contact.data
        self.contact_info = form.contact.data

    @classmethod
    def query_by_cardid(cls, cardID):
        result = FoundInfo.query.filter_by(cardID=cardID).all()
        return result

    @classmethod
    def query_by_keyword(cls, keyword):
        keyword = '%' + keyword + '%'
        result = FoundInfo.query.filter(FoundInfo.title.like(keyword)).all()
        return result

    @classmethod
    def my(cls):
        uid = current_user.id
        result = FoundInfo.query.filter_by(uid=uid).all()
        return result
