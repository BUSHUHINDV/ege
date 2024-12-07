'''№ 3084) (А. Кабанов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может
  а) добавить в кучу один камень;
  б) увеличить количество камней в куче в два раза;
  в) увеличить количество камней в куче в три раза.
Игра завершается в тот момент, когда количество камней в куче становится не менее 43. Если при этом в куче оказалось не более 72 камней, то победителем считается игрок, сделавший последний ход. В противном случае победителем становится его противник. В начальный момент в куче было S камней, 1 ≤ S ≤ 42.
Ответьте на следующие вопросы:
  Вопрос 1. Найдите минимальное значение S, при котором Ваня выигрывает своим первым ходом при любой игре Пети.
  Вопрос 2. Сколько существует значений S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
  Вопрос 3. Найдите минимальное и максимальное значения S, при которых одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
Найденные значения запишите в ответе в порядке возрастания.
Спрятать ответ'''

# print('задание 19')
# def game(s,n):
#     if s>=43 or n>2:
#         return n==2 and s<=72 or n==1 and s>72
#     if n%2==0:
#         return game(s+1,n+1) and game(s*2,n+1) and game(s*3,n+1)
#     else:
#         return game(s + 1, n + 1) or game(s * 2, n + 1) or game(s * 3, n + 1)
# for i in range(43):
#     if game(i,0):
#         print(i)
#         #break
#
# print('задание 20')
# def game(s,n):
#     if s>=43 or n>3:
#         return n==3 and s<=72 or n==2 and s>72
#     if n%2!=0:
#         return game(s+1,n+1) and game(s*2,n+1) and game(s*3,n+1)
#     else:
#         return game(s + 1, n + 1) or game(s * 2, n + 1) or game(s * 3, n + 1)
# for i in range(43):
#     if game(i,0):
#         print(i)
#
# print('задание 21')
# def game(s,n):
#     if s>=43 or n>4:
#         return n==4 and s<=72 or n==3 and s>72 or n==2 and s<=72 or n==1 and s>72
#     if n%2==0:
#         return game(s+1,n+1) and game(s*2,n+1) and game(s*3,n+1)
#     else:
#         return game(s + 1, n + 1) or game(s * 2, n + 1) or game(s * 3, n + 1)
# for i in range(43):
#     if game(i,0):
#         print(i)
# print('задание 19')
# def g(s,k,n):
#     if s+k>=259 or n>2:
#         return n==2
#     if n%2==0:
#         return g(s+1,k,n+1) or g(s*2,k,n+1) or g(s,k+1,n+1) or g(s,k*2,n+1)
#     return g(s+1,k,n+1) or g(s*2,k,n+1) or g(s,k+1,n+1) or g(s,k*2,n+1)
# for i in range(242):
#     if g(17,i,0):
#         print(i)
#         break
# print('задание 20')
# def g(s,k,n):
#     if s+k>=259 or n>3:
#         return n==3
#     if n%2!=0:
#         return g(s+1,k,n+1) and g(s*2,k,n+1) and g(s,k+1,n+1) and g(s,k*2,n+1)
#     return g(s+1,k,n+1) or g(s*2,k,n+1) or g(s,k+1,n+1) or g(s,k*2,n+1)
# for i in range(242):
#     if g(17,i,0):
#         print(i)
#
# print('задание 21')
# def g(s,k,n):
#     if s+k>=259 or n>4:
#         return n==2 or n==4
#     if n%2==0:
#         return g(s+1,k,n+1) and g(s*2,k,n+1) and g(s,k+1,n+1) and g(s,k*2,n+1)
#     return g(s+1,k,n+1) or g(s*2,k,n+1) or g(s,k+1,n+1) or g(s,k*2,n+1)
# for i in range(242):
#     if g(17,i,0):
#         print(i)
from math import *

# print('задание 19')
# def f(s,n):
#     if s>=129 or n>2:
#         return n==2
#     if n%2==0:
#         return f(s+1,n+1) and f(s*2,n+1)
#     else:
#         return f(s+1,n+1) or f(s*2,n+1)
#
# for i in range(1,129):
#     if f(i,0):
#         print(i)
#
# print('задание 20')
# def f(s,n):
#     if s>=129 or n>3:
#         return n==3
#     if n%2!=0:
#         return f(s+1,n+1) and f(s*2,n+1)
#     else:
#         return f(s+1,n+1) or f(s*2,n+1)
#
# for i in range(1,129):
#     if f(i,0):
#         print(i)
# print('задание 21')
# def f(s,n):
#     if s>=129 or n>4:
#         return n==4 or n==2
#     if n%2==0:
#         return f(s+1,n+1) and f(s*2,n+1)
#     else:
#         return f(s+1,n+1) or f(s*2,n+1)
#
# for i in range(1,129):
#     if f(i,0):
#         print(i)

print('задание 19')
def f(s,n):
    if s<=19 or n>2:
        return n==2
    if n%2==0:
        return f(s-2,n+1) and f(s-5,n+1) and f(floor(s/3),n+1)
    else: #all([f(s-2,n+1) , f(s-5,n+1) , f(floor(s/3),n+1)])
        return f(s-2,n+1) or f(s-5,n+1) or f(floor(s/3),n+1)
        ##any([f(s-2,n+1) , f(s-5,n+1) , f(floor(s/3),n+1)])
for i in range(1,500):
    if f(i,0):
        print(i)

print('задание 20')
def f(s,n):
    if s<=19 or n>3:
        return n==3
    if n%2!=0:
        return f(s-2,n+1) and f(s-5,n+1) and f(floor(s/3),n+1)
    else: #all([f(s-2,n+1) , f(s-5,n+1) , f(floor(s/3),n+1)])
        return f(s-2,n+1) or f(s-5,n+1) or f(floor(s/3),n+1)
        ##any([f(s-2,n+1) , f(s-5,n+1) , f(floor(s/3),n+1)])
for i in range(1,500):
    if f(i,0):
        print(i)

print('задание 20')
def f(s,n):
    if s<=19 or n>4:
        return n==4 or n==2
    if n%2==0:
        return f(s-2,n+1) and f(s-5,n+1) and f(floor(s/3),n+1)
    else: #all([f(s-2,n+1) , f(s-5,n+1) , f(floor(s/3),n+1)])
        return f(s-2,n+1) or f(s-5,n+1) or f(floor(s/3),n+1)
        ##any([f(s-2,n+1) , f(s-5,n+1) , f(floor(s/3),n+1)])
for i in range(1,500):
    if f(i,0):
        print(i)