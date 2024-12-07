#for i in range(1,101):
#    print(i,"Hello world!",end=", ")
'''
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
print('Выберите операцию: \n 1 - "+", 2 - "-", 3 - "*", 4 - "/"')
operation=input()
if operation=='1':
    print(a,'+',b,'=',a+b)
elif operation=='2':
    print(a,'-',b,'=',a-b)
elif operation=='3':
    print(a,'*',b,'=',a*b)
elif operation == '4':
    if b!=0:
        print(a, '/', b, '=', a / b)
    else:
        print("На ноль делить нельзя!")
else:
    print('неверный ввод')
'''
# n=int(input())
# minxx=30000
# for i in range(n):
#     a=int(input())
#     if a%3==0:
#         if a<minxx:
#             minxx=a
# print(minxx)
import random
import telebot
from telebot import types


bot=telebot.TeleBot('6141219944:AAFxAKzaGoXwXBOnRCjZUmgNW1-ztOlv9Z0')
greetings = ["Привет", "Здравствуй", "Добрый день"]
privet=["Здоров1", 'здоров2']
priv=random.choice(privet)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text in greetings:
#         bot.reply_to(message, priv)

@bot.message_handler(commands=['game'])
def game_reply(message):
  markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
  itembtn1 = types.KeyboardButton('1')
  itembtn2 = types.KeyboardButton('2')
  itembtn3 = types.KeyboardButton('3')
  markup.row(itembtn1, itembtn2, itembtn3)
  bot.send_message(message.chat.id, "Выбери ответ:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text in greetings:
        bot.reply_to(message, priv)
bot.infinity_polling()



