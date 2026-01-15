import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("API_TOKEN")


# функция-обработчик команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот!")


# создаем приложение
app = ApplicationBuilder().token(TOKEN).build()

# добавляем обработчик команды
app.add_handler(CommandHandler("start", start))

# запускаем бота
app.run_polling()
