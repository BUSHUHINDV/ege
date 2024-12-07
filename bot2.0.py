import vk_api #pip install vk_api
import time
import random

#token= "369fdf9a93b447b6057d35cc73b9af27c71bfca3291c9dd302734585e77ae6867e47c6cb8be02dbdc421a"
token= "b8bb4a73c54d84a3d10df07dc5ab23f3cd406b21c11b485b36d24f1cc15ab9b805eef612146698f6c1d82"
vk = vk_api.VkApi(token=token)

value = {
    "offset" : 0,
    "count" : 20,
    "filter" : "unanswered"
    }
while True:
    messages = vk.method("messages.getConversations",value)
    print(messages)
    if messages ["count"] >= 1:
        user_id = messages["items"][0]["last_message"]["from_id"]
        text = messages["items"][0]["last_message"]["text"]
        if text.lower() == "привет":
            vk.method("messages.send", {"peer_id": user_id, "message": "Привет!)", "random_id": random.randint(1, 2147483647)})
        elif text.lower() == "kiberone":
            vk.method("messages.send", {"peer_id": user_id, "message": "вперед за киберонами!", "random_id": random.randint(1, 2147483647)})
        else:
            vk.method ("messages.send", {"peer_id": user_id, "message": "Я не понял(!","random_id": random.randint(1, 2147483647)})
    time.sleep(1)