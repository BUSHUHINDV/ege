##ДЕЛ(45, A) ∧ ((ДЕЛ(x, 30) ∧ ДЕЛ(x, 12)) → ДЕЛ(x, A))
#def D(x,A):
#    if x%A==0:
#        return True
#    else:
#        return False
#list1=[1,3,5,15,45]
#for A in range(1,100):
#    p=0
#    for x in range(100):
#        if not(D(45,A) and ((D(x,30) and D(x,12))<=D(x,A))):
#            p = 1
#            break
#    if p == 0:
#       print(A)
#

#
# f=open('C:/Users/qwe/Downloads/27-98a.txt')
# l=[]
# sl=[]
# n=f.readline()
# a = [int(x) for x in n.split()]
# n1=a[1]
# for i in f:
#     l.append(int(i))
# print(l)
# for i in range(len(l)-n1):
#     sl=[]
#     for j in range(i,i+a[1]):
#         sl.append(l[j])
#     sl.sort()
#
#     print(sl)

'''Задание 15 .
(И.Карпачев) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n  делится
без остатка на натуральное число m», а через БИТЧЁТ(n) утверждение «натуральное
число n имеет чётное количество единиц в двоичной записи».
Пусть на числовой прямой дан отрезок B = [100; 190]
Найдите наибольшее значение х, для которого выражение
БИТЧЁТ(x) ⋀ (x ∈ B) ⋀ ДЕЛ(x, 8)
тождественно истинно (т. е. принимает значение 1)?'''

def ДЕЛ(a, b):
   if a%b==0:
       return True
   else:
       return False
def БИТЧЁТ(x):
    s=bin(x)[2:]
    if s.count('1')%2==0:
        return True
    else:
        return False

for x in range(1000):
    if (БИТЧЁТ(x) and (x>=100 and x<=190) and ДЕЛ(x, 8)):
        print(x)
#print(bin(20)[:2])
