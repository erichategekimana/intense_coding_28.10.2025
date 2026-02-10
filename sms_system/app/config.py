from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET = os.environ.get("JWT_SECRET")
    SQLALCHEMY_DATABASE = os.environ.get("SQLALCHEMY_DATABASE_URI")
