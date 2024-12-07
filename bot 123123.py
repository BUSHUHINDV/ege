import telebot
from telebot import types
import requests
YandexAPI='461f3755-0a28-4825-a573-7c73b5e35e9a'
bot=telebot.TeleBot('6141219944:AAFxAKzaGoXwXBOnRCjZUmgNW1-ztOlv9Z0')
#bot=telebot.TeleBot('5826273791:AAFAjzu7JRfvyw4ogpBZqlHKNyRPP_NK9-4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать погоду")
    #btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1)
    bot.send_message(message.chat.id,
text="Привет, {0.first_name}! Я тестовый бот сообщающий погоду с Yandex".format(message.from_user),
                     reply_markup=markup)



@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Узнать погоду"):
        #https://yandex.ru/pogoda/uray?lat=60.124549&lon=64.815429
        lat=60.124549;  lon = 64.815429
        param={'lat':lat, 'lon':lon, 'lang':'ru_RU', 'limit':7,
               'hours': True, 'extra':False}
        url='https://api.weather.yandex.ru/v2/forecast'
        resp=requests.get(url,params=param,headers={'X-Yandex-API-Key':YandexAPI})
        #print(resp.json())
        # data=resp.json()
        #print(resp.text)
        # print_pogoda='Температура воздуха: '+str(data["fact"]["temp"])+\
        #       ' °C\n'+'Ощущается как:'+str( data["fact"]["feels_like"])+' °C\n'\
        #      +'Скорость ветра:' +str(data["fact"]["wind_speed"])+' м/с'
        # bot.send_message(message.chat.id, text=print_pogoda)
        if resp.status_code == 200:
            # Преобразуем ответ в JSON формат
            data = resp.json()
            # Выводим данные о текущей погоде
            bot.send_message(message.chat.id, text=f'Температура воздуха: {data["fact"]["temp"]} °C')
            bot.send_message(message.chat.id, text=f'Ощущается как: {data["fact"]["feels_like"]} °C')
            bot.send_message(message.chat.id, text=f'Скорость ветра: {data["fact"]["wind_speed"]} м/с')
            bot.send_message(message.chat.id, text=f'Давление: {data["fact"]["pressure_mm"]} мм рт. ст.')
            bot.send_message(message.chat.id, text=f'Влажность: {data["fact"]["humidity"]} %')
            bot.send_message(message.chat.id, text=f'Погодное описание: {data["fact"]["condition"]}')
            bot.send_message(message.chat.id, text=f'Восход солнца: {data["forecasts"]["parts"]["sunrise"]}')
        else:
            # Выводим код ошибки
            bot.send_message(message.chat.id, text=f'Ошибка: {resp.status_code}')

bot.infinity_polling()
