import logging
from app.core.config import settings


def _build_logger() -> logging.Logger:
    logger = logging.getLogger(settings.APP_NAME)
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


logger = _build_logger()
