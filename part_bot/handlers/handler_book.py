from telebot.types import Message, ReplyKeyboardRemove

from config import bot
from part_database.db_for_user import get_lang_by_tg_id
from part_database.db_for_catalog import show_list_catalog, get_id_by_name
from part_database.db_for_book import show_list_book_by_cat_id, show_book_info
from part_bot.keyboards.default import main_menu, category_menu, name_book_menu
from part_bot.keyboards.inline import show_detail_book


@bot.message_handler(func=lambda msg: msg.text == 'Главное меню' or msg.text == 'Main Menu')
def react_main_menu(message: Message):
    chat_id = message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        bot.send_message(chat_id, 'Хорошо, готовы начать просмотре ?', reply_markup=main_menu(lang))
    elif lang == 'en':
        bot.send_message(chat_id, 'Okay, are you ready to start watching?', reply_markup=main_menu(lang))


@bot.message_handler(func=lambda msg: msg.text == '📕 Посмотреть категории' or msg.text == '📕 View categories')
def react_show_categories(message: Message):
    chat_id = message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        bot.send_message(chat_id, 'Вот наши категорию', reply_markup=category_menu(lang))
    elif lang == 'en':
        bot.send_message(chat_id, 'Here are our categories', reply_markup=category_menu(lang))


@bot.message_handler(func=lambda msg: msg.text == '🔙 Назад' or msg.text == '🔙 Back' or msg.text in show_list_catalog())
def show_book(message: Message):
    chat_id = message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        if message.text == '🔙 Назад':
            react_main_menu(message)
            return

        elif message.text in show_list_catalog():
            cat_id = get_id_by_name(message.text)
            bot.send_message(chat_id, 'Выбирай что хочешь', reply_markup=name_book_menu(cat_id, lang))
            bot.register_next_step_handler(message, get_test, lang, cat_id)
        else:
            bot.send_message(chat_id, 'Что-то пошло не так, попробуйте заново', reply_markup=category_menu(lang))
    if lang == 'en':
        if message.text == '🔙 Back':
            react_main_menu(message)
            return

        elif message.text in show_list_catalog():
            cat_id = get_id_by_name(message.text)
            bot.send_message(chat_id, 'Choose what you want', reply_markup=name_book_menu(cat_id, lang))
            bot.register_next_step_handler(message, get_test, lang, cat_id)
        else:
            bot.send_message(chat_id, 'Something went wrong, try again', reply_markup=category_menu(lang))


def get_test(message: Message, lang, cat_id):
    chat_id = message.chat.id
    if lang == 'ru':
        if message.text == '🔙 Назад к категориям':
            react_show_categories(message)
            return

        name = message.text
        list_book_name = show_list_book_by_cat_id(cat_id)

        if name in list_book_name:
            title, img_link, author, price, estimation, estimation_quantity, type_book = show_book_info(name)
            text = f"""
Название: {title}
Автор: {author} 🧙‍♂️
Цена: {price} ₽
Оценка книги: {estimation} ⭐
Количество оценок: {estimation_quantity}
Тип книги: {type_book} 
"""
            bot.send_photo(chat_id, photo=img_link, caption=text, reply_markup=show_detail_book(title, lang))
        else:
            bot.send_message(chat_id, 'Произошла ошибка', reply_markup=category_menu(lang))
    elif lang == 'en':
        if message.text == '🔙 Back to Categories':
            react_show_categories(message)
            return

        name = message.text
        list_book_name = show_list_book_by_cat_id(cat_id)

        if name in list_book_name:
            title, img_link, author, price, estimation, estimation_quantity, type_book = show_book_info(name)
            text = f"""
Title: {title}
Author: {author} 🧙‍♂️
Price: {price} ₽
Book Evaluation: {estimation} ⭐
Number of ratings: {estimation_quantity}
Type of book: {type_book} 
        """
            bot.send_photo(chat_id, photo=img_link, caption=text, reply_markup=show_detail_book(title, lang))
        else:
            bot.send_message(chat_id, 'An error has occurred', reply_markup=category_menu(lang))
