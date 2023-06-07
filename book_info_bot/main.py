import telebot
import requests
import json
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

    titles = [item['title'] for item in req_data]
    titles_text = '\n'.join(titles)

    bot.send_message(message.chat.id, titles_text)

@bot.message_handler(func=lambda message: True)
def author(message):
    data = requests.get(f'http://127.0.0.1:8000/api_author/{message.text}')
    req_data = data.json()
    about = [str(value) for value in req_data.values()]
    about_text = '\n'.join(about)
    bot.send_message(message.chat.id, about_text)


bot.polling()
