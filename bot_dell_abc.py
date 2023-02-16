from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from random import randint

token1 = ""
bot = Bot(token="")
updater = Updater(token=token1)
dispatcher = updater.dispatcher

def start(update:Updater, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id,
    "Hello Amigo\nЗапиши слова через пробел и отправь сообщение\nЯ удалю все слова содржащие 'абв'")

def abc_extractor(update:Updater, context: CallbackContext):
    text = update.message.text
    if len(text) < 3:
        context.bot.send_message(update.effective_chat.id,  "Нет слов, мой дорогой друг")
    else:
        context.bot.send_message(update.effective_chat.id, f"Готово:  {abc_off(text)}")

def abc_off(text):
    text, out_text = text.lower().split(), ''    
    for x in text:  
        if "абв" not in str(x): out_text += str(x) + ' '
    return out_text

start_handler = CommandHandler('start', start)
abc_extractor_handler = MessageHandler(Filters.text, abc_extractor)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(abc_extractor_handler)

updater.start_polling()
updater.idle()
