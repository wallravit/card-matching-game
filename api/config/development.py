import os

from .base import *

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
