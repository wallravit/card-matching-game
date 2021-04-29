from datetime import datetime
from typing import List, Optional

from api.exception import NotFoundError
from api.models.game_model import GameModel
from api.models.user_model import UserModel
from api.repositories import GameRepository, UserRepository
from api.schemas import game_schemas
from api.utils import acquire_logger
from api.v1.business_logic import CardMatchingLogic
from sqlalchemy.orm import Session


class GamesController:
    def __init__(self) -> None:
        self._logger = acquire_logger("game-controller")
        self._game_logic = CardMatchingLogic(self._logger)
        self._game_repository = GameRepository(self._logger)

    async def get_best_click(self, db: Session) -> Optional[int]:
        return self._game_repository.get_best_click_count(db)

    async def get_games_session(
        self, db: Session, session_id: str, user: UserModel
    ) -> Optional[GameModel]:
        game_session = self._game_repository.get_by_session_id(db, session_id, user.id)
        if game_session:
            return game_session
        else:
            raise NotFoundError("game session not found.")

    async def get_user_best_click(self, db: Session, user: UserModel) -> Optional[int]:
        return self._game_repository.get_best_click_count(db, user.id)

    async def list_game_sessions(self, db: Session, user: UserModel) -> List[GameModel]:
        return self._game_repository.list_session_by_user_id(db, user.id)

    async def create_game_session(self, db: Session, user: UserModel) -> GameModel:
        new_game = GameModel(
            user_id=user.id,
            game_state=self._game_logic.generate_new_game(),
            game_answer=self._game_logic.generate_game_answer(),
            created_datetime=datetime.now(),
            updated_datetime=datetime.now(),
        )
        return self._game_repository.create(db, new_game)

    async def game_reset(self, db: Session, session_id: str, user: UserModel):
        try:
            current_session = await self.get_games_session(db, session_id, user)
            current_session.game_state = self._game_logic.generate_new_game()
            current_session.game_answer = self._game_logic.generate_game_answer()
            current_session.click_count = 0
            current_session.game_finished = False
            return self._game_repository.update_session(db, current_session)
        except:
            range

    async def game_update(
        self,
        db: Session,
        session_id: str,
        user: UserModel,
        game_action: game_schemas.GameAction,
    ) -> GameModel:
        try:
            current_session = await self.get_games_session(db, session_id, user)
            new_session = self._game_logic.open_card(current_session, game_action)
            return self._game_repository.update_session(db, new_session)
        except:
            raise
