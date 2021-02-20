import telebot
import requests
import json
import re
from telebot.types import ReplyKeyboardMarkup,KeyboardButton
TOKEN = '1656459425:AAEymoNrG9_OP5yJh1vkXRJur4gkJoWh9-I'
bot = telebot.TeleBot(TOKEN)

def Button(message):
    r = requests.get('https://khayyam2601.herokuapp.com/api/button')
    data = json.loads(r.text)
    key = ReplyKeyboardMarkup(True,False)
    text = "سلام {} شماره دانشجویی تو وارد کن :)".format(message.from_user.first_name)
    bot.send_message(message.from_user.id,text,reply_markup=key)

@bot.message_handler(commands=['start'])
def start(message):
    Button(message)

@bot.message_handler(regexp=r'[0-9]+')
def Check_num(message):
    link = 'https://khayyam2601.herokuapp.com/api/number'
    text = {"text":message.text}
    r = requests.post(link,data=json.dumps(text))
    data = json.loads(r.text)
    if data['code'] == 401:
        bot.send_message(message.from_user.id,"دسترسی غیر مجاز!!")
    else:
        bt = data['text']
        bot.send_message(message.from_user.id,bt)

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://khayyam2601.herokuapp.com/' + TOKEN)
    return "!",200


#
# bot.polling()