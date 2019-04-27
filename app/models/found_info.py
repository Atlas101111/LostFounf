from flask import current_app
from sqlalchemy import Column, Integer, String, ForeignKey, desc
from sqlalchemy.orm import relationship

from app.models.base import Base


class FoundInfo(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nickname = Column(String(20), nullable=False)  # nickname of publisher
    category = Column(String(20), nullable=False, default='其他')
    description = Column(String(256), nullable=True)
    location = Column(String(20), nullable=False)  # now it can only indicate the campus
    title = Column(String(30), nullable=False, default='未填写')
    contact = Column(String(20), nullable=False)  # the contact way user left
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))  # foreign key

    @classmethod
    def recent(cls, category):  # pick up the latest 30 infos in the database
        recent_ = FoundInfo.query.fliter_by(status=True, category=category).group_by(
            FoundInfo.id
        ).order_by(desc(FoundInfo.create_time)).distinct().limit(
            current_app.config['RECENT_INFO_COUNT']).all()
        return recent_  # return a list of lost infos, each element is a LostInfo object

    @classmethod
    def to_dict(cls, recent):   # turn the recent result set to list
        result = []
        for info in recent:
            temp = {
                'id': info.id,
                'nickname': info.nickname,
                'category': info.category,
                'description': info.description,
                'location': info.location,
                'uid': info.uid
            }
            result.append(temp)
        return result
        pass



