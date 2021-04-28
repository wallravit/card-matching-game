from datetime import datetime
from typing import Optional

from api.models import UserModel
from api.schemas import user_schemas
from api.utils import acquire_logger
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self) -> None:
        self._logger = acquire_logger(self.__class__.__name__)

    def create(self, db: Session, user: user_schemas.UserCreate) -> Optional[UserModel]:
        try:
            self._logger.debug(f"create a new user for user {user.username}.")
            db_user = UserModel(
                username=user.username,
                hashed_password=user.password,
                created_datetime=datetime.now(),
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except:
            self._logger.exception("create user fail.")
            raise

    def get_user(self, db: Session, username: str) -> user_schemas.UserInDB:
        return db.query(UserModel).filter(UserModel.username == username).first()
