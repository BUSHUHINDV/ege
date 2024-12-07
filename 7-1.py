import random # from random import chouse
BodyParts = ["глаза", "ноги", "волосы", "уши", "руки", "губы", "щеки", "поступки",
             "мысли", "зубы", "ладони" ]
AnimalBodyParts = ["хвост", "мех", "голова", "запах", "смех", "рот", "воспоминания",
                   "улыбка", "нос"]
Adjectives = ["неординарные", "пропорциональные", "привлекательные", "изящные",
              "вдохновляющие"]
Animals = ["жирафа", "кота", "хомяка", "тигра", "слона", "зайца", "льва",
           "бегемота", "пингвина", "единорога"]
Plus = ["спящего", "космического" ,"убегающего", "кричащего", "дикого", "безумного"]
BodyPart = random.choice(BodyParts)
AnimalBodyPart = random.choice(AnimalBodyParts)
Adjective = random.choice(Adjectives)
Animal = random.choice(Animals)
Add = random.choice(Plus)
result = "Твои " + BodyPart + " более " + Adjective + " чем " +AnimalBodyPart +\
         " " +Add+ " " + Animal;
print(result)