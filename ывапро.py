#print('x y z w f')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                if ((x==(not y))<=((z<=(not w))and(w<=y)))==1:
#                    print(x,y,z,w,((x==(not y))<=((z<=(not w))and(w<=y))))
#def f(n):
#    if n==10:
#        return 1
#    elif n<10:
#        return f(n+1)+f(n*2)
#    else:
#        return 0
#print(f(1))
#def g(n):
#    if n==35:
#        return 1
#    if n==17 or n>35 :
#        return 0
#    else:
#        return g(n + 1) + g(n * 2)
#print(f(1)*g(10))
#def f(n,sl,um):
#    if n==472 and um>sl:
#        return 1
#    if n>472:
#        return 0
#    else:
#        return f(n+3,sl+1,um)+f(n*2,sl,um+1)+f(n*7,sl,um+1)
#print(f(2,0,0))
#f=open('C:/Users/qwe/Desktop/Вероника/inf_11_2023/Доп.файлы/Задание 24/24.txt')
#s=f.readline()
#print(len(s))
#q=['F','D','C']
#w=['A','O']
#maxl=k=i=0
#while i<(len(s)-1):
#    if s[i] in q and s[i+1] in w:
#        k+=1
#        i+=2
#    else:
#        maxl=max(maxl,k)
#        k=0
#        i+=1
#print(maxl)
# def g(a,b,n):
#     if ((a+b)>62 and (a+b)<75) or n>3:
#         return n==3
#     if a+b>74 or n>3 :
#         return n==2
#     if n%2!=0:
#         return g(a+2,b,n+1) and g(a*2,b,n+1) and g(a,b+2,n+1) and g(a,b*2,n+1)
#     return g(a+2,b,n+1) or g(a*2,b,n+1) or g(a,b+2,n+1) or g(a,b*2,n+1)
# for i in range(1,47):
#     if g(15,i,0):
#         print(i)
# (F(1006) – F(1004)) / F(1005)?
#f1=0
#for i in range(1006,1,-1):
#    f1+=i
#    print(i,f1)
#for i in range(1006,1,-2):
#    f1+=i
#print(f1)
#n=1006
#f1=0
#while n>2:
#    if n<3:
#        f1+=n
#    n-=1
#n=1006
#while n>2:
#    if n<3:
#        f1+=n
#    n-=2
#print(f1)
#
#k=0
#for q in 'ВЕРОНИКА':
#    for w in 'ВЕРОНИКА':
#        for e in 'ВЕРОНИКА':
#            for r in 'ВЕРОНИКА':
#                for t in 'ВЕРОНИКА':
#                    for y in 'ВЕРОНИКА':
#                        s=q+w+e+r+t+y
#                        kolg=0
#                        kols=0
#                        for i in s:
#                            if i in 'ЕОИА':
#                                kolg += 1
#                            if i in 'ВРНК':
#                                kols += 1
#                        if kolg>kols:
#                            k+=1
#print(k)
#f=open('09.csv')
#k=0
#for s in f:
#    #print(s)
#    a=list(map(int,s.split(';')))
#    #print(a)
#    kol_ch=0
#    kol_nech=0#!
#    s_nech=0#min
#    s_che=0
#    for i in a:
#        if i % 2 == 0:
#            kol_ch += 1
#            s_che += i
#        if i % 2 != 0:
#            kol_nech += 1
#            s_nech += i
#    if (a[0]!=a[1]!=a[2]!=a[3]!=a[4]!=a[0]!=a[2]!=a[4]!=a[1]!=a[3]!=a[0])and(kol_nech>kol_ch)and(s_nech<s_che):
#    #if (len(set(a))==5) and (kol_nech > kol_ch) and (s_nech < s_che):
#        k+=1
#        print(a)
#print(k)
## Задание 12
from itertools import product
for i in product('12',repeat=20):
    if i.count('1')==10 and i.count('2')==10:
        #s='0'+10*'1'+10*'2'+'0'
        s='0'+''.join(i)+'0'
        while '00' not in s:
            s=s.replace('012','30',1)
            if '011' in s:
                s=s.replace('011','20',1)
                s=s.replace('022','40',1)
            else:
                s=s.replace('01','10',1)
                s = s.replace('02','101',1)
        if s.count('1')==7 and s.count('2')==3:
            print(s.count('3'))
#def dell(m,n):
#    if m%n==0:
#        return True
#    else:
#        return False
#
#for a in range(1,100):
#    f=1
#    for x in range(1,100):
#        for y in range(1,100):
#            if not((not(dell(144, x))or (not(dell(x, y)))) or (x+y > 100) or(a-x > y)):
#                f=0
#    if f==1:
#        print(a)
#