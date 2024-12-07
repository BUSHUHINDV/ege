import telebot
from telebot import types
import requests
from geopy import geocoders

#from os import environ

bot=telebot.TeleBot('5826273791:AAFAjzu7JRfvyw4ogpBZqlHKNyRPP_NK9-4')
token_yandex ='461f3755-0a28-4825-a573-7c73b5e35e9a'

city='Урай'
geolocator = geocoders.Nominatim(user_agent="telebot")
latitude = str(geolocator.geocode(city).latitude)
longitude = str(geolocator.geocode(city).longitude)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать погоду")
    markup.add(btn1)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Узнать погоду"):
        #https://yandex.ru/pogoda/uray?lat=60.122719&lon=64.785118
        # Задаем координаты населенного пункта
        lat = 60.122719  # широта Москвы
        lon = 64.785118  # долгота Москвы

        # Задаем параметры запроса
        params = {
            'lat': lat,
            'lon': lon,
            'lang': 'ru_RU',  # язык ответа
            'limit': 7,  # срок прогноза в днях
            'hours': True,  # наличие почасового прогноза
            'extra': False  # подробный прогноз осадков
        }

        # Задаем значение ключа API
        api_key = '461f3755-0a28-4825-a573-7c73b5e35e9a'

        # Задаем URL API
        url = 'https://api.weather.yandex.ru/v2/forecast'

        # Делаем запрос к API
        response = requests.get(url, params=params, headers={'X-Yandex-API-Key': api_key})

        # Проверяем статус ответа
        if response.status_code == 200:
            # Преобразуем ответ в JSON формат
            data = response.json()
            # Выводим данные о текущей погоде
            print(f'Температура воздуха: {data["fact"]["temp"]} °C')
            print(f'Ощущается как: {data["fact"]["feels_like"]} °C')
            print(f'Скорость ветра: {data["fact"]["wind_speed"]} м/с')
            print(f'Давление: {data["fact"]["pressure_mm"]} мм рт. ст.')
            print(f'Влажность: {data["fact"]["humidity"]} %')
            print(f'Погодное описание: {data["fact"]["condition"]}')
        else:
            # Выводим код ошибки
            print(f'Ошибка: {response.status_code}')




        #print(yandex_json)
        bot.send_message(message.chat.id, text=f'Температура воздуха: {data["fact"]["temp"]} °C')

bot.infinity_polling()

