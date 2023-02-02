from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
   file = open('PYTHON\Seminar_10\db.csv', 'a', encoding = 'utf-8')
   file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text} {datetime.datetime.now()}\n')
   file.close()