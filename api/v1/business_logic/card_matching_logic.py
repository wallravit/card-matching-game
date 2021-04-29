import random
from datetime import datetime
from typing import List

from api.config import CARD_GAME_COL, CARD_GAME_ROW
from api.exception import UnprocessableEntity
from api.models.game_model import GameModel
from api.schemas import game_schemas


class CardMatchingLogic:
    def __init__(self, logger) -> None:
        self._logger = logger.getChild(self.__class__.__name__)

    def generate_new_game(self):
        cards = []
        for i in range(CARD_GAME_ROW * CARD_GAME_COL):
            cards.append(0)
        return cards

    def generate_game_answer(self):
        cards = []
        for i in range(1, int((CARD_GAME_COL * CARD_GAME_ROW) / 2) + 1):
            cards.append(i)
            cards.append(i)
        random.shuffle(cards)
        return cards

    def update_game_board(
        self, current_session: GameModel, action: game_schemas.GameAction
    ):
        return None

    def is_game_finish(self, current_session: GameModel):
        return current_session.game_state == current_session.game_answer

    def get_position_index_1d(self, action: game_schemas.GameAction):
        if action.row > CARD_GAME_ROW or action.col > CARD_GAME_COL:
            raise UnprocessableEntity(
                f"card open position invalid. board size is {CARD_GAME_COL} x {CARD_GAME_ROW}."
            )
        return (action.col- 1) * CARD_GAME_ROW + (action.row - 1)

    def get_card_number(
        self, current_session: GameModel, action: game_schemas.GameAction
    ):
        return current_session.game_answer[self.get_position_index_1d(action)]

    def open_card(self, current_session: GameModel, action: game_schemas.GameAction):
        position_1d = self.get_position_index_1d(action)

        card_guess_open = current_session.game_state[position_1d]
        card_open_number = self.get_card_number(current_session, action)

        if card_guess_open == 0:
            open_card_count = [card for card in current_session.game_state if card < 0]
            if len(open_card_count) > 1:
                current_session.game_state = [
                    0 if card < 0 else card for card in current_session.game_state
                ]
            if card_open_number * -1 in current_session.game_state:
                self._logger.info(f"found maching card number {card_open_number}")
                current_session.game_state[position_1d] = card_open_number
                current_session.game_state = [
                    card_number * -1
                    if card_number == (card_open_number * -1)
                    else card_number
                    for card_number in current_session.game_state
                ]
            else:
                current_session.game_state[position_1d] = card_open_number * -1
            current_session.updated_datetime = datetime.now()
            current_session.click_count += 1
            current_session.game_finished = self.is_game_finish(current_session)
        return current_session
