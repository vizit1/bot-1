import os

from telegram import Bot
from telegram.ext import CommandHandler, Updater

TOKEN = os.environ.get("API_TOKEN")


def start(update, context):
    update.message.reply_text("Привет! Я бот!")


updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
