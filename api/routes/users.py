from importlib import import_module
from typing import Dict

from api.utils.route_utils import create_response
from fastapi import APIRouter, Depends, Response

router = APIRouter()


@router.get("/{version}/users", tags=["users"])
async def user_doc(version: str) -> Response:
    controller = import_module(f"api.{version}.controllers")
    resp = {
        "status": "success"
    }
    return create_response(result=resp, status_code=200)
