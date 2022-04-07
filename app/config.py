import os

from dotenv import load_dotenv

load_dotenv()


class DevConfig:
    SECRET_KEY = os.getenv("DEV_SECRET_KEY")
    MYSQL_HOST = os.getenv("DEV_MYSQL_HOST")
    MYSQL_USER = os.getenv("DEV_MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("DEV_MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("DEV_MYSQL_DB")


class ProdConfig:
    def __init__(self):
        self.SECRET_KEY = os.getenv("PROD_SECRET_KEY")
        self.MYSQL_HOST = os.getenv("PROD_MYSQL_HOST")
        self.MYSQL_USER = os.getenv("PROD_MYSQL_USER")
        self.MYSQL_PASSWORD = os.getenv("PROD_MYSQL_PASSWORD")
        self.MYSQL_DB = os.getenv("PROD_MYSQL_DB")