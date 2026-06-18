import os
from dotenv import load_dotenv
from datetime import timedelta

JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=5)

load_dotenv()


class Config:

    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")

    UPLOAD_FOLDER = "uploads"

    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("SECRET_KEY")

    STORAGE_TYPE = os.getenv(
        "STORAGE_TYPE",
        "local"
    )