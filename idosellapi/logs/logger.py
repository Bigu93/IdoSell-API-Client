import logging
import os
from idosellapi.config.settings import LOG_LEVEL

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join("idosellapi/logs", "api.log"),
    filemode="a",
)


def get_logger(name):
    return logging.getLogger(name)
