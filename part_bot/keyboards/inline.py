from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from part_database.db_for_book import show_link_detail_by_name_book


def show_detail_book(title_book, lang):
    markup = InlineKeyboardMarkup()
    link = show_link_detail_by_name_book(title_book)
    if lang == 'ru':
        markup.add(
            InlineKeyboardButton(text='Перейти к категории', callback_data='go_category'),
            InlineKeyboardButton(text='Перейти на страницу книги', callback_data='show_page', url=link)
        )
        return markup
    elif lang == 'en':
        markup.add(
            InlineKeyboardButton(text='Go to the category', callback_data='go_category'),
            InlineKeyboardButton(text='Go to the book page', callback_data='show_page', url=link)
        )
        return markup
