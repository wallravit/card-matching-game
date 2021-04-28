from datetime import datetime, timedelta
from typing import Dict, Optional

from api.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from api.exception import UnauthorizedError
from api.repositories import UserRepository
from api.schemas import user_schemas
from api.utils import acquire_logger
from fastapi import Depends, Request
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class UsersController:
    def __init__(self) -> None:
        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self._user_repository = UserRepository()
        self._logger = acquire_logger(self.__class__.__name__)

    async def get_user_info(self) -> None:
        self._logger.info("get user info.")
        return None

    async def create_user(self, db: Session, request: Request) -> Dict:
        try:
            payload = await request.json()
            result = self._user_repository.create(
                db,
                user_schemas.UserCreate(
                    username=payload["username"],
                    password=self._hash_password(payload["password"]),
                ),
            )
            return result
        except:
            self._logger.exception("create user fail.")
            raise

    async def generate_token(self, db: Session, request: Request):
        payload = await request.json()
        user = self._authenticate_user(db, payload["username"], payload["password"])
        if not user:
            raise UnauthorizedError("username or password is incorrect.")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self._create_access_token(
            data={"username": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    async def get_current_user(self, db: Session, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("username")
            if username is None:
                raise UnauthorizedError("Could not validate credentials")
            token_data = user_schemas.TokenData(username=username)
        except JWTError:
            raise UnauthorizedError("Could not validate credentials")
        user = self._user_repository.get_user(db, username)
        if user is None:
            raise UnauthorizedError("Could not validate credentials")
        return user

    def _authenticate_user(self, db: Session, username: str, password: str):
        user = self._user_repository.get_user(db, username)
        if not user:
            return False
        if not self._verify_password(password, user.hashed_password):
            return False
        return user

    def _create_access_token(
        self, data: Dict, expires_delta: Optional[timedelta] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def _hash_password(self, password):
        return self._pwd_context.hash(password)

    def _verify_password(self, plain_password, hashed_password):
        return self._pwd_context.verify(plain_password, hashed_password)
