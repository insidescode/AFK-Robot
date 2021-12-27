"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""
import importlib
import time
import re
import sys
from termcolor import colored, cprint
from sys import argv
from typing import Optional
from HYPE_AFK_BOT import dispatcher, updater, LOGGER
from AWAY import ALL_MODULES
from MISCL import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, ChatMigrated, NetworkError, TelegramError, TimedOut, Unauthorized
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from MISCL.chat_status import *
AFKSAY = """Hey there.

I am a simple AFK Bot. I tell users that you are away if you are, so they don't need to be hanging for your reply.
"""
HYPE_AFK_BOT_IMG = "https://telegra.ph/file/72a6935b3af8962bd64f9.jpg"
IMPORTED = {}
HELPABLE = {}
GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("AWAY." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)


def start(update: Update, context: CallbackContext):
    if update.effective_chat.type == "private":
        update.effective_message.reply_photo(
            HYPE_AFK_BOT_IMG,
            AFKSAY,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="Add AFK Robot To Your Group",
                    url="t.me/{}?startgroup=true".format(context.bot.username),)], ]),)
    else:
        update.effective_message.reply_photo(
            HYPE_AFK_BOT_IMG,
            "Bot Should be Admin for some Features To Work Properly",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="Channel",
                    url="https://t.me/sluttyoreo")], ]),)


def main():
    start_handler = CommandHandler("start", start, run_async=True)
    dispatcher.add_handler(start_handler)


LOGGER.info("READY")
cprint(f"AFK Robot is Online", 'yellow')
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
main()
updater.idle()
cprint(f"AFK Robot   offline", 'white', 'on_red')
cprint(f"Join Channel", 'red')
cprint(f"@Sluttyoreo | @Aarzaai_Ishq", 'green')
updater.stop()
