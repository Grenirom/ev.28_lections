import telebot
from Mytoken import token
from telebot import types
import csv

#InlineKEyboardMarkup
#ReplyKeyboardMarkup

bot = telebot.TeleBot(token)

entry = {}

inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Доход', callback_data='income')
btn2 = types.InlineKeyboardButton('Расход', callback_data='costs')
inline_keyboard.add(btn1, btn2)


@bot.message_handler(commands=['start', 'hello'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет, выбери нужную опцию:', reply_markup=inline_keyboard)

@bot.callback_query_handler(func= lambda c: True)
def inline(c):
    if c.data == 'income':
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Работа')
        k2 = types.KeyboardButton('Подработки')
        k3 = types.KeyboardButton('Другое...')
        income_keyboard.add(k1, k2, k3)
        msg = bot.send_message(chat_id, 'Выберите категорию:', reply_markup=income_keyboard)
        bot.register_next_step_handler(msg, get_category_income)

    if c.data == 'costs':
        chat_id = c.message.chat.id
        costs_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Проезд')
        k2 = types.KeyboardButton('Еда')
        k3 = types.KeyboardButton('Развлечения')
        k4 = types.KeyboardButton('Другое...')
        costs_keyboard.add(k1, k2, k3, k4)
        msg = bot.send_message(chat_id, 'Выберите категорию:', reply_markup=costs_keyboard)
        bot.register_next_step_handler(msg, get_category_costs)



def get_category_income(message):
    chat_id = message.chat.id
    entry.update({'category': message.text}) # == entry['category'] = message.text
    msg = bot.send_message(chat_id, 'Укажите сумму:')
    bot.register_next_step_handler(msg, get_summ_income)

def get_summ_income(message):
    chat_id = message.chat.id
    entry.update({'summary': message.text})

    file_name = 'income.csv'

    with open(file_name, 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow( (entry['category'], entry['summary']) )

    bot.send_message(chat_id, 'Ваши доходы были успешно внесены в таблицу!', reply_markup=inline_keyboard)


def get_category_costs(message):
    chat_id = message.chat.id
    entry.update({'category': message.text})
    msg = bot.send_message(chat_id, 'Укажите сумму:')
    bot.register_next_step_handler(msg, get_summ_costs)


def get_summ_costs(message):
    chat_id = message.chat.id
    entry.update({'summary': message.text})

    file_name = 'costs.csv'

    with open(file_name, 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow( (entry['category'], entry['summary']) )
        bot.send_message(chat_id, 'Ваши расходы были успешно внесены в таблbцу!', reply_markup=inline_keyboard)

bot.polling()
