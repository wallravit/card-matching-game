from api.utils import acquire_logger


class UserController:
    def __init__(self):
        self._logger = acquire_logger(self.__class__.__name__)