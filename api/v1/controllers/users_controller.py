from api.utils import acquire_logger


class UsersController:
    def __init__(self):
        self._logger = acquire_logger(self.__class__.__name__)
    
    def get_user_info(self):
        self._logger.info("get user info.")
        return None