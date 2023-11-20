import logging
import os
from config.settings import LOG_LEVEL

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join("logs", "api.log"),
    filemode="a",
)


def get_logger(name):
    return logging.getLogger(name)
