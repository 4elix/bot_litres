from telebot.types import Message

from config import bot
from part_bot.commands.default_set_cmd import react_start
from part_bot.handlers.handler_book import react_main_menu
from part_bot.keyboards.default import menu_lang, menu_settings, main_menu
from part_database.db_for_user import search_user_by_tg_id, delete_account, get_lang_by_tg_id, update_lang


@bot.message_handler(func=lambda msg: msg.text == '⚙ Настройки' or msg.text == '⚙ Settings')
def react_settings(message: Message):
    chat_id = message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        bot.send_message(chat_id, 'Выбирайте разделы', reply_markup=menu_settings(lang))
    elif lang == 'en':
        bot.send_message(chat_id, 'Choose sections', reply_markup=menu_settings(lang))


@bot.message_handler(func=lambda msg: msg.text == 'Удалить аккаунт' or msg.text == 'Поменять язык'
                                      or msg.text == 'Delete an account' or msg.text == 'Change the language')
def react_options(message: Message):
    chat_id = message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        if message.text == 'Удалить аккаунт':
            delete_account(chat_id)
            bot.send_message(chat_id, 'Аккаунт удален')
            react_start(message)
            return
        elif message.text == 'Поменять язык':
            bot.send_message(chat_id, 'Хорошо', reply_markup=menu_lang(lang))
    elif lang == 'en':
        if message.text == 'Delete an account':
            delete_account(chat_id)
            bot.send_message(chat_id, 'Account deleted')
            react_start(message)
            return
        elif message.text == 'Change the language':
            bot.send_message(chat_id, 'Good', reply_markup=menu_lang(lang))


@bot.message_handler(func=lambda msg: msg.text == 'ru' or msg.text == 'en'
                                      or msg.text == '🔙 Назад' or msg.text == '🔙 Back')
def change_lang(message: Message):
    chat_id = message.chat.id
    text = message.text
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        if text == 'ru':
            update_lang('ru', chat_id)
            bot.send_message(chat_id, 'Язык успешно изменен, на Русский')
            react_settings(message)
            return
        elif text == 'en':
            update_lang('en', chat_id)
            bot.send_message(chat_id, 'Язык успешно изменен, на Английский')
            react_settings(message)
            return
    elif lang == 'en':
        if text == 'ru':
            update_lang('ru', chat_id)
            bot.send_message(chat_id, 'The language has been successfully changed to Russian')
            react_settings(message)
            return
        elif text == 'en':
            update_lang('en', chat_id)
            bot.send_message(chat_id, 'The language has been successfully changed to English')
            react_settings(message)
            return
    elif lang == '🔙 Назад':
        react_settings(message)
        return
    elif lang == '🔙 Back':
        react_settings(message)
        return
