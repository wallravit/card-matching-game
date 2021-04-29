from api.database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_datetime = Column(TIMESTAMP, nullable=False)
