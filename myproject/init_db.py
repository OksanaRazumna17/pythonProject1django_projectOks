import sys
import os

# Добавляем корневую папку проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from myproject.database import engine, Base
    from myproject.models import User  # Убедитесь, что вы импортируете модели правильно
except ModuleNotFoundError as e:
    print(f"Ошибка: {e}. Проверьте, что модули импортируются правильно.")
    sys.exit(1)

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("База данных успешно инициализирована.")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")

if __name__ == "__main__":
    print("Инициализация базы данных...")
    init_db()

