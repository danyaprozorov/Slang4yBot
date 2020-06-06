import telebot
import cfg
from telebot import types

bot = telebot.TeleBot(cfg.TOKEN)


class user:
    def __init__(self, id):
        self.id = id



@bot.message_handler(commands=['start'])
def start(message):
    Nikita.id = f'{message.from_user.id}'
    bot.send_message(message.chat.id, 'Привет, я бот такой-то')
    bot.send_message(message.chat.id, 'Я помогу тебе то-то')
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_hello = types.KeyboardButton('Hello')
    markup_reply.add(item_hello)
    bot.send_message(message.chat.id, 'Чтобы меня юзать жми на кнопки', reply_markup=markup_reply)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, f'Отлично! рад видеть тебя, {message.from_user.first_name}')
        bot.send_message(message.chat.id, 'Снизу меню, с чего начнем?')



Nikita = user(0)
bot.polling(none_stop=True)
