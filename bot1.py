#Если при выполнении команды в Windows PowerShell
# у вас возникла ошибка с таким текстом, это значит что в
# вашей системе закрыт доступ к выполнению сценариев PowerShell
# политикой безопасности. Чтобы открыть доступ необходимо выполнить
# следующую команду: Set-ExecutionPolicy Unrestricted -Scope CurrentUser
#pip install pyTelegramBotAPI
import telebot
from telebot import types
import random
#В меню PyCharm выбрать File -> Settings… во вкладке Python Interpreter,
bot=telebot.TeleBot('6141219944:AAFxAKzaGoXwXBOnRCjZUmgNW1-ztOlv9Z0')
greetings = ["Привет", "Здравствуй", "Добрый день"]
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if(message.text in greetings):
#         bot.reply_to(message, "Здравствуй человек")
# bot.infinity_polling()

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#             bot.reply_to(message, message.text)






# answer_pool = ["Камень", "Ножницы", "Бумага"]
#
# @bot.message_handler(commands=['game'])
# def game_reply(message):
#   markup = types.InlineKeyboardMarkup()
#   itembtn1 = types.InlineKeyboardButton(text='Камень', callback_data='Камень')
#   itembtn2 = types.InlineKeyboardButton(text='Ножницы', callback_data='Ножницы')
#   itembtn3 = types.InlineKeyboardButton(text='Бумага', callback_data='Бумага')
#   itembtn4 = types.InlineKeyboardButton(text='Заново', callback_data='Заново')
#   markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
#   bot.send_message(message.chat.id, "Выбери ответ:", reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def answering(call):
#   if call.data == "Заново":
#     game_reply(call.message)
#     return
#   bot_answer = answer_pool[random.randint(0,2)]
#   bot.send_message(call.message.chat.id, bot_answer)
#   result = answer_pool.index(call.data) - answer_pool.index(bot_answer)
#   if result == -1 or result == 2:
#     bot.send_message(call.message.chat.id, "Ты выиграл")
#   elif result == 0:
#     bot.send_message(call.message.chat.id, "Ничья")
#   else:
#     bot.send_message(call.message.chat.id, "Я выиграл")

bot.infinity_polling()
