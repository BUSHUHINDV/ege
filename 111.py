'''for i in range(100):
    print(i, "Hello World!")

s='Hello World \n'*100
print(s)
'''
'''
r_password='PaSSword'
login=False
while login==False:
    passs=input("Введите пароль: ")
    if passs==r_password:
        print("Пароль верен \n Вы вошли")
        login = True
    else:
        print("Пароль неверный")
        '''
'''Напишите программу, которая ищет среди целых чисел, принадлежащих
числовому отрезку [6080068; 6080176], простые числа. Выведите все найденные простые
числа в порядке возрастания, слева от каждого числа выведите его номер по порядку.'''
def prost(n):
    k=0
    for j in range(2,n//2+1):
        if n % j==0:
            k+=1
    if k==0:
        return True
    else:
        return False
nomer=0
for i in range(6080068, 6080177):
    nomer+=1
    if prost(i):
        print(nomer, '-', i)

