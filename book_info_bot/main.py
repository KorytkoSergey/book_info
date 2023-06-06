import telebot
import requests

key_for_bot = '6033095543:AAHTwZvPtmA7sXuWbRI_eiq2UGbcgfkHU5Y'
key_for_book = ''
bot = telebot.TeleBot(key_for_bot)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=['book_list'])
def book_list(message):
    data = requests.get(f'http://127.0.0.1:8000/api_book/')
    req_data = data.json()
    bot.send_message(message.chat.id, str(req_data))

bot.polling()
