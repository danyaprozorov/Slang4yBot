import telebot
import cfg
import random
from telebot import types
import datetime
import time

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
    def __init__(self, id, choic, lear, inproc):
        self.id = id
        self.choic = choic
        self.lear = lear
        self.inproc = inproc

class game:
    def __init__(self, gnum, answer, mod, word, learned):
        self.gnum = gnum
        self.answer = answer
        self.mod = mod
        self.word = word
        self.learned = learned

class date:
    def __init__(self, day, month, today, max):
        self.day = day
        self.month = month
        self.today = today
        self.max = max

@bot.message_handler(commands=['start'])
def start(message):
    nikita.id = f'{message.from_user.id}'
    bot.send_message(message.chat.id, 'Привет, меня зовут Slang4uBot')
    time.sleep(2)
    bot.send_message(message.chat.id, 'Я буду твоим личным помощником в изучении английского языка с помощью '
                                      'слэнговых выражений')
    time.sleep(2)
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_hello = types.KeyboardButton('Привет 👋')
    markup_reply.add(item_hello)
    bot.send_message(message.chat.id, 'Мы будем общаться с помощью кнопок. Нажимай...', reply_markup=markup_reply)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == game.answer and game.answer != 'no':
        if game.mod == 3:
            game.mod = -1
        game.mod += 1
        bot.send_message(call.message.chat.id, 'Да! так держать 👍')
        game.answer = 'no'
        i = -1
        while game.word != wordss[i].wrd:
            i += 1
            if game.word == wordss[i].wrd:
                wordss[i].prog2 += 1
                if wordss[i].prog == 0:
                    wordss[i].prog = 1
                if wordss[i].prog2 >= 4:
                    wordss[i].prog2 = 0
                    wordss[i].prog = 2
                    game.learned += 1
                    time1()
    elif game.answer != 'no':
        bot.send_message(call.message.chat.id, 'Кажется, ты ошибся 👎')
        if game.mod == 3:
            game.mod = -1
        game.mod += 1
        game.answer = 'no'
    if game.gnum == 60:
        learning.clear()
        nikita.lear = 0
        bot.send_message(call.message.chat.id, 'На это все) В этот раз' + str(game.learned) + ' слов(а))')
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_back = types.KeyboardButton('Главное меню')
        markup_reply.add(item_back)
        bot.send_message(call.message.chat.id, 'Жмякай', reply_markup=markup_reply)
    else:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_next = types.KeyboardButton('Продолжить')
        item_back = types.KeyboardButton('Главное меню')
        markup_reply.add(item_next, item_back)
        bot.send_message(call.message.chat.id, 'Летим дальше? 🚀', reply_markup=markup_reply)

@bot.message_handler(content_types=['text'])
def get_text(message):
    saves()
    if message.text == 'Привет 👋':
        time.sleep(2)
        bot.send_message(message.chat.id, f'Ну наконец-то, я уже тебя заждался, {message.from_user.first_name}')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Немного вводной информации перед тем, как мы начнем')
        time.sleep(2)
        bot.send_message(message.chat.id, 'У меня есть несколько функций:')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Мой прогресс(ты всегда можешь отслеживать свою успеваемость и смотреть, '
                                          'сколько времени ты провел со мной)')
        time.sleep(2)
        bot.send_message(message.chat.id,
                         'Выбор слов(я не хочу давить на тебя своим авторитетом, так что ты сам можешь '
                         'выбирать, что учить). Давай-ка я тебе все разжую: тапнув на эту вкладку у тебя '
                         'появится первый сленг для изучения и откроется 3 пункта: "изучить", '
                         '"отложить" и "я знаю это слово". Выбрав первый пункт, это слово переместится '
                         'во вкладку "учить слова", где ты сможешь попрактиковаться. Выбрав второй '
                         'пункт, ты откладываешь изучение этого слова на потом, но не волнуйся, '
                         'ты всегда сможешь к нему вернуться. Третий пункт удаляет слово из базы данных '
                         'и помечает его как изученное.')
        time.sleep(2)
        bot.send_message(message.chat.id,
                         'Учить слова(думаю, тут объяснять ничего не нужно, тапай кнопку и открывай для '
                         'себя неизведанные слэнги)')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Топики(ты можешь сам выбрать топики из предложенного списка, но будь '
                                          'осторожен, самый последний очень коварный и предназначен исключительно для '
                                          'пользователей 🔞). Выбрав, понравившийся топик, твоим очам предстанут 5 '
                                          'умопомрачительных слэнгов, после этого тебя ожидает небольшая практика, '
                                          'которую ты можешь остановить в любой момент, просто выйдя в главное меню(чтобы '
                                          'открыть новые слова, просто перезапусти понравившийся топик)')
        time.sleep(2)
        bot.send_message(message.chat.id, 'C чего начнем?')
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
        time1()
        nikita.choic += 1
        choice(message)
    if message.text == 'Учить слова':
        learn(message)
    if message.text == 'Изучаемые слова':
        learnwords(message)
    if message.text == 'Начать изучение':
        learni(message)
    if message.text == 'Следущие':
        nikita.lear += 1
        if nikita.lear < 5:
            rep(message)
        else:
            nikita.lear = 0
            bot.send_message(message.chat.id, 'Ты готов начать?')
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_startt = types.KeyboardButton('Начать')
            item_back = types.KeyboardButton('Главное меню')
            markup_reply.add(item_startt, item_back)
            bot.send_message(message.chat.id, 'Выбирай)', reply_markup=markup_reply)
    if message.text == 'Начать':
        game.gnum = 0
        game.mod = 0
        game.learned = 0
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_back = types.KeyboardButton('Главное меню')
        markup_reply.add(item_back)
        bot.send_message(message.chat.id, 'Выбирай)', reply_markup=markup_reply)
        gamek(message)
    if message.text == 'Продолжить':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_back = types.KeyboardButton('Главное меню')
        markup_reply.add(item_back)
        bot.send_message(message.chat.id, 'Выбирай)', reply_markup=markup_reply)
        if game.mod == 0 or game.mod == 2:
            gamek(message)
        else:
            gamer(message)
    if message.text == 'Выбор топика':
        topicchoice(message)
    if message.text == 'Daily' or message.text == 'Relevant' or message.text == 'Fcking slang':
        topiccheck(message)
    if message.text == 'Мой прогресс':
        progress(message)


def progress(message):
    time2()
    bot.send_message(message.chat.id, '🔥 Словарный запас: ' + wordbase())
    bot.send_message(message.chat.id, '🔥 Наибольшее количество новых слов за день: ' + str(date.max))
    bot.send_message(message.chat.id, '🔥 Сегодня слов выучено: ' + str(date.today))
    bot.send_message(message.chat.id, '🔥 В процессе изучения: ' + inlearning())
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_back)
    bot.send_message(message.chat.id, 'Ничиго себе результаты🔝', reply_markup=markup_reply)


def wordbase():
    i = 0
    j = 0
    while i < 45:
        if wordss[i].prog == 2:
            j += 1
        i += 1
    return str(j)


def inlearning():
    i = 0
    j = 0
    while i < 45:
        if wordss[i].prog2 > 0 and wordss[i].prog == 1:
            j += 1
        i += 1
    return str(j)


def topicchoice(message):
    bot.send_message(message.chat.id, '1⃣ Daily')
    bot.send_message(message.chat.id, '2⃣ Relevant')
    bot.send_message(message.chat.id, '3⃣ Fcking slang')
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_progress = types.KeyboardButton('Daily')
    item_choice = types.KeyboardButton('Relevant')
    item_learn = types.KeyboardButton('Fcking slang')
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_progress, item_choice, item_learn, item_back)
    bot.send_message(message.chat.id, 'Выбирай тему)', reply_markup=markup_reply)


def topiccheck(message):
    topic = message.text.lower()
    i = 0
    learning.clear()
    j = 0
    while i < 45:
        if wordss[i].prog != 2 and wordss[i].topic == topic:
            learning.append(wordss[i])
            j += 1
        i += 1
        if j == 5:
            break
    if j < 5 and j != 0:
        learning.clear()
        bot.send_message(message.chat.id, 'В этом топике оталось слишком мало слов, найдите их в "Выборе слов"')
        topicchoice()
    elif j == 0:
        bot.send_message(message.chat.id, 'Ты знаешь все слова из этого топика😉')
        topicchoice(message)
    else:
        bot.send_message(message.chat.id, 'Давай повторим слова😉')
        rep(message)


def gamek(message):
    try:
        if game.mod == 0:
            bot.send_photo(message.chat.id, open('./imgs/' + learning[numbrs[game.gnum] - 1].img, 'rb'))
            game.word = learning[numbrs[game.gnum] - 1].wrd
        if game.mod == 2:
            bot.send_message(message.chat.id, learning[numbrs[game.gnum] - 1].trans)
            game.word = learning[numbrs[game.gnum] - 1].wrd
    except BaseException:
        bot.send_message(message.chat.id, 'Произошла ошибка, перезайди, пожалуйста')
        main_menu(message)
    r = random.randint(1, 3)
    if r == 1:
        game.answer = 'a'
        r = learning[numbrs[game.gnum] - 1].wrd
        a = r
        game.gnum += 1
        b = learning[numbrs[game.gnum] - 1].wrd
        game.gnum += 1
        с = learning[numbrs[game.gnum] - 1].wrd
        game.gnum += 1
    elif r == 2:
        game.answer = 'b'
        r = learning[numbrs[game.gnum] - 1].wrd
        b = r
        game.gnum += 1
        a = learning[numbrs[game.gnum] - 1].wrd
        game.gnum += 1
        с = learning[numbrs[game.gnum] - 1].wrd
        game.gnum += 1
    elif r == 3:
        game.answer = 'c'
        r = learning[numbrs[game.gnum] - 1].wrd
        с = r
        game.gnum += 1
        a = learning[numbrs[game.gnum] - 1].wrd
        game.gnum += 1
        b = learning[numbrs[game.gnum] - 1].wrd
        game.gnum += 1
    markup_inline = types.InlineKeyboardMarkup()
    item_a = types.InlineKeyboardButton(text=a, callback_data='a')
    markup_inline.add(item_a)
    item_b = types.InlineKeyboardButton(text=b, callback_data='b')
    markup_inline.add(item_b)
    item_c = types.InlineKeyboardButton(text=с, callback_data='c')
    markup_inline.add(item_c)
    if game.mod == 0:
        bot.send_message(message.chat.id, '☝ Какой вариант описывает картинку?', reply_markup=markup_inline)
    if game.mod == 2:
        bot.send_message(message.chat.id, '☝ Переведи слово', reply_markup=markup_inline)


def gamer(message):
    try:
        if game.mod == 1:
            bot.send_message(message.chat.id, learning[numbrs[game.gnum] - 1].wrd)
            game.word = learning[numbrs[game.gnum] - 1].wrd
        if game.mod == 3:
            bot.send_message(message.chat.id, norus(learning[numbrs[game.gnum] - 1].diff))
            game.word = learning[numbrs[game.gnum] - 1].wrd
    except BaseException:
        bot.send_message(message.chat.id, 'Произошла ошибка, перезайди, пожалуйста ❗')
        main_menu(message)
    r = random.randint(1, 3)
    if r == 1:
        game.answer = 'a'
        r = learning[numbrs[game.gnum] - 1].trans
        a = r
        game.gnum += 1
        b = learning[numbrs[game.gnum] - 1].trans
        game.gnum += 1
        с = learning[numbrs[game.gnum] - 1].trans
        game.gnum += 1
    elif r == 2:
        game.answer = 'b'
        r = learning[numbrs[game.gnum] - 1].trans
        b = r
        game.gnum += 1
        a = learning[numbrs[game.gnum] - 1].trans
        game.gnum += 1
        с = learning[numbrs[game.gnum] - 1].trans
        game.gnum += 1
    elif r == 3:
        game.answer = 'c'
        r = learning[numbrs[game.gnum] - 1].trans
        с = r
        game.gnum += 1
        a = learning[numbrs[game.gnum] - 1].trans
        game.gnum += 1
        b = learning[numbrs[game.gnum] - 1].trans
        game.gnum += 1
    markup_inline = types.InlineKeyboardMarkup()
    item_a = types.InlineKeyboardButton(text=a, callback_data='a')
    markup_inline.add(item_a)
    item_b = types.InlineKeyboardButton(text=b, callback_data='b')
    markup_inline.add(item_b)
    item_c = types.InlineKeyboardButton(text=с, callback_data='c')
    markup_inline.add(item_c)
    if game.mod == 1:
        bot.send_message(message.chat.id, '☝ Переведи слово', reply_markup=markup_inline)
    if game.mod == 3:
        bot.send_message(message.chat.id, '☝ О чем идет речь?', reply_markup=markup_inline)


def learni(message):
    i = 0
    learning.clear()
    j = 0
    while i < 45:
        if wordss[i].prog == 1:
            learning.append(wordss[i])
            j += 1
        i += 1
        if j == 5:
            break
    if j < 5:
        learning.clear()
        bot.send_message(message.chat.id, 'Нужно выбрать как минимум 5 слова для изучения ❗')
        learn(message)
    else:
        bot.send_message(message.chat.id, 'Давай повторим слова😉')
        rep(message)


def rep(message):
    bot.send_photo(message.chat.id, open('./imgs/' + learning[nikita.lear].img, 'rb'))
    bot.send_message(message.chat.id, learning[nikita.lear].wrd + ' - ' + learning[nikita.lear].trans)
    bot.send_message(message.chat.id, learning[nikita.lear].diff)
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_next = types.KeyboardButton('Следущие')
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_next, item_back)
    bot.send_message(message.chat.id, '👆 Запоминай 👆', reply_markup=markup_reply)


def learnwords(message):
    i = 0
    j = 1
    while i < 45:
        if wordss[i].prog == 1:
            bot.send_message(message.chat.id, str(j) + '. ' + wordss[i].wrd + ' [' + str(wordss[i].prog2) + '/4]')
            j += 1
        i += 1
    if j == 1:
        bot.send_message(message.chat.id, 'Нет изучемых слов, пополните их в разделе Выбор слов ❗')
        main_menu(message)
    else:
        have(message)


def have(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать изучение')
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_start, item_back)
    bot.send_message(message.chat.id, 'Выбирай 👆', reply_markup=markup_reply)


def learn(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать изучение')
    item_have = types.KeyboardButton('Изучаемые слова')
    item_back = types.KeyboardButton('Главное меню')
    markup_reply.add(item_start, item_have, item_back)
    bot.send_message(message.chat.id, '👇 Выбирай', reply_markup=markup_reply)


def choice(message):
    try:
        if wordss[nikita.choic].prog == 0:
            bot.send_photo(message.chat.id, open('./imgs/' + wordss[nikita.choic].img, 'rb'))
            bot.send_message(message.chat.id, wordss[nikita.choic].wrd + ' - ' + wordss[nikita.choic].trans)
            bot.send_message(message.chat.id, wordss[nikita.choic].diff)
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_yes = types.KeyboardButton('Изучить')
            item_no = types.KeyboardButton('Отложить')
            item_know = types.KeyboardButton('Я знаю это слово')
            item_back = types.KeyboardButton('Главное меню')
            markup_reply.add(item_yes, item_no, item_know, item_back)
            bot.send_message(message.chat.id, '👇 Жми на кнопку', reply_markup=markup_reply)
        else:
            nikita.choic += 1
            if nikita.choic >= 45:
                nikita.choic = 0
                choice(message)
            else:
                choice(message)
    except BaseException:
        bot.send_message(message.chat.id, 'Слова для изучения закончились😥')
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
    bot.send_message(message.chat.id, '🔻 Жми на кнопку 🔻', reply_markup=markup_reply)


def norus(t):
    alphabet = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    lst = list(t)
    i = 0
    t = 0
    while i < len(lst):
        if t == 0:
            i += 1
        if lst[i] in alphabet:
            t = 1
        if t == 1:
            lst.pop(i)
    lst = "".join(lst)
    return [str(lst)]


def time1():
    x = datetime.datetime.now()
    if date.day == x.day and date.month == x.month:
        date.today += 1;
    else:
        if date.max < date.today:
            date.max = date.today
        date.today = 1
    date.day = x.day
    date.month = x.month
    saves()


def time2():
    x = datetime.datetime.now()
    if date.day != x.day or date.month != x.month:
        if date.max < date.today:
            date.max = date.today
        date.today = 0
    date.day = x.day
    date.month = x.month
    saves()


def saves():
    save = []
    save1 = []
    save1.append(str(date.day) + '\n')
    save1.append(str(date.month) + '\n')
    save1.append(str(date.today) + '\n')
    save1.append(str(date.max) + '\n')
    i = 0
    while i < len(wordss):
        save.append(str(wordss[i].wrd) + '\n')
        save.append(str(wordss[i].trans) + '\n')
        save.append(str(wordss[i].diff) + '\n')
        save.append(str(wordss[i].topic) + '\n')
        save.append(str(wordss[i].img) + '\n')
        save.append(str(wordss[i].prog) + '\n')
        save.append(str(wordss[i].prog2) + '\n')
        i += 1
    m = open("date.txt", "w", encoding='utf-8')
    m.writelines(save1)
    m.close
    m = open("date.txt", "r", encoding='utf-8')
    m.close
    f = open("words1.txt", "w", encoding='utf-8')
    f.writelines(save)
    f.close
    f = open("words1.txt", "r", encoding='utf-8')
    f.close


learning = []
wordss = []
numbrs = []
i = 0
f = open("words1.txt", "r", encoding='utf-8')
while i < 315:
    wordss.append(Words(f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip(),
                        f.readline().strip(), f.readline(), f.readline()))
    i += 1
f.close()
i = 0
while i < 45:
    wordss[i].prog = int(wordss[i].prog)
    wordss[i].prog2 = int(wordss[i].prog2)
    i += 1
i = 0
f = open("nums.txt", "r", encoding='utf-8')
while i < 60:
    numbrs.append(f.readline())
    i += 1
f.close()
i = 0
while i < 60:
    numbrs[i] = int(numbrs[i])
    i += 1
i = 0
f = open("date.txt", "r", encoding='utf-8')
date = date(f.readline(), f.readline(), f.readline(), f.readline())
f.close()
date.day = int(date.day)
date.month = int(date.month)
date.today = int(date.today)
date.max = int(date.month)
nikita = user(0, 0, 0, 0)
game = game(0, 'no', 0, 'no', 0)
bot.polling(none_stop=True)
