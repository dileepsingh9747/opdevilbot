import os

from flask import Flask, request

import telebot

TOKEN = '1345444847:AAEl65PK-p3kDkp3ufhO4A-WiBq5lxn89g0'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,text='chup ker maderchod')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://opakhilbot.herokuapp.com/' + "1345444847:AAEl65PK-p3kDkp3ufhO4A-WiBq5lxn89g0")
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))