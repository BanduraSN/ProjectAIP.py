import telebot
from telebot import types
from time import sleep
import random
import json
import sqlite3

with open('token.txt', 'r') as file:
    tok = file.read()

token = tok
bot = telebot.TeleBot(token)

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()


def add_db(user_id: int, user_name: str, user_surname: str, username: str):
    """
    Функция отвечает за добавление пользователя в базу данных
    :param user_id: Айди телеграмм пользователья
    :param user_name: Имя телеграмм пользователья
    :param user_surname: Фамилия телеграмм пользователья
    :param username: Псевдоним телеграмм пользователья
    :return: Новый пользователь в БД
    """
    cursor.execute('INSERT OR IGNORE INTO Subs (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start', 'help'])
def start_m(message):
    """
    Функцию отправляет пользователю сообщение с приветствием
    :param message: /start , /help
    :return: Приветствие
    """
    bot.send_message(message.chat.id, "Привет, тебя приветствует бот, который поможет тебе найти фильм на этот вечер, "
                                      "чтобы найти фильм, напиши Подбор")

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_sname = message.from_user.last_name
    username = message.from_user.username

   # add_db(user_id=user_id, user_name=user_name, user_surname=user_sname, username=username)


@bot.message_handler(commands=['Подбор', 'podbor'])
def start_podbor(message):
    """
    Функция добавления клавишей и выбором пользователя,
    фильм какого жанра от желает посмотреть
    :param message: /Подбор, /podbor
    :return: Добавляет пользователю клавиши для выбора жанра
    """
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

    mark.add(it1, it2, it3, it4, it5, it6, it7, it8, it9)
    bot.send_message(message.chat.id,'Сейчас посмотрим, что у нас есть', reply_markup=mark)
    bot.send_message(message.chat.id, 'Фильм какого жанра, вы хотели бы посмотреть')


@bot.message_handler(content_types='text')
def category_answer(message):
    """
    Функция поиска случайных фильмов по жанрам
    :param message: Выбранный жанр
    :return: Список фильмов(Если правильно введён жанр)
    или сообщение о неправильном вводе жанра
    """
    if message.text == '❤Драма❤':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/Drama.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == '⚔Боевик⚔':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/action.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == 'Фантастика👽':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/Sci-fi.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == '💀Ужасы💀':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/horror.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == '😹Комедия😹':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/comedy.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == '🕵🏻Триллер🕵🏻':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/thriller.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == 'Приключения🌏':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/adventure.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == '👮🏻‍♀Военный👮🏻‍♀':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/military.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    elif message.text == 'Мультфильм👾':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton(text='Подбор')
        mark.add(it1)
        with open('Films/animation.json', encoding='utf-8-sig') as file:
            a = json.load(file)
        random_films = random.choices(a, k=3)
        answer = ''
        for i in range(len(random_films)):
            answer += 'Название фильма: ' + random_films[i]['Название'] + '\n' + 'Год выпуска ' + random_films[i][
                'Год'] + '\n' + 'Рейтинг ' + random_films[i]['Рейтинг'] + '\n' + '\n'
        bot.send_message(message.chat.id, 'Жанр, который вы выбрали: ' + str(message.text), reply_markup=mark)
        sleep(1)
        bot.send_message(message.chat.id, 'Предлагаем Вам посмотреть эти фильмы:' + '\n' + '\n' + answer)
        sleep(2)
        bot.send_message(message.chat.id, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')



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

        mark.add(it1, it2, it3, it4, it5, it6, it7, it8, it9)
        bot.send_message(message.chat.id, 'Фильм какого жанра, вы хотели бы посмотреть', reply_markup=mark)



    else:
        bot.send_message(message.chat.id,
                         'Кажется, ты ошибся, я не разговорчивый бот, напиши одну из команд ( /start,  /help )')

if __name__ == '__main__':
    bot.polling(none_stop=True)
