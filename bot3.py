import vk_api
import time
import random
token = "21628b6fa788b63e83dac44d80218db7c5071e4acc020062697cf205921d71cbe31f24fb01360d2d47c83"
vk = vk_api.VkApi(token=token)

questions = ["Столица России?", 'Самое большое озеро в мире?', 'Самая популярный спорт в мире?'] 
answ = [['Египет', "Москва", "Лондон", "Париж"],
        ['Каспийское море', "Виктория", "Гурон", "Байкал"],
        ['Гольф', "Хоккей", "Футбол", "Бадминтон"]] 
right = [2, 1, 3]

money = 100 
i = 0

vk._auth_token()

while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"}) 
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"] 
        body = messages["items"][0]["last_message"]["text"] 
        if i == 0 or body == str(right[i-1]):
            if i != 0:
                money *= 2
                mess = 'Ваш выигрыш: ' + str(money)
                vk.method("messages.send", {"peer_id": id, "message": mess,
                            "random_id": random.randint(1, 2147483647)})
            if i == 3:
                vk.method("messages.send", {"peer_id": id,
                            "message": "Игра окончена!",
                            "random_id": random.randint(1, 2147483647)})
                break
            mess = questions[i]+'\n' + '1.'+answ[i][0]+'\n'+\
                                       '2.'+answ[i][1]+'\n'+\
                                       '3.'+answ[i][2]+'\n'+\
                                       '4.'+answ[i][3]+'\n'+\
                                       'Ответ пишется цифрой!'
            vk.method("messages.send", {"peer_id": id, "message": mess,
                                        "random_id": random.randint(1, 2147483647)})
            i += 1
        else:
            vk.method("messages.send",	{"peer_id": id, "message":"Вы проиграли!",
                                           "random_id": random.randint(1, 2147483647)})
            break 
    time.sleep(1)

