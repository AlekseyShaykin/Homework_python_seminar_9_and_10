from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! Я бот, который поможет тебе определить возможный цвет глаз ребенка на основании цвета глаз его родителей. Если готовы продолжать, нажмите /menu')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('/hi\n /choice\n ')

async def choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Вам необходимо выбрать интересующий цвет глаз одного из родителей: карий (/black) , голубой (/blue), зеленый(/green).')

#  Введите сочетание цветов, используя команду: hr. Например, /hr голубой зеленый    

async def black(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Вот вероятности цвета глаз для ребенка: ')
    await update.message.reply_photo('PYTHON\Seminar_10\images\КАРИЙ.jpg')
    time.sleep(3)
    await update.message.reply_text('Также Вы можете воспользоваться ручным подбором: для этого введите сочетание цветов, используя команду: hr. Например, /hr голубой зеленый  ')

async def blue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Вот вероятности цвета глаз для ребенка: ')
    await update.message.reply_photo('PYTHON\Seminar_10\images\ГОЛУБОЙ.jpg')
    time.sleep(3)
    await update.message.reply_text('Также Вы можете воспользоваться ручным подбором: для этого введите сочетание цветов, используя команду: hr. Например, /hr голубой зеленый  ')

async def green(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Вот вероятности цвета глаз для ребенка: ')
    await update.message.reply_photo('PYTHON\Seminar_10\images\ЗЕЛЕНЫЙ.jpg')
    time.sleep(3)
    await update.message.reply_text('Также Вы можете воспользоваться ручным подбором: для этого введите сочетание цветов, используя команду: hr. Например, /hr голубой зеленый  ')

    
async def heritage(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    # await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split(' ') # /sum  1212 2332332  /heritage голубой зеленый
    if items[1] == 'карий' and items[2] == 'карий':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\карий карий.jpg')
    elif items[1] == 'карий' and items[2] == 'голубой':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\карий голубой.jpg')
    elif items[2] == 'карий' and items[1] == 'голубой':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\карий голубой.jpg')
    elif items[1] == 'карий' and items[2] == 'зеленый':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\карий зеленый.jpg')
    elif items[2] == 'карий' and items[1] == 'зеленый':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\карий зеленый.jpg') 
    elif items[1] == 'голубой' and items[2] == 'голубой':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\голубой голубой.jpg')
    elif items[1] == 'голубой' and items[2] == 'зеленый':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\голубой зеленый.jpg')
    elif items[2] == 'голубой' and items[1] == 'зеленый':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\голубой зеленый.jpg') 
    elif items[1] == 'зеленый' and items[2] == 'зеленый':
        await update.message.reply_text(f'{items[1]} цвет глаз у папы + {items[2]} цвет глаз у мамы приведет к следующей вероятности у их ребенка:')
        await update.message.reply_photo('PYTHON\Seminar_10\images\зеленый зеленый.jpg')
   

       
