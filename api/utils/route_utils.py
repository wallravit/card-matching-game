from fastapi.responses import JSONResponse


def create_response(result=None, error=None, status_code=200) -> JSONResponse:
    body = {}
    if error:
        body = {"error": error}
    else:
        body = result
    return JSONResponse(content=body, status_code=status_code)