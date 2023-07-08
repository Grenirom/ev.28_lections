import telebot
from telebot import types
import random

token = '6151607580:AAFXC0c1H9pfKcq1Iw_XC6Ijvexjrp1XtTo'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Да')
btn2 = types.KeyboardButton('Нет')
keyboard.add(btn1, btn2)



@bot.message_handler(commands=['start','game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Привет King, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)
    
def check_answer(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Ok!\nВот правила игры:\nНужно угадать число которое я загадаю в диапозоне от 1-10(включительно)!\n Если не угадаешь, я тебя повешу! :)')
        number = random.randint(1,10)
        game(message, 3, number)

    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Пока!')
    else:
        bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильный ответ!\nВведите повторно!', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)


def game(message, attempts, number):
    message_bot = bot.send_message(message.chat.id, 'Выбери число:')
    bot.register_next_step_handler(message_bot, check_number, attempts-1, number)

def check_number(message, attempts, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Ты Угадал!')
    elif attempts == 0:
        bot.send_message(message.chat.id, 'Попытки закончились!\nТы проиграл!')
    else:
        bot.send_message(message.chat.id, 'Нет, ты не угадал число!\nПробуй еще раз!')
        game(message, attempts, number)
        

bot.polling()