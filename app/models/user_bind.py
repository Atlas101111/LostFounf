from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base


class UserBind(Base):
    openid = Column(String(20), primary_key=True)  # user's id in the platform
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))

    @classmethod
    def in_table(cls, openid):  # if this openid has been bound yet
        result = UserBind.query.filter_by(openid=openid).first()
        return result
