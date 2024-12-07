#f=open ('C:/Users/qwe/Downloads/17-7 (1).txt')
#e=[]
#for i in f:
#    e.append(int(i))
#print(e)
#k=0
#for r in e:
#    o=oct(r)[2:]
#    if o[-1]=='7':
#        if len(o)>=2:
#            if o[-2] != '2':
#                k+=1
#                print(r, k)
#        else:
#            k+=1
#            print(r, k)
#for i in range (10000):
#    x = i
#    m = 0
#    s = 0
#    while x > 0:
#      d = x % 6
#      s += d
#      if d > m: m = d
#      x = x // 6
#    if m==5 and s==16:
#        print(i,m,s)
'''
(№ 4356) (П. Волгин) В файле 17-7.txt содержится последовательность целых чисел.
Элементы последовательности могут принимать значения от 0 до 200 включительно.
Определите сначала количество троек элементов последовательности, в которых хотя бы одно число
в троичной системе счисления в нулевом разряде имеет 2, а затем сумму минимальных чисел из таких троек.
Под тройкой подразумевается три идущих подряд элемента последовательности.
'''
k=0
y=0
f=open('C:/Users/qwe/Downloads/17-7 (2).txt')
e=[]
for i in f:
    e.append(int(i))
print (e)
print(len(e))

for t in range (len(e)-2):
    a=e[t]
    b=e[t+1]
    c=e[t+2]

    s1 = ''
    s2 = ''
    s3 = ''
    while a>0:
        z=a%3
        a=a//3
        s1=str(z)+s1
    while b>0:
        z=b%3
        b=b//3
        s2=str(z)+s2
    while c>0:
        z=c%3
        c=c//3
        s3=str(z)+s3
    if s1[-1]=='2' or s2[-1]=='2' or s3[-1]=='2':
        k+=1
        y += min(e[t], e[t+1], e[t+2])
print (k)
    #y+=min(a, b, c)
print (y)
