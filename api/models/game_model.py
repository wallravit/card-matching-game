from datetime import datetime

from api.database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSON


class GameModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    game_state = Column(JSON)
    game_finished = Column(Boolean, default=False)
    updated_datetime = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    created_datetime = Column(TIMESTAMP, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
