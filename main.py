from config import bot

from part_bot.commands.default_set_cmd import *
from part_bot.handlers.handler_user import *
from part_bot.handlers.handler_book import *
from part_bot.handlers.handler_settings import *
from part_bot.callback.callback_book import *


if __name__ == '__main__':
    print('start bot ')
    bot.infinity_polling()
