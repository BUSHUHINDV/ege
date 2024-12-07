import telebot
#pip install requests
import requests
from telebot import types
from bs4 import BeautifulSoup as bs



url='https://yandex.ru/pogoda/uray'

bot=telebot.TeleBot('5826273791:AAFAjzu7JRfvyw4ogpBZqlHKNyRPP_NK9-4')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать погоду")
    #btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1)
    #bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Узнать погоду"):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'}

        #page = requests.get(url).content
        res=requests.get(url,headers)
        #res = requests.get(url)
        print(res.text)
        #print(page)
        #soup = bs(page, 'lxml')
        #soup = bs(page, 'html.parser')
        #soup = bs(res, 'lxml')

        # current_weather = soup.find('div', {'class': 'current-weather'})
        # current_weather_temperature = current_weather.find('div', {
        #     'class': 'current-weather__thermometer current-weather__thermometer_type_now'})
        # current_weather_description = current_weather.find('span', {'class': 'current-weather__comment'})
        # weather='Сейчас\n\t{}, {}\n'.format(current_weather_temperature.text, current_weather_description.text)
        bot.send_message(message.chat.id, text=res)

bot.infinity_polling()