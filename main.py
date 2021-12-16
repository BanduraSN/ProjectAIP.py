import telebot
from telebot import types
from time import sleep
import random
import json
import sqlite3

with open('C:/Users/79776/Desktop/о/token.txt', 'r') as file:
    tok = file.read()

token = tok
bot = telebot.TeleBot(token)

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()


def add_db(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT OR IGNORE INTO Subs (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start', 'help'])
def start_m(message):
    bot.send_message(message.chat.id, "Привет, тебя приветствует бот, который поможет тебе найти фильм на этот вечер, "
                                      "чтобы найти фильм, напиши команду /Подбор или просто напиши Подбор")

    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    add_db(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


@bot.message_handler(commands=['Подбор', 'command3', 'podbor'])
def start_podbor(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    it1 = types.KeyboardButton(text='❤Драма❤')
    it2 = types.KeyboardButton(text='⚔Боевик⚔')
    it3 = types.KeyboardButton(text='😹Комедия😹')
    it4 = types.KeyboardButton(text='Мультфильм👾')
    it5 = types.KeyboardButton(text='💀Ужасы💀')
    it6 = types.KeyboardButton(text='Фантастика👽')
    it7 = types.KeyboardButton(text='🕵🏻Триллер🕵🏻')
    it8 = types.KeyboardButton(text='👮🏻‍♀Военный👮🏻‍♀')
    it9 = types.KeyboardButton(text='Приключения🌏')
    it10 = types.KeyboardButton(text='Назад')

    mark.add(it1, it2, it3, it4, it5, it6, it7, it8, it9, it10)
    bot.send_message(message.chat.id, 'Фильм какого жанра, вы хотели бы посмотреть', reply_markup=mark)


@bot.message_handler(content_types='text')
def category_answer(message):
    if message.text == '❤Драма❤':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/Drama.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == '⚔Боевик⚔':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/action.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == 'Фантастика👽':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/Sci-fi.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == '💀Ужасы💀':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/horror.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == '😹Комедия😹':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/comedy.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == '🕵🏻Триллер🕵🏻':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/thriller.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == 'Приключения🌏':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/adventure.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == '👮🏻‍♀Военный👮🏻‍♀':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/military.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == 'Мультфильм👾':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Назад')
        mark.add(it1)
        with open('Films/animation.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random4 = random.choices(a, k=3)
        ffd = ''
        for i in range(len(random4)):
            ffd += 'Название фильма: ' + random4[i]['Название'] + '\n' + 'Год выпуска ' + random4[i][
                'Год'] + '\n' + 'Рейтинг ' + random4[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + ffd)

    elif message.text == 'Назад':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        bot.send_message(message.chat.id, 'Нажмите на эту классную кнопку и мы найдем вам фильм)', reply_markup=mark)

    elif message.text == 'Подбор' or message.text == 'подбор':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='❤Драма❤')
        it2 = types.KeyboardButton(text='⚔Боевик⚔')
        it3 = types.KeyboardButton(text='😹Комедия😹')
        it4 = types.KeyboardButton(text='Мультфильм👾')
        it5 = types.KeyboardButton(text='💀Ужасы💀')
        it6 = types.KeyboardButton(text='Фантастика👽')
        it7 = types.KeyboardButton(text='🕵🏻Триллер🕵🏻')
        it8 = types.KeyboardButton(text='👮🏻‍♀Военный👮🏻‍♀')
        it9 = types.KeyboardButton(text='Приключения🌏')
        it10 = types.KeyboardButton(text='Назад')

        mark.add(it1, it2, it3, it4, it5, it6, it7, it8, it9, it10)
        bot.send_message(message.chat.id, 'Фильм какого жанра, вы хотели бы посмотреть', reply_markup=mark)



    else:
        bot.send_message(message.chat.id,
                         'Кажется, ты ошибся, я не разговорчивый бот, напиши одну из команд( /start,  /help,  /Подбор )')


bot.polling(none_stop=True)
