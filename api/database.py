from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.config import DATABASE_ENGINE_ARGS, DATABASE_URL
from api.utils import acquire_logger

logger = acquire_logger("database")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db() -> None:
    from api.models import GameModel, UserModel

    try:
        logger.info("start create app tables.")
        Base.metadata.create_all(bind=engine)
        logger.info("create app tables done.")
    except:
        logger.exception("create app table fail.")
