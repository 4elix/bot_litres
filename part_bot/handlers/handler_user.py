from telebot.types import Message

from config import bot
from support import check_user_name
from part_database.db_for_user import add_user
from part_database.db_for_catalog import show_list_catalog
from part_bot.keyboards.default import home_menu


@bot.message_handler(func=lambda msg: msg.text == 'Зарегистрироваться 🖐' or msg.text == 'Register 🖐')
def react_register(message: Message):
    chat_id = message.chat.id
    txt = message.text
    if txt == 'Зарегистрироваться 🖐':
        lang = 'ru'
        text = 'Значит ты новый пользователь, а значит напиши как тебя зовут'
        bot.send_message(chat_id, text)
        bot.register_next_step_handler(message, get_name, lang)
    elif txt == 'Register 🖐':
        lang = 'en'
        text = 'So you are a new user, which means write your name'
        bot.send_message(chat_id, text)
        bot.register_next_step_handler(message, get_name, lang)


def get_name(message: Message, lang):
    chat_id = message.chat.id
    user_name = message.text
    status = check_user_name(user_name)
    if lang == 'ru':
        if status == 200:
            add_user(user_name, lang, chat_id)
            text = 'И так, регистрация прошла успешно'
            bot.send_message(chat_id, text, reply_markup=home_menu(chat_id, lang))
        else:
            text = 'И так, вы ввели не правильно имя'
            bot.send_message(chat_id, text, reply_markup=home_menu(chat_id, lang))
            return
    elif lang == 'en':
        if status == 200:
            add_user(user_name, lang, chat_id)
            text = 'And so, the registration was successful'
            bot.send_message(chat_id, text, reply_markup=home_menu(chat_id, lang))
        else:
            text = 'And so, you entered the wrong name'
            bot.send_message(chat_id, text, reply_markup=home_menu(chat_id, lang))
            return


