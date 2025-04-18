from peewee import DoesNotExist
from database.models import User, Category, Item, db

# Функция для создания пользователя
def set_user(tg_id: int) -> None:
    with db.connection_context():
        # Используем get_or_create для предотвращения дублей
        User.get_or_create(tg_id=tg_id)

# Получаем все категории
def get_categories():
    with db.connection_context():
        return list(Category.select())  # Возвращаем список категорий

# Получаем товары по категории
def get_category_item(category_id):
    with db.connection_context():
        return list(Item.select().where(Item.category == category_id))  # Возвращаем список товаров

# Получаем товар по его id
def get_item(item_id):
    with db.connection_context():
        try:
            return Item.get(Item.id == item_id)  # Получаем один товар по id
        except DoesNotExist:
            return None  # Возвращаем None, если товар не найден
