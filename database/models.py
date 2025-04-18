from peewee import Model, BigIntegerField, CharField, ForeignKeyField, IntegerField
from peewee import SqliteDatabase

# Подключаем SQLite базу данных
db = SqliteDatabase('db.sqlite3')  # Используем SqliteDatabase вместо connect

# Базовая модель
class BaseModel(Model):
    class Meta:
        database = db  # Все модели будут использовать эту базу данных

# Модель пользователя
class User(BaseModel):
    tg_id = BigIntegerField(unique=True)  # Telegram ID, уникальное поле

# Модель категории
class Category(BaseModel):
    name = CharField(max_length=25)  # Название категории

# Модель товара
class Item(BaseModel):
    name = CharField(max_length=25)  # Название товара
    description = CharField(max_length=120)  # Описание товара
    price = IntegerField()  # Цена товара
    category = ForeignKeyField(Category, backref='items')  # Внешний ключ на категорию

# Функция для создания таблиц
def create_tables():
    with db:
        db.create_tables([User, Category, Item])  # Создаем таблицы для моделей
