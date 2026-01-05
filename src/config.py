import os
from dotenv import load_dotenv

# Load các biến từ file .env
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
    TESTING = os.environ.get('TESTING', 'False').lower() in ['true', '1']
    CORS_HEADERS = 'Content-Type'

    # --- PHẦN KẾT NỐI DATABASE CHỈNH SỬA ---
    # Ưu tiên lấy full URI từ .env, nếu không có thì tự ráp từ các biến lẻ
    DB_USER = os.getenv("DB_USER", "sa")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "Aa%40123456")
    DB_SERVER = os.getenv("DB_SERVER", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "1433")
    DB_NAME = os.getenv("DB_NAME", "RetinalHealthDB")

    # Đổi tên thành SQLALCHEMY_DATABASE_URI để session.py nhận được
    # Sử dụng mssql+pyodbc để ổn định hơn mssql+pymssql
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    f"mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    # ----------------------------------------

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

# --- GIỮ NGUYÊN PHẦN SWAGGER CỦA BẠN ---
class SwaggerConfig:
    """Swagger configuration."""
    template = {
        "swagger": "2.0",
        "info": {
            "title": "Medical AI API", # Đổi tên cho chuyên nghiệp
            "description": "API for Retinal Analysis and Medical Management",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": ["http", "https"],
        "consumes": ["application/json"],
        "produces": ["application/json"]
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs"
    }