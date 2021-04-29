from logging import Logger
from typing import Optional

from api.models import GameModel
from api.schemas import game_schemas
from api.utils import acquire_logger
from sqlalchemy import func
from sqlalchemy.orm import Session


class GameRepository:
    def __init__(self, logger: Logger) -> None:
        self._logger = logger.getChild(self.__class__.__name__)

    def get_best_click_count(self, db: Session, user_id: int = None) -> Optional[int]:
        best_game_session = None
        if user_id:
            best_game_session = (
                db.query(func.max(GameModel.click_count))
                .filter(GameModel.game_finished == True)
                .filter(GameModel.user_id == user_id)
                .first()
            )
        else:
            best_game_session = (
                db.query(func.max(GameModel.click_count))
                .filter(GameModel.game_finished == True)
                .first()
            )
        best_game_click_count = best_game_session[0]
        if not best_game_click_count:
            return None
        return best_game_click_count

    def get_by_session_id(self, db: Session, session_id, user_id) -> GameModel:
        return (
            db.query(GameModel)
            .filter(GameModel.user_id == user_id)
            .filter(GameModel.id == session_id)
            .first()
        )

    def list_session_by_user_id(self, db: Session, user_id: int):
        return db.query(GameModel).filter(GameModel.user_id == user_id).all()

    def create(self, db: Session, game: GameModel) -> Optional[GameModel]:
        try:
            self._logger.info(f"create game for user id {game.user_id}.")
            db.add(game)
            db.commit()
            db.refresh(game)
            return game
        except:
            self._logger.exception("game create fail.")

    def update_session(self, db: Session, game: GameModel):
        self._logger.info(
            f"update game session for user id {game.user_id}, session id {game.id}"
        )
        current_session = (
            db.query(GameModel)
            .filter(GameModel.id == game.id)
            .filter(GameModel.user_id == game.user_id)
            .update(
                {
                    "game_state": game.game_state,
                    "click_count": game.click_count,
                    "game_finished": game.game_finished,
                },
                synchronize_session=False,
            )
        )
        db.commit()
        return self.get_by_session_id(db, game.id, game.user_id)
