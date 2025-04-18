

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.request import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]
], 
                           resize_keyboard=True, input_field_placeholder="Выберите пункт меню...")

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Салаты', callback_data='Salads')],
    [InlineKeyboardButton(text='Фаст-фуды', callback_data='Fast Foods')],
    [InlineKeyboardButton(text='Напитки', callback_data='Drinks')]
])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Oтправить номер", request_contact=True)]],
                                 resize_keyboard=True)


# Синхронная версия функции для получения категорий
def categories():
    all_categories = get_categories()  # Убираем await, теперь get_categories синхронная
    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


# Синхронная версия функции для получения товаров
def items(category_id):
    all_items = get_category_item(category_id)  # Убираем await, теперь get_category_item синхронная
    keyboard = InlineKeyboardBuilder()

    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
