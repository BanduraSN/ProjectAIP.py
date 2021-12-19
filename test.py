from unittest.mock import MagicMock
import unittest
import mock
import main


class TG(unittest.TestCase):
    @mock.patch('main.bot')
    def test_start(self, main_bot):
        name='test'
        user=MagicMock(first_name=name)
        chat= MagicMock(id=1)
        message = MagicMock(from_user=user,chat=chat)
        main.start_m(message=message)
        main.bot.send_message.assert_called_with(1, 'Привет, тебя приветствует бот, который поможет тебе найти фильм на этот вечер, чтобы найти фильм, напиши Подбор')

    @mock.patch('main.bot')
    def test_podbor(self, main_bot, answer='folms'):
        name = 'test1'
        user = MagicMock(first_name=name)

        chat = MagicMock(id=1)
        message = MagicMock(text='❤Драма❤', chat=chat)
        main.category_answer(message)
        main.bot.send_message.assert_called_with(1, 'Чтобы снова подобрать фильмы, нажмите на кнопку Подбор')

    @mock.patch('main.bot')
    def test_answer(self, main_bot, answer='folms'):
        name = 'test1'
        user = MagicMock(first_name=name)

        chat = MagicMock(id=1)
        message = MagicMock(from_user=user, chat=chat)
        main.start_podbor(message)
        main.bot.send_message.assert_called_with(1, 'Фильм какого жанра, вы хотели бы посмотреть')

    @mock.patch('main.bot')
    def test_error(self, main_bot, answer='folms'):
        name = 'test1'
        user = MagicMock(first_name=name)

        chat = MagicMock(id=1)
        message = MagicMock(from_user=user, chat=chat)
        main.category_answer(message)
        main.bot.send_message.assert_called_with(1, 'Кажется, ты ошибся, я не разговорчивый бот, напиши одну из команд ( /start,  /help )')
