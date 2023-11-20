import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_USERNAME = os.getenv("IDOSELL_CLIENT_USERNAME")
CLIENT_SECRET = os.getenv("IDOSELL_CLIENT_SECRET")
BASE_URL = os.getenv("IDOSELL_BASE_URL")

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()

STOCK_IDS = dict(item.split(":") for item in os.getenv("STOCK_IDS").split(","))
