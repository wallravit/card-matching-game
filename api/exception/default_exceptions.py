from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self, detail=None):
        super().__init__(404, detail)
