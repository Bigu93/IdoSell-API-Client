import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join("logs", "api.log"),
    filemode="a",
)


def get_logger(name):
    return logging.getLogger(name)
