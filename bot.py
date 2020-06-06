import telebot
import cfg
from telebot import types

bot = telebot.TeleBot(cfg.TOKEN)


class Words(object):
    def __init__(self, wrd, trans, diff, topic, img):
        self.wrd = wrd
        self.trans = trans
        self.diff = diff
        self.topic = topic
        self.img = img


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
        bot.send_message(message.chat.id, f'Рад видеть тебя, {message.from_user.first_name}')
        bot.send_message(message.chat.id, 'Снизу меню, с чего начнем?')
        main_menu(message)
    if message.text == 'Выбор слов':



def main_menu(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_progress = types.KeyboardButton('Мой прогресс')
    item_choice = types.KeyboardButton('Выбор слов')
    item_learn = types.KeyboardButton('Учить слова')
    item_topic = types.KeyboardButton('Выбор топика')
    markup_reply.add(item_progress, item_choice, item_learn, item_topic)
    bot.send_message(message.chat.id, 'Жми на кнопку)', reply_markup=markup_reply)


wordss = []
i = 0
f = open("words1.txt", "r", encoding='utf-8')
while i < 16:
    wordss.append(Words(f.readline(), f.readline(), f.readline(), f.readline()., f.readline().strip()))
    i += 1
f.close

Nikita = user(0)
bot.polling(none_stop=True)
