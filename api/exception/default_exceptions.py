from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self, detail=None):
        super().__init__(404, detail)


class UnauthorizedError(HTTPException):
    def __init__(self, detail=None):
        super().__init__(401, detail)


class UnprocessableEntity(HTTPException):
    def __init__(self, detail=None):
        super().__init__(422, detail)
