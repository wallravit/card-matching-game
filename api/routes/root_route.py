from typing import Dict, List, Optional

from api.config import APP_VERSION
from api.database import SessionLocal
from api.utils import acquire_logger
from api.utils.route_util import create_response
from fastapi import APIRouter, Request, Response

logger = acquire_logger("root-router")
router = APIRouter()


@router.get("/", tags=["root"])
async def index() -> Response:
    return create_response(
        result={"message": "Cards Matching Game.", "version": APP_VERSION}
    )
