
import telebot
from telebot import types
import random 

token = '5776918891:AAGapZCEZsWALZ1b0-yYUfXs-FYeSGL7mkE'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton("Да")

button2 = types.KeyboardButton('Нет')

keyboard.add(button1, button2)

@bot.message_handler(commands=['start', 'hello', 'hi'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGZHJjb2jsdcyM37HilJvwckYfs1PiVwAC2gADWuOKFz_0I1hYuGhpKwQ')
    msg = bot.send_message(message.chat.id, f"Привет, {message.chat.first_name}! Ехала?", reply_markup=keyboard)
    bot.register_next_step_handler(msg, check_answer) 


def check_answer(message):
    if message.text == "Да":
        bot.send_message(message.chat.id, "ок! Вот правила игры: нужно угадать число от 1 до 10 за 3 попытки ")
        random_number = random.choice(range(1, 11))
        print(random_number)
        game(message, 3, random_number)
    else:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGZHpjb2nc58lj8uACMcfv_ck5y848VwAC2wADWuOKF7VzytcUYD7WKwQ")

def game(message, attempts, random_number):
    msg = bot.send_message(message.chat.id, "Делай, делай")
    bot.register_next_step_handler(msg, check_number, attempts -1, random_number)

def check_number(message, attempts, random_number):
    if message.text == str(random_number):
        bot.send_message(message.chat.id, "Базар джексон, фартовый ты")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGZEVjb2ND3qgbbZBuqTyI170yyZ9d6AAC_AIAAn3Ssw1pSs1DWcHaqisE")

    elif attempts == 0:
        bot.send_message(message.chat.id, f"Лох педальный Число было {random_number}")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEGZHRjb2kZXsd_JnlG-yRzhRoGslpi7QACIQMAAn3Ssw2TKT7-aQABb4YrBA")
    else:
        bot.send_message(message.chat.id, f"По новой, у тебя осталось {attempts} попыток" )
        game(message, attempts, random_number)
    

bot.polling()