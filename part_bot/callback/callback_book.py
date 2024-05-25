from telebot.types import Message, CallbackQuery

from config import bot
from part_bot.keyboards.inline import show_detail_book
from part_bot.keyboards.default import category_menu
from part_database.db_for_user import get_lang_by_tg_id


@bot.callback_query_handler(func=lambda call: call.data == 'go_category')
def show_category(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        bot.send_message(chat_id, 'Хорошо', reply_markup=category_menu(lang))
    elif lang == 'en':
        bot.send_message(chat_id, 'Good', reply_markup=category_menu(lang))


@bot.callback_query_handler(func=lambda call: call.data == 'show_page')
def show_category(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    lang = get_lang_by_tg_id(chat_id)
    if lang == 'ru':
        bot.send_message(chat_id, 'Хорошо', reply_markup=category_menu(lang))
    elif lang == 'en':
        bot.send_message(chat_id, 'Good', reply_markup=category_menu(lang))

