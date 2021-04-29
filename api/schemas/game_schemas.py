from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class GameSchema(BaseModel):
    id: int
    user_id: int
    click_count: int
    game_state: List
    game_finished: bool


class GameInDBBase(GameSchema):
    updated_datetime: datetime
    created_datetime: datetime

    class Config:
        orm_mode = True


class Game(GameInDBBase):
    pass


class GameAction(BaseModel):
    row: int
    col: int
