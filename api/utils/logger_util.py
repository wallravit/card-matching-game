import logging


def _acquire_console_handler() -> logging.Handler:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(processName)s %(threadName)s [%(levelname)s] "
        "%(name)s[%(lineno)d]: %(message)s"
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    return handler


def acquire_logger(app_name: str) -> logging.Logger:
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)

    handler = _acquire_console_handler()

    logger.handlers = []
    logger.addHandler(handler)
    return logger
