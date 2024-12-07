# f=open('C:/Users/qwe/Downloads/17-5.txt')
# e=[]
# t=0
# smm=0
# sm=0
#
# for i in f:
#    e.append(int(i))
# print (e)
# for k in range (len(e)-1):
#    a=e[k]
#    b=e[k+1]
#    if abs(a)%10==7 or abs(b)%10==7:
#        t+=1
#        sm=a+b
#        smm=max(sm, smm)
# print (t, smm)
# print(-7%10)

# for m in range(2,50,2):
#     for n in range(1,50,2):
#         N = 2 ** m * 3 ** n
#         if 150000000<N< 300000000:
#             print('N==',N,' m==',m,' n==',n, ' m+n=' ,m+n)
'''
Задание 17 № 37340В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает
10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, разность которых четна и
хотя бы одно из чисел делится на 31, затем максимальную из сумм элементов таких пар. В данной задаче под парой
подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
17.txt
'''
'''
f=open('C:/Users/qwe/Downloads/17 (1).txt')
e=[]
for i in f:
    e.append(int(i))
print (e)
s=0;sm=0;k=0
for i in range(len(e)-1):
    for j in range(i+1,len(e)):
        if (e[i]%31==0 or e[j]%31==0) and (abs(e[i]-e[j])%2==0):
            k+=1
            s=e[i]+e[j]
            sm=max(sm,s)
print(k,sm)
'''
'''
Нужно налить бассейн водой. Размеры бассейна: a, b, c м.

Скорость, с которой наливается в него вода d м3/час.
Определите, через сколько часов бассейн, наконец, заполнится.
Выведите число, округлять не нужно.
Пример 1
Ввод	Вывод
1
2
3
0.5
12.0''''''
a = int(input())
b = int(input())
c = int(input())
d = float(input())
print((a * b * c) / d)
'''
'''
Напишите программу, которая производит такие вычисления:

вводится число;
к нему надо прибавить следующее;
полученную сумму умножить на следующее число;
шаги 2 – 3 повторить три раза.
При исходном числе 1 получится такой результат:
1 + 2 = 3
3 ⋅ 3 = 9
9 + 4 = 13
13 ⋅ 5 = 65
65 + 6 = 71
71 ⋅ 7 = 497
497 + 8 = 505
505 ⋅ 9 = 4545
'''
'''
# 1
a = int(input())
s = 0
next = a;
# 2
next += 1;
s = a + next
# print()
# 3
next += 1;
s *= next
# 2

next += 1;
s += next
# 3
next += 1;
s *= next
# 2

next += 1;
s += next
# 3
next += 1;
s *= next
# 2

next += 1;
s += next
# 3
next += 1;
s *= next

print(s)
'''
'''
Удава можно измерять в попугаях. Для этого даже не нужно их глотать.
Измерьте длину строки в попугаях.
Напишите программу, которая определяет, сколько раз слово parrot укладывается в во введенной строке.
Пример
Ввод	Вывод
38 попугаев и еще одно попугайское крылышко
7
'''
#a = input()
#print(a.count(' ')+1-a.count(' - ')*2)
'''
f=open('C:/Users/qwe/Downloads/17-7.txt')
l=[]
k=0
m=0
m1=0
for i in f:
    l.append(int(i))
for i in range(len(l)-2):

    if (str(hex(l[i])[2:][-1])=='0' and str(hex(l[i+1])[2:][-1])=='0') or (str(hex(l[i+1])[2:][-1])=='0' and str(hex(l[i+2])[2:][-1])=='0') or (str(hex(l[i+2])[2:][-1])=='0' and str(hex(l[i])[2:][-1])=='0'):
        k += 1
        m=max(l[i],l[i+1],l[i+2])
        m1+=m
        print(k,m1)
'''
#print ('x y z w')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                if not((y<= (x or z))and(z<=y)):
#                    print (x, y, z, w, (y<= (x or z))and(z<=y))
#
print('X Y Z W F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(not(y<=w) or (x==z)or x):
                    print(x,y,z,w, not(y<=w) or (x==z)or x)