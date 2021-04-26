from importlib import import_module
from typing import Dict
from api.exception import NotFoundError
from api.utils.route_util import create_response, get_controller
from fastapi import APIRouter, Depends, Response

router = APIRouter()


@router.get("/{version}/users", tags=["users"])
async def get_user_info(version: str) -> Response:
    controller = get_controller("UsersController", version)
    resp = {"status": "success"}
    return create_response(result=resp, status_code=200)


@router.post("/{version}/users/", tags=["user"])
async def create_user(version: str) -> Response:
    controller = get_controller("UsersController", version)
    resp = {"status": "success"}
    return create_response(result=resp, status_code=200)