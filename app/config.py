import os
from dotenv import load_dotenv

load_dotenv()


class DevConfig:
    SECRET_KEY = os.getenv("DEV_SECRET_KEY")


class ProdConfig:
    SECRET_KEY = os.getenv("PROD_SECRET_KEY")