# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Используйте SQLite как базу данных
# Здесь база данных будет сохранена в файле `my_django_db.sqlite3` в корневой директории проекта
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./my_django_db.sqlite3")

# Создаем движок базы данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Параметр `check_same_thread` нужен для SQLite

# Создаем локальную сессию для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для создания моделей с использованием SQLAlchemy
Base = declarative_base()

