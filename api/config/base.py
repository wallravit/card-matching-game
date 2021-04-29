import os

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", 5432))
DATABASE_NAME = os.getenv("DATABASE_NAME", "cardGameDB")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "username")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}",
)

SECRET_KEY = os.getenv("SECRET_KEY", "KEEP-SECURE")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

CARD_GAME_ROW = int(os.getenv("CARD_GAME_ROW", 4))
CARD_GAME_COL = int(os.getenv("CARD_GAME_COL", 3))
