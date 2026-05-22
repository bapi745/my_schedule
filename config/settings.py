import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    # ─── Secret Keys ──────────────────────────────────────────────
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-change-in-production")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # ─── MySQL via SQLAlchemy ──────────────────────────────────────
    # Format: mysql+pymysql://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:your_password@localhost:3306/task_manager_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # Set True to log SQL queries (dev only)