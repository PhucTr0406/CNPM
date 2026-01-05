from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import Config

# Sử dụng đúng tên biến đã khai báo trong config.py
DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URL, echo=True)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)