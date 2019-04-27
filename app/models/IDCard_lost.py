from flask import current_app
from sqlalchemy import Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship

from app.models.base import Base


class IDCardLost(Base):   # Record about things that been missed
    id = Column(Integer, primary_key=True, autoincrement=True)  # id for this record
    nickname = Column(String(20), nullable=False)  # nickname of publisher
    cardID = Column(String(20), nullable=False, default='未知') # id in the card
    description = Column(String(256), nullable=True)
    location = Column(String(20), nullable=False)
    title = Column(String(30), nullable=False, default='未填写')
    contact = Column(String(20), nullable=False)  # the contact way user left
    user = relationship('User')  # Who lost this
    uid = Column(Integer, ForeignKey('user.id'))     # foreign key in user

    @classmethod
    def recent(cls):
        recent_ = IDCardLost.query.fliter_by(status=True).group_by(
            IDCardLost.id
        ).order_by(desc(IDCardLost.create_time)).distinct().limit(
            current_app.config['RECENT_INFO_COUNT']).all()
        return recent_

    @classmethod
    def get_by_id(cls, cardID): # Find the record only by id in the card
        result = IDCardLost.query.fliter_by(status=True, cardID=cardID).first()
        return result


