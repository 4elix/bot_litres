from telebot.types import Message

from config import bot
from part_bot.keyboards.default import home_menu, choice_language
from part_database.db_for_user import search_user_by_tg_id, update_lang, get_lang_by_tg_id


@bot.message_handler(commands=['start'])
def react_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте, дорогой читатель / Hello, dear reader', reply_markup=choice_language())
    bot.register_next_step_handler(message, react_choice_language)


def react_choice_language(message: Message):
    chat_id = message.chat.id
    lang = message.text
    user = search_user_by_tg_id(chat_id)

    if lang == 'Русский':
        lan = 'ru'
        if user is not None:
            status_lang = get_lang_by_tg_id(chat_id)
            if status_lang == lan:
                bot.send_message(chat_id, 'Хорошо', reply_markup=home_menu(chat_id, lan))
            else:
                update_lang(lan, chat_id)
                bot.send_message(chat_id, 'Хорошо', reply_markup=home_menu(chat_id, lan))
        else:
            bot.send_message(chat_id, 'Хорошо', reply_markup=home_menu(chat_id, lan))

    elif lang == 'English':
        lan = 'en'
        if user is not None:
            statis_lang = get_lang_by_tg_id(chat_id)
            if statis_lang == lan:
                bot.send_message(chat_id, 'Good', reply_markup=home_menu(chat_id, lan))
            else:
                update_lang(lan, chat_id)
                bot.send_message(chat_id, 'Good', reply_markup=home_menu(chat_id, lan))
        else:
            bot.send_message(chat_id, 'Good', reply_markup=home_menu(chat_id, lan))
