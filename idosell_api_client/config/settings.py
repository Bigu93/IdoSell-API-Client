import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_USERNAME = os.getenv("IDOSELL_CLIENT_USERNAME")
CLIENT_SECRET = os.getenv("IDOSELL_CLIENT_SECRET")
BASE_URL = os.getenv("IDOSELL_BASE_URL")
