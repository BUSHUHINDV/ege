    # x='1'*200
# while x.count('111')>0 or x.count('222'):
#     x= x.replace('111','22',1)
#     x= x.replace('222','1',1)
# print(x)

'''Задание 12 .
(И.Карпачев) Дана программа для Редактора:
НАЧАЛО
ПОКА нашлось (27) ИЛИ нашлось (377) ИЛИ нашлось (777)
 ЕСЛИ нашлось (27)
 ТО заменить (27, 7)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (377)
 ТО заменить (377, 72)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (777)
 ТО заменить (777, 3)
 КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой выше программе поступает строка, начинающаяся с четырех
цифр «3», а затем содержащая n цифр «7».
Определите наибольшее двузначное значение n, при котором в строке, получившейся в
результате выполнения программы, останутся только цифры «7».
'''
for n in range(10,100):
    x='3333'+'7'*n
    while ('27' in x) or ('377' in x) or ('777' in x) :
        if ('27' in x):
            x= x.replace('27','7',1)
        if ('377' in x):
            x = x.replace('377', '72', 1)
        if ('777' in x):
            x = x.replace('777', '3', 1)
    if x.count('3')==0 and x.count('2')==0:
        print(n)
    #print(x, n)