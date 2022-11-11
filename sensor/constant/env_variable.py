import os
from dotenv import load_dotenv

ENV_PATH = os.path.join(os.getcwd(), "sensor", "config", ".env")
load_dotenv(ENV_PATH)

MONGODB_URL_KEY = os.getenv("MONGO_DB_URL", None)
AWS_ACCESS_KEY_ID_ENV_KEY = os.getenv("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY_ENV_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", None)
REGION_NAME = "ap-south-1"
