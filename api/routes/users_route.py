from importlib import import_module
from typing import Dict, List, Optional

from api.database import SessionLocal
from api.exception import NotFoundError
from api.schemas import user_schemas
from api.utils import acquire_logger
from api.utils.route_util import create_response, get_controller
from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


logger = acquire_logger("users-router")
router = APIRouter()


@router.get("/{version}/users", response_model=user_schemas.User, tags=["users"])
async def get_user_info(
    version: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> Response:
    try:
        controller = get_controller("UsersController", version)
        result = await controller.get_current_user(db, token)
        logger.info(f"{result}")
        return result
    except:
        raise


@router.post("/{version}/users", response_model=user_schemas.User, tags=["user"])
async def create_user(
    version: str, request: Request, db: Session = Depends(get_db)
) -> Response:
    try:
        controller = get_controller("UsersController", version)
        result = await controller.create_user(db, request)
        return result
    except:
        raise


@router.post(
    "/{version}/users/token", response_model=user_schemas.TokenSchema, tags=["user"]
)
async def generate_token(
    version: str, request: Request, db: Session = Depends(get_db)
) -> Response:
    try:
        controller = get_controller("UsersController", version)
        result = await controller.generate_token(db, request)
        return result
    except:
        raise
