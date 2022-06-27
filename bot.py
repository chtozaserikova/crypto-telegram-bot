import requests
import telebot
import schedule
import time
from main import *
from telebot import types

'''
мы можем мониторить результаты, отправля запросы каждые полчаса. Результаты - сохранять в БД и после сверять значения.
Как только произойдет резкое увеличение суммы - пора закупаться. 
'''

bot = telebot.TeleBot('token')

def main():
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    key1 = types.KeyboardButton('Список ордеров')
    key2 = types.KeyboardButton('Инфо')
    key3 = types.KeyboardButton('Просмотр сделок')
    markup.add(key1, key2, key3)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в моего бота по торговле на бирже Yobit', reply_markup=main())

@bot.message_handler(commands=['info'])
def info(message):
	global current, inp_token
	inp_token = False
	current = 'info'
	bot.send_message(message.from_user.id, "Какая криптовалюта? \nПример: btc", reply_markup=types.ReplyKeyboardRemove())
def cont(message):
    if message.text == 'Инфо':
        bot.send_message(message.chat.id, get_ticker, reply_markup=main())
    elif message.text == 'Список ордеров':
        bot.send_message(message.chat.id, get_depth, reply_markup=main())
    elif message.text == 'Просмотр сделок':
        bot.send_message(message.chat.id, get_trades, reply_markup=main())

#   [-] =======================================================================>



if __name__ == '__main__':
    main()


bot.polling(none_stop=True)