from config import token
from random import choice
import telebot

bot = telebot.TeleBot(token)

# Handle '/coin'
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)
# Handle '/fact'
@bot.message_handler(commands=['fact'])
def coin_handler(message):
    fact = choice(["I'm the best bot ever!", "I'm super cute!"])
    bot.reply_to(message, fact)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hellow world!")

# Handle '/info'
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, "stable")

# Handle all other messages with content_type 'photo'
@bot.message_handler(content_types=['photo'])
def echo_message(message):
    bot.reply_to(message, "Wonderful image!")

@bot.message_handler(content_types=['gif'])
def echo_message(message):
    bot.reply_to(message, "Wow!")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()