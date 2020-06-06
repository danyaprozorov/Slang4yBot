import telebot
import cfg
import random
from telebot import types

bot = telebot.TeleBot(cfg.TOKEN)


class Words(object):
    def __init__(self, wrd, trans, diff, topic, img, prog, prog2):
        self.wrd = wrd
        self.trans = trans
        self.diff = diff
        self.topic = topic
        self.img = img
        self.prog = prog
        self.prog2 = prog2


class user:
    def __init__(self, id, choic):
        self.id = id
        self.choic = choic


@bot.message_handler(commands=['start'])
def start(message):
    nikita.id = f'{message.from_user.id}'
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
        choice(message)
    if message.text == 'Главное меню':
        main_menu(message)
    if message.text == 'Изучить':
        wordss[nikita.choic].prog = 1
        nikita.choic += 1
        choice(message)
    if message.text == 'Отложить':
        nikita.choic += 1
        choice(message)
    if message.text == 'Я знаю это слово':
        wordss[nikita.choic].prog = 2
        nikita.choic += 1
        choice(message)
    if message.text == 'Учить слова':
        learn(message)
    if message.text == 'Изучаемые слова':
        learnwords(message)
#    if message.text == 'Начать изучение':
#        try:
#            i = 0
#            j = 1
#            while i < 4:
#                if wordss[i].prog == 1:
#                    j += 1
#                i += 1
#            if j == 1:


def learnwords(message):
    i = 0
    j = 1
    while i < 4:
        if wordss[i].prog == 1:
            bot.send_message(message.chat.id, str(j) + '. ' + wordss[i].wrd + ' [' + str(wordss[i].prog2) + '/4]')
            j += 1
        i += 1
    if j == 1:
        bot.send_message(message.chat.id, 'Нет изучемых слов, пополните их в разделе Выбор слов')
        main_menu(message)
    else:
        have(message)

def have(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать изучение')
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_start, item_back)
    bot.send_message(message.chat.id, 'Выбирай)', reply_markup=markup_reply)


def learn(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать изучение')
    item_have = types.KeyboardButton('Изучаемые слова')
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_start, item_have, item_back)
    bot.send_message(message.chat.id, 'Выбирай)', reply_markup=markup_reply)


def choice(message):
    try:
        if wordss[nikita.choic].prog == 0:
            bot.send_animation(message.chat.id, open(wordss[nikita.choic].img, 'rb'))
            bot.send_message(message.chat.id, wordss[nikita.choic].wrd + ' - ' + wordss[nikita.choic].trans)
            bot.send_message(message.chat.id, wordss[nikita.choic].diff)
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_yes = types.KeyboardButton('Изучить')
            item_no = types.KeyboardButton('Отложить')
            item_know = types.KeyboardButton('Я знаю это слово')
            item_back = types.KeyboardButton('Главное меню')
            markup_reply.add(item_yes, item_no, item_know, item_back)
            bot.send_message(message.chat.id, 'Жми на кнопку)', reply_markup=markup_reply)
        else:
            nikita.choic += 1
            if nikita.choic >= 4:
                nikita.choic = 0
                choice(message)
            else:
                choice(message)
    except BaseException:
        bot.send_message(message.chat.id, 'Слова для изучения закончились(')
        bot.send_message(message.chat.id, 'Выучите еще неизученные слова или ждите добавления новых')
        nikita.choic = 0
        main_menu(message)


def main_menu(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_progress = types.KeyboardButton('Мой прогресс')
    item_choice = types.KeyboardButton('Выбор слов')
    item_learn = types.KeyboardButton('Учить слова')
    item_topic = types.KeyboardButton('Выбор топика')
    markup_reply.add(item_progress, item_choice, item_learn, item_topic)
    bot.send_message(message.chat.id, 'Жми на кнопку)', reply_markup=markup_reply)


wordss = []
learning = []
i = 0
f = open("words1.txt", "r", encoding='utf-8')
while i < 16:
    wordss.append(Words(f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip(),
                        f.readline().strip(), f.readline(), f.readline()))
    i += 1
f.close()
i = 0
while i < 4:
    wordss[i].prog = int(wordss[i].prog)
    wordss[i].prog2 = int(wordss[i].prog2)
    i += 1
nikita = user(0, 0)
bot.polling(none_stop=True)
