from typing import Dict, List, Optional

from api.database import SessionLocal
from api.exception import NotFoundError
from api.schemas import game_schemas
from api.utils import acquire_logger
from api.utils.route_util import create_response, get_controller
from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from api.models.game_model import GameModel

logger = acquire_logger("game-router")
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{version}/games/global/best_click", tags=["game"])
async def get_global_best_click(
    version: str, db: Session = Depends(get_db)
) -> List[game_schemas.Game]:
    try:
        games_controller = get_controller("GamesController", version)
        result = await games_controller.get_best_click(db)
        payload = {"best_click_count": result}
        return create_response(result=payload)
    except:
        raise


@router.get("/{version}/games/best_click", tags=["game"])
async def get_user_best_click(
    version: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> Response:
    try:
        users_controller = get_controller("UsersController", version)
        games_controller = get_controller("GamesController", version)
        user = await users_controller.get_current_user(db, token)
        result = await games_controller.get_user_best_click(db, user)
        payload = {"best_click_count": result}
        return create_response(result=payload)
    except:
        raise


@router.get("/{version}/games", response_model=List[game_schemas.Game], tags=["game"])
async def list_games_session(
    version: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> List[game_schemas.Game]:
    try:
        users_controller = get_controller("UsersController", version)
        games_controller = get_controller("GamesController", version)
        user = await users_controller.get_current_user(db, token)
        result = await games_controller.list_game_sessions(db, user)
        return result
    except:
        raise


@router.get(
    "/{version}/games/{session_id}",
    response_model=game_schemas.Game,
    tags=["game"],
)
async def get_games_session(
    version: str,
    session_id: str,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Response:
    try:
        users_controller = get_controller("UsersController", version)
        games_controller = get_controller("GamesController", version)
        user = await users_controller.get_current_user(db, token)
        result = await games_controller.get_games_session(db, session_id, user)
        return result
    except:
        raise


@router.post("/{version}/games", response_model=game_schemas.Game, tags=["game"])
async def create_game_session(
    version: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> Response:
    try:
        users_controller = get_controller("UsersController", version)
        games_controller = get_controller("GamesController", version)
        user = await users_controller.get_current_user(db, token)
        result = await games_controller.create_game_session(db, user)
        return result
    except:
        raise


@router.post(
    "/{version}/games/{session_id}", response_model=game_schemas.Game, tags=["game"]
)
async def update_game_session(
    version: str,
    session_id: str,
    game_action: game_schemas.GameAction,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Response:
    try:
        users_controller = get_controller("UsersController", version)
        games_controller = get_controller("GamesController", version)
        user = await users_controller.get_current_user(db, token)
        result = await games_controller.game_update(db, session_id, user, game_action)
        return result
    except:
        raise


@router.post(
    "/{version}/games/{session_id}/reset",
    response_model=game_schemas.Game,
    tags=["game"],
)
async def update_game_session(
    version: str,
    session_id: str,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Response:
    try:
        users_controller = get_controller("UsersController", version)
        games_controller = get_controller("GamesController", version)
        user = await users_controller.get_current_user(db, token)
        result = await games_controller.game_reset(db, session_id, user)
        return result
    except:
        raise
