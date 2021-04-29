from logging import Logger
from typing import Optional

from api.models import UserModel
from api.schemas import user_schemas
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, logger: Logger) -> None:
        self._logger = self._logger = logger.getChild(self.__class__.__name__)

    def create(self, db: Session, user: UserModel) -> Optional[UserModel]:
        try:
            self._logger.debug(f"create a new user for user {user.username}.")
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except:
            self._logger.exception("create user fail.")
            raise

    def get_user(self, db: Session, username: str) -> user_schemas.UserInDB:
        return db.query(UserModel).filter(UserModel.username == username).first()
