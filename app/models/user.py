from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import login_manager
from app.models.base import Base


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)  # user's id
    nickname = Column(String(15), nullable=False)
    gender = Column(Integer, nullable=True, default=1)
    college = Column(String(20), nullable=True)
    grade = Column(String(10), nullable=True)
    majority = Column(String(20), nullable=True)
    avatarUrl = Column(String(256))
    bind = relationship('UserBind')


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
