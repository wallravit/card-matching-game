from .base import *
from typing import Dict

DATABASE_ENGINE_ARGS = Dict
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))