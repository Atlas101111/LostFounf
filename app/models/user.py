from sqlalchemy import Column, Integer, String

from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)  # user's id
    nickname = Column(String(15), nullable=False)
    gender = Column(Integer, nullable=True, default=1)
    avatarUrl = Column(String(50))
