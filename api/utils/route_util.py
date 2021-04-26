from importlib import import_module

from api.exception import NotFoundError
from api.utils import acquire_logger
from fastapi.responses import JSONResponse

logger = acquire_logger("route-utils")


def create_response(result=None, error=None, status_code=200) -> JSONResponse:
    body = {}
    if error:
        body = {"error": error}
    else:
        body = result
    return JSONResponse(content=body, status_code=status_code)


def get_attr(controller, name):
    try:
        return getattr(controller, name)
    except Exception:
        logger.exception("get attr error.")
        raise NotFoundError()


def get_controllers_version(version):
    folder_version = get_folder_version(version)
    try:
        return import_module("api.{}.controllers".format(folder_version))
    except Exception as ex:
        print(ex)
        raise NotFoundError(f"version {version} not support")


def get_folder_version(version):
    return version.replace(".", "_")


def get_controller(name, version, **kwargs):
    controllers = get_controllers_version(version)
    Controller = get_attr(controllers, name)
    return Controller(**kwargs)
