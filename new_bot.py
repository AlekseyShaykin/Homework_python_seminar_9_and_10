from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *





app = ApplicationBuilder().token("5802615262:AAH8977C9gP5bgL6opuWfE6GPT47YNgnMTY").build()
print('Server has started')


app.add_handler(CommandHandler("Hi", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("black", black))
app.add_handler(CommandHandler("green", green))
app.add_handler(CommandHandler("blue", blue))
app.add_handler(CommandHandler("hr", heritage))

app.run_polling()

