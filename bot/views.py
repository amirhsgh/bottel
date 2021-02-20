from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Button,NumberId
import json
import telebot
import requests
from telebot.types import ReplyKeyboardMarkup,KeyboardButton
TOKEN = '1656459425:AAEymoNrG9_OP5yJh1vkXRJur4gkJoWh9-I'
bot = telebot.TeleBot(TOKEN)

class GetList(APIView):
    def get(self,request):
        # df = pd.read_excel("mm.xlsx")
        # a = df['A']
        # b = df['B']
        # for i,j in zip(b,a):
        #     Button.objects.create(button=j).save()
        #     NumberId.objects.create(button=Button.objects.get(button=j),text=).save()

        data = {'list':[]}
        button = Button.objects.all()
        for i in button:
            data['list'].append({'name':i.button})
        return Response(data)

class NumberBut(APIView):
    def post(self,request):
        data = json.loads(request.body)
        try:
            get_butt = Button.objects.get(button=data['text'])
            text = NumberId.objects.get(button=get_butt)
            return Response({"text":text.text,"code":200})
        except:
            return Response({"code":401})



def Button(message):
    r = requests.get('https://khayyam2601.herokuapp.com/api/button/')
    data = json.loads(r.text)
    key = ReplyKeyboardMarkup(True,False)
    text = "سلام {} شماره دانشجویی تو وارد کن :)".format(message.from_user.first_name)
    bot.send_message(message.from_user.id,text,reply_markup=key)

@bot.message_handler(commands=['start'])
def start(message):
    Button(message)

@bot.message_handler(regexp=r'[0-9]+')
def Check_num(message):
    link = 'https://khayyam2601.herokuapp.com/api/number/'
    text = {"text":message.text}
    r = requests.post(link,data=json.dumps(text))
    data = json.loads(r.text)
    if data['code'] == 401:
        bot.send_message(message.from_user.id,"دسترسی غیر مجاز!!")
    else:
        bt = data['text']
        bot.send_message(message.from_user.id,bt)

import time
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        time.sleep(15)