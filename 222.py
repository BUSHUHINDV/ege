'''
(№ 3522) (Е. Джобс) Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) К этой записи справа дописывается 0, если число нечетное, и слева 1 в обратном случае.
3) Если единиц в двоичном числе получилось четное количество, справа дописывается 1, иначе 0.
Например, двоичная запись 1010 числа 10 будет преобразована в 110100.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью числа – результата работы данного алгоритма.
Укажите минимальное число N, для которого результат работы алгоритма будет больше 228.
В ответе это число запишите в десятичной системе счисления.
'''

#for i in range (100):
#    n=bin(i)[2:]
#    if i % 2 == 0:
#        n = '1' + n
#    elif i % 2 != 0:
#        n = n + '1'
#    if n.count('1') % 2 == 0:
#        n = n + '1'
#    else:
#        n = n + '0'
#    z = int(n, 2)
#    if z > 228:
#        print(i, z)
#'''
#(№ 3538) (Е. Джобс) Все 4-буквенные слова, составленные из букв П, Р, В, Д, А, записаны в алфавитном порядке и пронумерованы.
#Вот начало списка:
#1. АААА
#2. АААВ
#3. АААД
#4. АААП
#5. АААР
#6. ААВА
#Найдите номер первого слова в этом списке, которое не содержит гласных и одинаковых букв.
#'''
#
#k=0
#s=['А', 'В', 'Д', 'П', 'Р']
#for a in s:
#    for b in s:
#        for c in s:
#            for d in s:
#                k+=1
#                z=a+b+c+d
#                if not('А' in z) and z.count('А')<=1 and z.count('В')<=1 and z.count('Д')<=1 and z.count('П')<=1 and z.count('Р')<=1:
#                    print (z, k)
#
#'''
#	(№ 4164) (Е. Джобс) Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды,
#	 в обеих командах v и w обозначают цепочки символов.
#1. заменить (v, w)
#2. нашлось (v)
#Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, эта команда не изменяет
# строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
#Дана программа для исполнителя Редактор:
#ПОКА нашлось(42) или нашлось(32)
#   ЕСЛИ нашлось(42)
#      ТО заменить(42, 51)
#   ИНАЧЕ заменить(32, 61)
#КОНЕЦ ПОКА
#На вход программе подана строка, содержащая только 20 двоек, 15 троек и 10 четверок. Порядок символов заранее неизвестен.
#Определите максимально возможную сумму всех цифр в конечной строке.
#'''
#s='42'*10+'2'*10+'3'*15
#while '42' in s or '32' in s:
#    if '42' in s:
#        s=s.replace ('42', '51', 1)
#    else:
#        s=s.replace ('32', '61', 1)
#print (s)
#k=0
#for i in s:
#    k=k+int(i)
#print (k)
#'''
#(№ 4417) (П. Волгин) Значение выражения (6425 + 410) – (1620 + 323)
#записали в системе счисления с основанием 4. В каком разряде четверичной записи числа при просмотре
#справа налево впервые встречается цифра 2?'''
#s=(64**25+4**10)-(16**20+32**3)
#s1=''
#while s>0:
#    a=s%4
#    s=s//4
#    s1=str(a)+s1
#print (s1)
#k=0
#for i in s1:
#    k+=1
#    if i=='2':
#        print (k)
#
'''
#(№ 4174) (Е. Джобс) Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими соотношениями:
#F(0) = 1, F(1) = 3
#F(n) = F(n–1) – F(n–2) + 3n, при чётном n > 1
#F(n) = F(n–2) – F(n–3) + 2n, при нечётном n > 1
#Чему равно значение функции F(40)? В ответе запишите только целое число.'''
#def F(n):
#    if n==0:
#        return 1
#    if n==1:
#        return 3
#    if n>1 and n%2==0:
#        return F(n-1)-F(n-2)+3*n
#    if n>1 and n%2!=0:
#        return F(n - 2) - F(n - 3) + 2*n
#print(F(40))
#s=16**44*16**30-(32**5*(8**40-8**32))*(16**17-32**4)
#n=hex(s)
#print (n)
#n=n.replace('e','1')
#print(n)
#print (n.count ('1'))
#def F(n):
#    if n==0:
#        return 1
#    if n==1:
#        return 3
#    if n>1:
#        return F(n - 1) - F(n - 2) + 3*n
#print (F(40))

#print('a b c')
#for a in range(2):
#
#    for b in range(2):
#
#        for c in range(2):
#            if a==b or c==b:
#                print(a,b,c)
#

#k=0
#from itertools import product
#for i in product('КУСАТЬ',repeat=5):
#    s=''.join(i)
#
#    if s[0]!='Ь' and s.count('СУК')==0 and s.count('К')<=1 and s.count('У')<=1 and s.count('С')<=1 and s.count('А')<=1 and s.count('Т')<=1 and s.count('Ь')<=1:
#        k+=1
#        print(k,s)

#def f(n):
#    if n<2:
#        return 1
#    if n>=2 and n%2==0:
#        return f(n/2) + 1
#    if n>=2 and n%2!=0:
#        return f(n-3)+3
#for i in range(1000):
#    #print(f(i))
#    if f(i)==31:
#        print (i)
k=0
f=open('C:/Users/qwe/Downloads/17-9.txt','r')
p=[]
for n in f:
   p.append(int(n))
for i in len(p)-2:
   q=bin(p[i])[2:]
   w=bin(p[i+1])[2:]
   e=bin(p[i+2])[2:]
   if (q.count('1')>=3 and w.count('1')>=3) and (q.count('0')>=1 and w.count('0')>=1) or (q.count('1')>=3 and e.count('1')>=3) and (q.count('0')>=1 and e.count('0')>=1) or (w.count('1')>=3 and e.count('1'>=3) and (w.count('0')>=1 and e.count('0')>=1):
      k+=1

