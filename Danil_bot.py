import random
import telebot
from telebot import types

bot = telebot.TeleBot('5826273791:AAFAjzu7JRfvyw4ogpBZqlHKNyRPP_NK9-4')
greetings = [
    'Привет', 'привет', 'Здравствуйте', 'здравствуйте', 'Добрый день',
    'добрый день', 'Добрый вечер', 'добрый вечер', 'прив'
]
actions = [
    "Вы просыпаетесь на окраине леса и не понимаете как здесь оказались.",
    "Вы видите старый дом, недалеко от вашего местоположения.",
    "Вы встречаете таинственного незнакомца, который предлагает вам помощь.",
    "Вы видите дым над холмом, на который вам предстоит подняться.",
    "Вы находите старый свиток с загадочной надписью.",
    "Вы слышите звуки стуков, доносящиеся из заброшенной шахты.",
    "Вы находите старое платье, которое кажется вам знакомым.",
    "Вы встречаете семью гномов, которые рассказывают вам свою историю.",
    "Вы находите меч, украденный из королевского замка.",
    "Вы слышите тихий голос, напутствующий вас к ближайшему городу."
]
privet = [
    "Здорова",
    "Салам",
    "Здравия желаю",
    "Приветик",
    "Приветствую", ]

global score
score = 0

answer_pool = ['Камень', 'Ножницы', 'Бумага']

danger = ["🐍", "🐊", "🐉", "👻"]


@bot.message_handler(commands=['start'])
def echo_all(message):
    bot.reply_to(
        message,
        random.choice(privet) +
        ", Пользователь! Я бот, который поможет тебе сделать самые простые задачи. Чтобы начать, введи '/help'"
    )


@bot.message_handler(commands=['dice'])
def dice_reply(message):
    markup = types.InlineKeyboardMarkup()
    itembtn5 = types.InlineKeyboardButton(text='Бросить', callback_data='Бросить')
    markup.row(itembtn5)
    i = ["1", "2", "3", "4", "5", "6"]
    dice_choice = random.choice(i)
    bot.send_message(message.chat.id, "Выпало:", reply_markup=markup)
    bot.send_message(message.chat.id, text=dice_choice)


@bot.message_handler(commands=['help'])
def help_reply(message):
    bot.send_message(message.chat.id, text="Напиши /game - начать игру камень, ножницы, бумага")
    bot.send_message(message.chat.id, text="Напиши /dice - бросить кубик")
    bot.send_message(message.chat.id, text="Напиши /help - посмотрет возожные команды")
    bot.send_message(message.chat.id, text="Напиши /quest - начать текстовый квест")
    bot.send_message(message.chat.id, text="Напиши /doors - начать игру двери")


@bot.message_handler(commands=['quest'])
def start_quest(message):
    na4alo = random.choice(actions)
    actions.remove(na4alo)
    markup = types.InlineKeyboardMarkup()
    if na4alo == "Вы просыпаетесь на окраине леса и не понимаете как здесь оказались.":
        itembtn1 = types.InlineKeyboardButton(
            text='Преодолевать желание зайти в лес и попытаться обойти его',
            callback_data='1')
        itembtn2 = types.InlineKeyboardButton(text='Пойти в глубь леса',
                                              callback_data='2')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы видите старый дом, недалеко от вашего местоположения.":
        itembtn1 = types.InlineKeyboardButton(text='Пойти в него',
                                              callback_data='3')
        itembtn2 = types.InlineKeyboardButton(text='Пройти мимо',
                                              callback_data='4')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы встречаете таинственного незнакомца, который предлагает вам помощь.":
        itembtn1 = types.InlineKeyboardButton(text='Принять помощь',
                                              callback_data='5')
        itembtn2 = types.InlineKeyboardButton(text='Отказаться', callback_data='6')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы видите дым над холмом, на который вам предстоит подняться.":
        itembtn1 = types.InlineKeyboardButton(text='Подняться', callback_data='7')
        itembtn2 = types.InlineKeyboardButton(text='Пройти мимо',
                                              callback_data='8')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы находите старый свиток с загадочной надписью.":
        itembtn1 = types.InlineKeyboardButton(text='Прочитать надпись',
                                              callback_data='9')
        itembtn2 = types.InlineKeyboardButton(text='Пройти мимо',
                                              callback_data='10')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы слышите звуки стуков, доносящиеся из заброшенной шахты.":
        itembtn1 = types.InlineKeyboardButton(text='Пойти в шахту',
                                              callback_data='11')
        itembtn2 = types.InlineKeyboardButton(text='Пройти мимо',
                                              callback_data='12')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы находите старое платье, которое кажется вам знакомым.":
        itembtn1 = types.InlineKeyboardButton(text='Взять с собой',
                                              callback_data='13')
        itembtn2 = types.InlineKeyboardButton(text='Оглянуться',
                                              callback_data='14')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы встречаете семью гномов, которые рассказывают вам свою историю.":
        itembtn1 = types.InlineKeyboardButton(text='Внимательно послушать',
                                              callback_data='15')
        itembtn2 = types.InlineKeyboardButton(text='Уйти', callback_data='16')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы находите меч, украденный из королевского замка.":
        itembtn1 = types.InlineKeyboardButton(text='Взять с собой',
                                              callback_data='17')
        itembtn2 = types.InlineKeyboardButton(text='Оглянуться',
                                              callback_data='18')
        markup.add(itembtn1, itembtn2)
    elif na4alo == "Вы слышите тихий голос, напутствующий вас к ближайшему городу.":
        itembtn1 = types.InlineKeyboardButton(text='Пойти к городу',
                                              callback_data='19')
        itembtn2 = types.InlineKeyboardButton(text='Убежать', callback_data='20')
        markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, na4alo, reply_markup=markup)


@bot.message_handler(commands=['game'])
def game_reply(message):
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton(text='Камень', callback_data='Камень')
    itembtn2 = types.InlineKeyboardButton(text='Ножницы', callback_data='Ножницы')
    itembtn3 = types.InlineKeyboardButton(text='Бумага', callback_data='Бумага')
    markup.row(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)


@bot.message_handler(commands=['doors'])
def doors_reply(message):
    bot.send_message(message.chat.id,
                     "Вы попали в замок из которого вам необходимо выбраться. Чтобы выбраться нужно пройти через лабиринт дверей.")
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton(text='🚪', callback_data='d1')
    itembtn2 = types.InlineKeyboardButton(text='🚪', callback_data='d2')
    itembtn3 = types.InlineKeyboardButton(text='🚪', callback_data='d3')
    markup.row(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Выберите дверь, чтобы пройти дальше:", reply_markup=markup)


@bot.callback_query_handler(func=lambda _: True)
def answering(call, score):
    if call.data == 'ЗановоКНБ':
        game_reply(call.message)
        return
    elif call.data == "Бросить":
        dice_reply(call.message)
        return
    elif call.data == "1":
        bot.send_message(
            call.message.chat.id,
            'Вы преодолеваете желание зайти в лес и попытаетесь обойти его. Но ваше действие приводит к смерти.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "2":
        bot.send_message(call.message.chat.id,
                         'Вы пытаетесь пройти в глубь леса, но ...')
        start_quest(call.message)
        return
    elif call.data == "3":
        bot.send_message(
            call.message.chat.id,
            'Вы пытаетесь пройти в дом, но вас настигает хозяин и он вас убивает.')
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "4":
        bot.send_message(
            call.message.chat.id,
            'Вы пройдете мимо дома. Вас замечает хозяин дома и гонится за вами. Вы начинаете убегать, но ...'
        )
        start_quest(call.message)
        return
    elif call.data == "5":
        bot.send_message(
            call.message.chat.id,
            'Вы приняли помощь от незнакомца. Он оказался наемным убийцей который охотился за вами.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "6":
        bot.send_message(
            call.message.chat.id,
            'Вы отказались от помощи незнакомца. Он оказался наемным убийцей который охотился за вами. Вам удалось скрыться от него, но ...'
        )
        start_quest(call.message)
        return
    elif call.data == "7":
        bot.send_message(
            call.message.chat.id,
            'Вы поднимаетеся над холм. Вы находите старый каменный ключ. За вами обЪявлена охота. Ночью вас настигают и вы погибаете.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "8":
        bot.send_message(
            call.message.chat.id,
            'Вы пройдете мимо холма. Вы находите старый каменный ключ.')
        start_quest(call.message)
        return
    elif call.data == "9":
        bot.send_message(
            call.message.chat.id,
            'Вы прочитали надпись. В ней написано: "Чтобы выбраться из леса, нужно пройти через дом и дойти до замка."'
        )
        start_quest(call.message)
        return
    elif call.data == "10":
        bot.send_message(call.message.chat.id, 'Вы проходите мимо старого свитка.')
        start_quest(call.message)
        return
    elif call.data == "11":
        bot.send_message(call.message.chat.id,
                         'Вы пытаетесь пройти в шахту, но ...')
        start_quest(call.message)
        return
    elif call.data == "12":
        bot.send_message(
            call.message.chat.id,
            'Вы проходите мимо шахты. Вас поджидают за углом гномы. Вы начинаете убегать, но они были быстрее вас'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "13":
        bot.send_message(
            call.message.chat.id,
            'Вы взяли с собой старое платье. Вы вспоминаете что это платье вашей мамы. Вы прибываете в своих воспоминаниях. Вы вспоминаете о том что ваша мать умерла. Вы не можете смириться с этим и умираете.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "14":
        bot.send_message(
            call.message.chat.id,
            'Вы оглянулись в старое платье, оно кажется вам очень знакомым, но вы не помните откуда вы его помните. На свякий случай вы берете его с собой.'
        )
        start_quest(call.message)
        return
    elif call.data == "15":
        bot.send_message(
            call.message.chat.id,
            'Вы внимательно послушали гномов. Они сказали что они живут в лесу и что в нем есть много доброго. Вы идете с ними в лес. Они заставляют вас жениться на их дочери, но вы отказываетесь и они зажаривают вас заживо.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "16":
        bot.send_message(
            call.message.chat.id,
            'Вы уходите из леса. Вы видите старый замок. Вы вспоминаете что у вас есть ключ. Вы открываете замок и видите таинственный сундук. Вы открываете его и видите надпись: "Вы выиграли!"'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "17":
        bot.send_message(
            call.message.chat.id,
            'Вы взяли с собой меч. Вы вспоминаете что это меч вашего отца. Вы вспоминаете что ваш отец умер  и вы должны отомстить за него. Вы идете на дуэль с убийцей. К сожалению, вы не смогли отомстить за него и он убил вас.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "18":
        bot.send_message(
            call.message.chat.id,
            'Вы оглянулись в меч. Вы вспоминаете что это меч вашего отца. Вы вспоминаете что ваш отец умер  и вы должны отомстить за него. Вы идете на дуэль с убийцей. Вам получилось отомстить за него.'
        )
        start_quest(call.message)
        return
    elif call.data == "19":
        bot.send_message(
            call.message.chat.id,
            'Вы пытаетесь пойти к городу. Голос начинает произносить напонятные слова все быстрее и быстрее. Вы начинаете убегать, но вы падаете на землю и погибаете. Оказалось что то было заклинание ведьмы от которого вам не удалось спастись.'
        )
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "20":
        bot.send_message(call.message.chat.id, 'Вы убегаете.')
        start_quest(call.message)
        return
    elif len(actions) == 0:
        bot.send_message(call.message.chat.id, 'Вы уже прошли все события.')
        bot.send_message(call.message.chat.id, 'Игра окончена.')
    elif call.data == "d1" or call.data == "d2" or call.data == "d3":
        ghost = random.randint(1, 3)
        if ghost == 1 and call.data == "d1" or ghost == 2 and call.data == "d2" or ghost == 3 and call.data == "d3":
            dang = random.randint(0, 3)
            if dang == 0:
                bot.send_message(call.message.chat.id,
                                 'Вы заходите в комнату и падаете в яму со змеями. Вы погибаете.' + danger[0])
            elif dang == 1:
                bot.send_message(call.message.chat.id,
                                 'Вы заходите в комнату где вас поджидают крокодилы. Вы погибаете.' + danger[1])
            elif dang == 2:
                bot.send_message(call.message.chat.id,
                                 'Вы заходите в комнату, где не замечаете дракона. Вы погибаете.' + danger[2])
            elif dang == 3:
                bot.send_message(call.message.chat.id,
                                 'Вы открываете дверь и на вас нападает призрак. Вы погибаете.' + danger[3])
            bot.send_message(call.message.chat.id, 'Игра окончена. Ваш результат: ' + str(score))
            markup = types.InlineKeyboardMarkup()
            itembtn = types.InlineKeyboardButton(text='Заново', callback_data='ЗановоД')
            markup.row(itembtn)
            bot.send_message(call.message.chat.id, "", reply_markup=markup)
        else:
            score = score + 1
            bot.send_message(call.message.chat.id, 'Вы выбрали правильную дверь. Вы проходите дальше.')
            doors_reply(call.message)
            return
    elif call.data == "ЗановоД":
        doors_reply(call.message)
        return
    else:
        bot_anwser = answer_pool[random.randint(0, 2)]
        bot.send_message(call.message.chat.id, bot_anwser)
        result = answer_pool.index(call.data) - answer_pool.index(bot_anwser)
        if result == -1 or result == 2:
            bot.send_message(call.message.chat.id, "Ты выиграл!")
        elif result == 0:
            bot.send_message(call.message.chat.id, "Ничья!")
        else:
            bot.send_message(call.message.chat.id, "Я выиграл!")
        markup = types.InlineKeyboardMarkup()
        itembtn4 = types.InlineKeyboardButton(text='Заново', callback_data='ЗановоКНБ')
        markup.row(itembtn4)
        bot.send_message(call.message.chat.id, "Выбери действие:", reply_markup=markup)


bot.infinity_polling()