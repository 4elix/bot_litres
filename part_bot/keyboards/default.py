from telebot.types import ReplyKeyboardMarkup, KeyboardButton


from part_database.db_for_user import search_user_by_tg_id
from part_database.db_for_catalog import show_list_catalog
from part_database.db_for_book import show_list_book_by_cat_id


def choice_language():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='Русский'),
        KeyboardButton(text='English')
    )
    return markup


def home_menu(tg_id, lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    user = search_user_by_tg_id(tg_id)

    if lang == 'ru':
        if user is None:
            markup.add(
                KeyboardButton(text='Зарегистрироваться 🖐')
            )
        else:
            markup.add(
                KeyboardButton(text='Главное меню')
            )
        return markup
    elif lang == 'en':
        if user is None:
            markup.add(
                KeyboardButton(text='Register 🖐')
            )
        else:
            markup.add(
                KeyboardButton(text='Main Menu')
            )
        return markup


def main_menu(lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if lang == 'ru':
        markup.add(
            KeyboardButton(text='⚙ Настройки'),
            KeyboardButton(text='📕 Посмотреть категории')
        )
        return markup
    elif lang == 'en':
        markup.add(
            KeyboardButton(text='⚙ Settings'),
            KeyboardButton(text='📕 View categories')
        )
        return markup


def category_menu(lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if lang == 'ru':
        markup.row(KeyboardButton(text='🔙 Назад'))
    elif lang == 'en':
        markup.row(KeyboardButton(text='🔙 Back'))

    category = show_list_catalog()
    button = [KeyboardButton(text=cat) for cat in category]
    markup.add(*button)
    return markup


def name_book_menu(cat_id, lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if lang == 'ru':
        markup.row(KeyboardButton(text='🔙 Назад к категориям'))
    elif lang == 'en':
        markup.row(KeyboardButton(text='🔙 Back to Categories'))

    list_name_book = show_list_book_by_cat_id(cat_id)
    button = [KeyboardButton(text=name) for name in list_name_book]
    markup.add(*button)
    return markup


def menu_settings(lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if lang == 'ru':
        markup.add(
            KeyboardButton(text='🔙 Назад'),
            KeyboardButton(text='Удалить аккаунт'),
            KeyboardButton(text='Поменять язык')
        )
        return markup
    elif lang == 'en':
        markup.add(
            KeyboardButton(text='🔙 Back'),
            KeyboardButton(text='Delete an account'),
            KeyboardButton(text='Change the language')
        )
        return markup


def menu_lang(lang):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(text='ru'),
        KeyboardButton(text='en')
    )

    if lang == 'ru':
        markup.row(KeyboardButton(text='🔙 Назад'))
        return markup

    elif lang == 'en':
        markup.row(KeyboardButton(text='🔙 Back'))
        return markup
