from .base import *

DATABASE_ENGINE_ARGS = {"check_same_thread": False}
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 120))
