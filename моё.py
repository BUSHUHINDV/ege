#'''Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
#F(n) = 1, при n < 2,
#F(n) = F(n/3) - 1, когда n ≥ 2 и делится на 3,
#F(n) = F(n - 1) + 7, когда n ≥ 2 и не делится на 3.
#Назовите минимальное значение n, для которого F(n) равно 111.'''
#def f(n):
#    if n<2:
#        return 1
#    if n>=2 and n%3==0:
#        return f(n/3)-1
#    if n>=2 and n%3!=0:
#        return f(n-1) + 7
#for n in range(1,100000):
#    f(n)
#    if f(n)==111:
#        print(n)

'''(А. Богданов) Значение выражения 81**18 - (81**8 - 1)((8 + 1)8 + 1) / 8 - 8 записали в системе счисления
 с основанием 3. Найдите количество единиц в этой записи.'''
#ss=''
#oo=''
#o=81**18 - (81**8 - 1)*((8 + 1)**8 + 1) // 8 - 8
##oo=str(o)
##print('{o:}'.format(123))
#
#print(o)
#while o>0:
#    s=o%3
#    ss=str(s)+ss
#    o=o//3
#print(ss)
#k=ss.count('1')
#print(k)



########################################################################
import decimal
####ss=''
####oo=0
#####o=81**18 - (81**8 - 1)*((8 + 1)**8 + 1) / 8 - 8
#####o=int(o)
####o=81**18 - (81**8 - 1)*((8 + 1)**8 + 1) // 8 - 8
#####print(o)
####
####print(o)
#####print(oo)
####while o>0:
####    s=o%3
####    ss=str(s)+ss
####    o=o//3
####print(ss)
####k=ss.count('1')
####print(k)




#f=open('C:/Users/qwe/Downloads/17-10.txt','r')
#l=[]
#k=0
#m=10000
#for i in f:
#    l.append(int(i))
#for i in range (len(l)-1):
#    s=l[i]+l[i+1]
#    if 99 < s < 1000:
#        q1=s%10
#        q2=(s//10)%10
#        if q1>q2:
#            k+=1
#            m=min(s,m)
#print(m,k)
#def f(x,p):
#    if x>=43 and p==4 and x<72:
#        return True
#    else:
#        if x<43 and p==4 and x>=72:
#            return False
#        else:
#            if x>=43 and x>=72:
#                return False
#        if p%2==1:
#            return f(x+1,p+1) or f(x*2,p+1) or f(x*3,p+1)
#        else:
#            return f(x + 1, p + 1) and f(x * 2, p + 1) and f(x*3,p+1)
#
#for i in range(1,43):
#    if f(i,1):
#        print(i)
#
#k=0
#q=''
#m=0
#f=open('C:/Users/qwe/Downloads/24-171.txt')
#for i in f:
#    s=i
#    print(s)
#    for j in s:
#        if j=='X':
#            q=q+j
#        if q=='X' and j=='Y' :
#            q+=j
#        else:
#            q=''
#            k=0
#        if q=='XY' and j=='Z':
#            q+=j
#            k+=1
#            m=max(m,k)
#        else:
#            q=''
#            k=0
#print(m)
#
#
#t=0
#k=0
#f=open('C:/Users/qwe/Downloads/24-171.txt')
#l=[]
#m=['XYZ','YZX','ZXY']
#for i in f:
#    l.append(i)
#for i in range (len (l)):
#    for j in range(len(l[i])-2):
#        s=l[i][j]+l[i][j+1]+l[i][j+2]
#        if s in m:
#            k+=1
#
#        else:
#            t=max(k,t)
#
#            k=0
#        print(t+2)


##f=open('C:/Users/qwe/Downloads/17-5.txt')
##l=[]
##k=0
##m=0
##t=0
##for i in f:
##    l.append(int(i))
##print(l)
##for i in range(len(l)-1):
##    if abs(l[i])%10==7 or abs(l[i+1])%10==7:
##        k+=1
##        t=l[i]+l[i+1]
##        m=max(t,m)
##print(k,m)
##print(abs(l[5])%10)
##

#def f(a,n):
#    if a>=100 or n>2:
#        return n==2
#    if n%2==0:
#        return any([f(a+1,n+1), f(a*a,n+1)]) # при любой игре - даже если дурак
#
#    return any([f(a+1,n+1), f(a*a,n+1)])
#
#for s in range(1,99):
#    if f(s,0):
#        print(s)
#        break # отсечка на минимальном
#
#for x in range(2,11):
#    o=609
#    ss=''
#    while o>0:
#        s=o%x
#        ss=str(s)+ss
#        o=o//x
#    print(ss,x)
#'''Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K
#(логическое «И» между соответствующими битами двоичной записи).
# Определите наименьшее натуральное число A, такое что выражение
#(( (X & 13 ≠ 0) ∨ (X & A = 0)) → (X & 13 ≠ 0)) ∨ (X & A ≠ 0) ∨ (X & 39 = 0)
#тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной X)?'''
#
#
#q=0
#def f(a,b):
#    s=''
#    za=bin(a)[2:]
#    zb=bin(b)[2:]
#    if len( za) > len(zb):
#        l= len( za) - len(zb)
#        zb='0'*l+zb
#    else:
#        l = len(zb) - len(za)
#        za = '0' * l + za
#    for i in range(len(za)):
#        if za[i]=='1' and zb[i]=='1':
#            s+='1'
#        else:
#            s+='0'
#    return int(s,2)

##print(f(13,39))
#for A in range(100):
#    q=1
#    for x in range(100):
#        if not ((( (f(x,13) != 0) or (f(x,A) == 0)) <= (f(x,13) != 0)) or (f(x,A) != 0) or (f(x,39) == 0)):
#            q=0
#    if q==1:
#        print(A)
#

#def f(n):
#    if n<2:
#        return 1
#    if n>=2 and n%2==0:
#        return f(n/2)+1
#    if n>=2 and n%2!=0:
#        return f(n-3)+3
#for n in range(100,1000):
#    if f(n)==31:
#        print(f(n),n)
#

#f=open('C:/Users/qwe/Downloads/17-4.txt')
#l=[]
#m=0
#k=0
#for i in f:
#    l.append(int(i))
#for i in range (len(l)):
#   if l[i]%3==0 and l[i]%7!=0 and l[i]%17!=0 and l[i]%19!=0 and l[i]%27!=0:
#       k+=1
#       m=max(l[i],m)
#print(k,m)

#print('19задание')
#def f(a,b,n):
#    if a+b>=77 or n>2:
#        return n==2
#    else:
#        return any([f(a+1,b,n+1),f(a*2,b,n+1),f(a,b+1,n+1),f(a,b*2,n+1)])
#for i in range(1,77):
#    if f(i,7,0):
#        print(i,)
#        break
#print('20задание')
#
#def f(a,b,n):
#    if a+b>=77 or n>3:
#        return n==3
#    if n%2==1:
#        return all([f(a+1,b,n+1),f(a*2,b,n+1),f(a,b+1,n+1),f(a,b*2,n+1)])
#    return any([f(a+1,b,n+1),f(a*2,b,n+1),f(a,b+1,n+1),f(a,b*2,n+1)])
#for i in range(1,77):
#    if f(i,7,0):
#        print(i)
#
#print('21задание')
#def f(a,b,n):
#    if a+b>=77 or n>4:
#        return n==4 or n==2
#    if n%2==0:
#        return all([f(a+1,b,n+1),f(a*2,b,n+1),f(a,b+1,n+1),f(a,b*2,n+1)])
#    return any([f(a+1,b,n+1),f(a*2,b,n+1),f(a,b+1,n+1),f(a,b*2,n+1)])
#for i in range(1,77):
#    if f(i,7,0):
#        print(i)
#
#for i in range(1000):
#   x = i
#   a = 0
#   b = 1
#   while x > 0:
#     if x % 2 > 0:
#       a = a + x % 13
#     else:
#       b = b * (x % 13)
#     x = x // 13
#   if a==4 and b==7:
#       print(i,a,b)
#
#def f(n):
#    if n==20:
#        return 1
#    if n>20:
#        return 0
#    if n==12:
#        return 0
#    if n<20:
#        return f(n+1)+f(n*2)
#print(f(3))
#
#def f2(n):
#    if n==30:
#        return 1
#    if n>30:
#        return 0
#    if n<30:
#        return f2(n+1)+f2(n*2)
#print(f2(20))


#def f(a,b,c,n):
#    if a+b+c>=73 or n>2:
#        return n==2
#    else:
#        return any([f(a+3,b,c,n+1),f(a+13,b,c,n+1),f(a+23,b,c,n+1),f(a,b+3,c,n+1),f(a,b+13,c,n+1),f(a,b+23,c,n+1),f(a,b,c+3,n+1),f(a,b,c+13,n+1),f(a,b,c+23,n+1),])
#for i in range(1,23):
#    if f(2,i,2*i,0):
#        print(i)

#def f(n):
#    if n<=5:
#        return n
#    elif n>5 and n%4==0:
#        return n+f(n/2-1)
#    elif n > 5 and n % 4 != 0:
#        return n+f(n+2)
#
#for n in range(2,50,2):
#    print(n,f(n))

#def f(n):
#    if n== '110001':        return 1
#    if int(n,2)>int('110001',2):        return 0
#    else:        return f(bin(int(n,2)+1)[2:])+f('1'+n)
#print(f('100')    )
#
#
#f=open('C:/Users/qwe/Downloads/24-s1.txt')
#l=[]
#for i in f:
#    l.append(i)
#k='QWERTYUIOPASDFGHJKLZXCVBNM'
#q=0
#mq=0
#for j in range (len(l)):
#    v=l[j].count('Q')
#    if v>mq:
#        q=j
#        mq=v
#print(mq,q)
#print(l[835])
#for i in k:
#    print(i,l[835].count(i))
#h=0
#for i in range(len(l)):
#    h+=l[i].count('C')
#print(h)

#N=0
#for m in range(2,50,2):
#    for n in range(1,50,2):
#        N=2**m*3**n
#        if 150000000<N<300000000:
#            print('N==',N,' m==',m,' n==',n, ' m+n=' ,m+n)

#f=open('C:/Users/qwe/Downloads/27-59a.txt')
#l=[]
#k=0
#for i in f:
#   l.append(int(i))
#print(l)
#for i in range (len(l)-1):
#    ss=l[i]
#    for j in range (i+1,len(l)):
#        ss+=l[j]
#        if ss%10==5:
#            k+=1
#print(k)
#
#
#s=0
#o=51616564684111151357987987987987879889
#while o>0:
#    s=s+o%10
#    o=o//10
#print(s)

#f=open('C:/Users/qwe/Downloads/17-7.txt')
#l=[]
#k=0
#m=0
#m1=0
#for i in f:
#    l.append(int(i))
#for i in range(len(l)-2):
#    if (str(hex(l[i])[2:][-1])=='0' and str(hex(l[i+1])[2:][-1])=='0') or (str(hex(l[i+1])[2:][-1])=='0' and str(hex(l[i+2])[2:][-1])=='0') or (str(hex(l[i+2])[2:][-1])=='0' and str(hex(l[i])[2:][-1])=='0'):
#        k += 1
#        m=max(l[i],l[i+1],l[i+2])
#        m1+=m
#        print(k,m1)
#'''
#print('x y z')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#             print(x,y,z,not(x == (y <= z)))
#'''
#'''
##¬ (ДЕЛ(x, 16) ≡ ДЕЛ(x, 24)) → ДЕЛ(x, A)
#q=0
#for A in range(1,10):
#    q=1
#    for x in range(1,1000):
#        if not((not ((x%16==0) == (x%24==0))) <= (x%A==0)):
#            q=0#;print(x,'!!!!!!!!!!!!!!!!')
#        #else: print(A,x)
#    if q==1:
#        print(A)
#'''
#def f(n):
#    if int(n,2)==int('100',2):
#        return 1
#    elif int(n,2)<int('100',2):
#        return 0
#    elif n == '1' + '0' * (len(n) - 1):
#        return 0
#    else:
#        return f(bin(int(n,2)-1)[2:])+f('1'+'0'*(len(n)-1))
#n='1100'
#print(f(n))
#'''


#f=open('C:/Users/qwe/Downloads/17-204.txt')
#l=[]
#m=0
#k=0
#l1=[]
#lt=[]
#for i in f:
#    l.append(int(i))
#for i in range(len(l)-2):
#    if (l[i+1]>=0 and l[i+1]%10==9) and(l[i]<=0 or l[i]%10!=9 ) and(l[i+2]<=0 or l[i+2]%10!=9):
#        k+=1
#        p=l[i]+l[i+1]+l[i+2]
#        m=max(p,m)
#print(l1)
#print(k,m)
#
#q=0
#k=0
#P=[1,3,7]
#Q=[1,2,4,5,6]
#A=[1,3,7]
#for a in A:
#    q=1
#    for x in range(100):
#        if not(((x == a) <= (x not in P)) or ((x not in Q) and (x in P))):
#            q=0
#    if q==1:
#        k+=1
#        print(k,A)
#
#k=0
#def f(n):
#    if n==1:
#        return 1
#    if n>=2 and n%2==0:
#        return f(n/2)+1
#    if n>=2 and n%2==1:
#        return f(n-1)+n
#for n in range (1,100001):
#    if f(n)==16:
#        k+=1
#        print(k,n)


#f=open('C:/Users/qwe/Downloads/17-7.txt')
#l=[]
#k=0
#s=0
#for i in f:
#    l.append(int(i))
#for i in range(len(l)-2):
#    if l[i]%3==2 or l[i+1]%3==2 or l[i+2]%3==2:
#        k+=1
#        s+=min(l[i],l[i+1],l[i+2])
#        print(k,s)
#
#def f(a,n):
#   if a>=33 or n>4:
#       return n==4 or n==2
#   if n%2==0:
#       return all([f(a+3,n+1),f(a*2,n+1)])
#   else:
#       return any([f(a+3,n+1),f(a*2,n+1)])

#or i in range(1,33):
#   if f(i,0):
#       print(i)

#def f(a,n):
#    if a>=33 or n>2:
#        return  n==2
#    if n%2==0:
#        return all([f(a + 3, n + 1), f(a * 2, n + 1)])
#    else:
#        return any([f(a+3,n+1),f(a*2,n+1)])
#
#for i in range(1,33):
#    if f(i,0):
#        print(i)
#
#f=open('C:/Users/qwe/Downloads/17 (2).txt')
#l=[]
#k=0
#m=0
#for i in f :
#    l.append(int(i))
#for i in range(len(l)-1):
#    for j in range(i+1,len(l)):
#        g=abs(l[i]-l[j])
#        if (g%36==0) and (l[i]%13==0 or l[j]%13==0):
#            k+=1
#            m=max(g,m)
#print(k,m)



#for n in range(1,10):
#    for a in range(200):
#        for b in range(200):
#            if (a-11)*n==-27 and (b-12)*n==-90:
#                print(a,b,n)


#def f(a,n):
#    if a>=65 or n>2:
#        return n==2
#    if n%2==0:
#        return any([f(a+1,n+1),f(a*4,n+1)])
#    else:
#        return any([f(a+1,n+1),f(a*4,n+1)])
#for s in range(1,65):
#    if f(s,0):
#        print(s)
#        break

#f=open('C:/Users/qwe/Downloads/zadanie24_2.txt')
#s=''
#k=1
#m=0
#for i in f:
#    s=s+i
#for i in range(len(s)-1):
#    if s[i]!=s[i+1]:
#        k+=1
#
#    else:
#        m = max(k, m)
#        k=1
#print(m)

#for i in range(110203,110246):
#    k=0
#    s = []
#    for j in range(1,i//2+1):
#        if i%j==0:
#            if j%2==0:
#                k+=1
#                s.append(j)
#    if i%2==0:
#        k+=1
#        s.append(i)
#
#    if k==4:
#        print(s)
#    else:
#        s=[]
#


#
##def f2(n):
##    return (bin(int(n,2)+1)[2:])
##
##def f(n):
##    if int(n,2)==int('11111',2):
##        return 1
##    elif int(n)>int('11111',2):
##        return 0
##    else:
##        print(bin(int(n,2)+1)[2:])
##        return f2(n)+f('1'+n)
##print(f('1'))
#
##def f(n):
##    if n==int('11111',2):
##        return 1
##    if n>int('11111',2):
##        return 0
##    if n<int('11111',2):
##        return f(n+1)+f(int(('1'+bin(n)[2:]),2))
##print(f(1))
##l='Q W E R T Y U I O P L K J H G F D S A Z X C V B N M'
##l2=[]
##p=[]
##l2=l.split()
##l2.sort()
##print(l2)
##g=[]
##k=0
##km=10000
##z=0
##for i in range(len(l2)-1):
##    g.append(l2[i]+l2[i+1])
##print(g)
##f=open(('C:/Users/qwe/Downloads/24-s1 (1).txt'))
##f1=[]
##for i in f:
##    f1.append(i)
##for i in f1:
##    k=0
##    for j in range(len(i)-1):
##        if i[j]+i[j+1] in g:
##            k+=1
##    if k!=0:
##        km=min(km,k)
##        p.append(km)
##
##    z+=1
##    #if km==18:
##    #    print(z)
##print(f1[344])
##a=0
##r=0
##v=0
##for s in l:
##    #print(s,f1[344].count(s))
##    a=f1[344].count(s)
##    #if a>f1[344].count(s):
##    #    a=max(a,f1[344].count(s))
##    print(a,s)
###    r=max(r,a)
###print(s,r)
##for i in f1:
##    v+=i.count('U')
##print(v)

#q=0
#for a in range(100):
#    q=1
#    for x in range(100):
#        if not (((x%2==0) <= (x%5!=0)) or (x+a >=90)):
#            q=0
#    if q==1:
#        print(a,x)

#f=open('C:/ЕГЭ 27,04/KEGE_KIM_0001512601/KIM_0001512601_24.txt')
#l=f.readline()
#i=0
#k=0
#m=0
#while i<len(l)-1:
#    if (l[i]=='B' and l[i+1]=='A') or (l[i]=='D' and l[i+1]=='A'):
#        k+=1
#        i+=2
#        m=max(m,k)
#    else:
#        k=0
#        i+=1
#print(m)
#l=l.replace('BA','1')
#l=l.replace('DA','1')
#for i in range(300):
#    if l.count('1'*i)!=0:
#        m=max(m,i)
#print(m)


#f=open('C:/ЕГЭ 27,04/KIM_0002848150_27_A__nrvx.txt')
#n=int(f.readline())
#l=[]
#nz=0
#k=0
#s=0
#m=2500645739106599
#for i in f:
#    l.append(int(i))
#for z in range(len(l)):
#     s=0
#     #print(z)
#     for j in range(len(l)):
#         s+=l[j]*(abs(z-j))
#         #print(l[j],(abs(z-j)), ' ',end=' ')
#     if s<m:
#         k=z+1
#     m=min(m,s)
#     print(z,m ,s)
#print(k,'   ',m,'otvet')
##
##o=5*216**3031+4+36**3042-3*6**3053-3064
##ss=''
##while o>0:
##    s=o%6
##    ss=str(s)+ss
##    o=o//6
##print(ss)
##i=int(ss)
##u=0
##while i>0:
##   u+=i%10
##   i=i//10
##print(u)
##
#k=0
#m=0
#f=open('C:/Users/qwe/Downloads/24-157.txt')
#n=f.readline()
#for i in range(len(n)):
#    k+=1
#    if n[i]=='Q' and n[i+1]=='W':
#        m=max(k,m)
#        k=0
#print(m)

#from functools import *
#@lru_cache(None)
#
#def P(n):
#    for i in range(2,n//2+1):
#        if n%i==0 and i!=n:
#            return True
#        else:
#            False
#
#for i in range(704969,1,-2):
#    s=0
#    print('-  ',i)
#    for j in range(4,i//2+1):
#        if i%j==0 and P(j):
#            s+=j
#    if s!=0 and i%s==0:
#        print(i,s)
#k=0
#from itertools import product
#for i in product('елносц',repeat=5):
#    k += 1
#    s=''.join(i)
#    if s.count('е')<2 and s.count('л')==0:
#        print(k,s)
#        break
#P=list(range(10,15))
#Q=list(range(5,21))
#R=list(range(15,26))
#A=[]
#for a in range(5,26):
#    A.append(a)
#    #print(A)
#    q=1
#    for x in range(5,26):
#        if not((not(x in A)) <= (x in P) and (x in Q) <= (x in R)):
#            q=0
#    if  q==1:
#       print(a)
#    else:
#        A.pop()
#print(A)
#k=0
#m=0
#s=''
#sm=''
#f=open('C:/Users/qwe/Downloads/24-168.txt')
#n=f.readline()
#for i in  range(len(n)-1):
#    if n[i]<=n[i+1]:
#        k+=1
#        s=s+n[i]
#    else:
#        m=max(m,k)
#        k=0
#        if len(sm)<len(s):
#            sm=s
#        s=''
#print(m,sm)
#print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

#def f(a,n):
#    if a>=65 or n>2:
#        return n==2
#    if n%2==0:
#        return any([f(a+1,n+1),f(a*4,n+1)])
#    else:
#        return any([f(a+1,n+1),f(a*4,n+1)])
#for s in range(1,65):
#    if f(s,0):
#        print(s)
#        break

#def f(a,n):
#    if a>=50  :
#        return n==3
#    if n%2==0 and a>69:
#        return n==2
#    if n%2==1:
#        return all([f(a+1,n+1),f(a*2,n+1)])
#    return any([f(a+1,n+1),f(a*2,n+1)])
#for s in range(1,50):
#    if f(s,0):
#        print(s)
#k=0
#for i in range(3,100):
#   if i%2==0:
#       k+=1
#print(k)
#
#f=open('C:/Users/qwe/Downloads/24-157.txt')
#n=f.readline()
#n=n.replace('QW','*')
#l=[]
#k=0
#s=''
#m=0
#sm=''
#for i in n:
#    l.append(i)
#for i in range(len(l)):
#    if l[i]!='*':
#        k+=1
#        s=s+l[i]
#    else:
#        m=max(m,k)
#        k=0
#
#        if len(s)>len(sm):
#            sm=s
#        s=''
#print(m+2)
#print(sm)


#k=0
#for i in range(150000,10000000000):
#    s=0
#    for  j in range(2,i//2+1):
#        if i%j==0:
#            s+=j
#    if s%13==10:
#        print(i,s)
#        k+=1
#        if k==8:
#            break
#
#k=0
#from itertools import product
#for  i in product('АВДПР',repeat=4):
#    s=''.join(i)
#    k+=1
#    if s.count("А")==0 and s.count('В')<=1 and s.count('Д')<=1 and s.count('П')<=1 and s.count('Р')<=1:
#        print(k,s)

#def f(a,n):
#    if a==1 or n>3:
#        return n==3
#    if n%2!=0:
#        if a%2==0:
#            return all([f(a//2,n+1),f(a-3,n+1)])
#        else:
#            if a%3==0:
#                return all([f(a//3,n+1),f(a-2,n+1)])
#    if a % 2 == 0:
#        return any([f(a // 2, n + 1), f(a - 3, n + 1)])
#    else:
#        if a % 3 == 0:
#            return any([f(a // 3, n + 1), f(a - 2, n + 1)])
#for s in range(1,38):
#    if f(s,0):
#        print(s)
#
#s=0
#for  i in range(520000,540000):
#    s=0
#    m=0
#    for j in range(2,i//2+1):
#        if i%j==0:
#            s=s+j
#            m=max(m,j)
#    p=str(s)
#    if p==p[::-1] and s!=0:
#        print(i,s,m)

#k=0
#cm=0
#from math import lcm
#c=0
#f=open('C:/Users/qwe/Downloads/27-77a.txt')
#q=f.readline()
#l=[]
#for i in f:
#    l.append(i.split())
#for i in range(len(l)):
#    for j in range (1,len(l[i])):
#        for y in range(j+1,len(l[i])):
#            print(lcm(int(l[i][j]),int(l[i][y])),end=" ")
#            k+=(lcm(int(l[i][j]),int(l[i][y])))
#    if (k%5==0 and k%7!=0) or (k%5!=0 and k%7==0):
#        cm=max(cm,k)
#    k=0
#    print(' ')
#print(cm)
#
#
#from functools import *
#@lru_cache(None)
#
#def f(n):
#    if n<=3:
#        return n+3
#    if n>3 and f(n-1)%2==0:
#        print('чет',n)
#        return f(n-2)+n
#    if n>3 and f(n-1)%2!=0:
#        print('не чет',n)
#        return f(n-2)+2*n
#s=0
#for i in range(40,51):
#    s+=f(i)
# #   print(f())
#print(s)
#def f(a,n):
#    if a>=56:
#        return n==3
#    if n%2==1:
#        return all([f(a+1,n+1),f(a*3,n+1)])
#    return any([f(a + 1, n + 1), f(a * 3, n + 1)])
#for s in range(1,56):
#    if f(s,0):
#        print(s)

#def f(s,p):
#    if s>=56 and p==3 and s<80:
#        return p==3
#    elif s>=80 and p==2:
#        return p==2
#    elif (s<56 and p==3)  or (s>=80 and p==3):
#        return False
#    if p%2!=0:
#        return (f(s+1,p+1) or f(s*3,p+1))
#    else:
#        return (f(s+1,p+1) and f(s*3,p+1))
#for i in range(1,56):
#    if f(i,0):
#        print(i)

#def f(n):
#    if n==25:
#        return 1
#    if n>25:
#        return 0
#    if n<25 and n%2==0:
#        return f(n+1)+f(n*2)+f(n+1)
#    if n<25 and n%2!=0:
#        return f(n+1)+f(n*2)+f(n+2)
#print(f(17))

#f=open('C:/Users/qwe/Downloads/24-157 (1).txt')
#n=f.readline()
#n = n.replace('PR', '*')
#n = n.replace('RP', '*')
#l=[]
#s=''
#k=0
#m=0
#for i in n:
#    l.append(i)
#for i in range(len(l)-1):
#    s+=l[i]
#    if l[i+1]=='*':
#        m=max(m,len(s)+1)
#        s=''
#print(s,m)
#print(m)

#f=open('C:/Users/qwe/Downloads/27-75a.txt')
#n=int(f.readline())
#p=''
#l=[]
#sm=0
#kk=0
#for i in range(1,n):
#    q=f.readline()
#    l.append(int(q))
#for i in range(len(l)-1):
#    s=l[i]
#    k=1
#    p=[]
#    p.append(l[i])
#    for j in range(i+1,len(l)):
#        s+=l[j]
#        p.append(l[j])
#        k+=1
#
#        if s%43==0 and j<len(l):
#            p.append(l[j])
#            sm=max(sm,s)
#            print(p)
#            print(s)
#            kk=k
#            p=[]
#        if j>=len(l)-i:
#            s = 0
#            k = 0
#            p=[]
#
#print(kk,sm)

#for i in range(40,1020):
#    x = i
#    a = 3 * x - 112
#    b = 3 * x + 58
#    while a != b:
#        if a > b:
#            a -= b
#        else:
#            b -= a
#    if a==34:
#        print(i,a)

#'''(№ 4037) Исполнитель Калькулятор преобразует число, записанное на
# экране в троичной системе счисления.
#У исполнителя есть две команды, которым присвоены номера:
#1. Прибавь 2
#2. Умножь на 2 и прибавь 1
#Сколько различных результатов можно получить из исходного числа 2 после
# выполнения программы,
#содержащей ровно 15 команд?'''
#from itertools import product
#l=['1','2']
#def f(n,k):
#    if k==1:
#        return n+2
#    if k==2:
#        return n*2+1
#u=[]
#for s in product(l,repeat=15):
#    i=''.join(s)
#    a=2
#    for j in i:
#        a=f(a,int(j))
#    if a not in u:
#        u.append(a)
#
#print(u)
#print(len(u))
#f=open('C:/Users/qwe/Downloads/1478.txt')
#k=0
#m=0
#for i in f:
#    s=f.readline()
#    for i in range(len(s)-1):
#        if s[i]=='X' and s[i+1]=='Y':
#            k+=1
#        elif s[i]=='Y' and s[i+1]=='Z':
#            k+=1
#        elif s[i]=='Z' and s[i+1]=='X':
#            k+=1
#        else:
#            m=max(m,k+1)
#            k=0
#print(m)

#for i in range(550000,551000):
#    f=0
#    k=0
#    fs = 0
#    for j in range(2,i//2+1):
#        if i%j==0:
#            k+=1
#            f+=j
#    if k!=0:
#        fs=f//k
#    if fs%31==13:
#        print(i,fs)

#from itertools import permutations
#f=open('C:/Users/Boss/Downloads/27-70a1.txt')
#f1=open('C:/Users/Boss/Downloads/27-70a2.txt')
#l=[]
#l1=[]
#m=0
#m1=0
#mm=0
#for i in f:
#    l.append(int(i))
#for i1 in f1:
#    l1.append(int(i1))
#for q in range(2,21):
#    for q1 in range(2,21):
#        for i in permutations(list(l),q1):
#            for i1 in permutations(list(l1),q):
#                w=sum(i)
#                w1=sum(i1)
#                r=w-w1
#                r1=w1-w
#                if r%5==0 or r1%5==0:
#                    m=max(m,r)
#                    m1=max(m,r1)
#                mm=max(m,m1)
#print(m,m1)
#print(mm)

#for i in range(100):
#    n1=bin(i)[2:]
#    n=n1+n1[-1]
#    if n1.count('1')%2==0:
#        n=n+'0'
#    else:
#        n=n+'1'
#    if n.count('1')%2==0:
#        n=n+'0'
#    else:
#        n=n+'1'
#    if int(n,2)>105:
#        print(i,int(n,2),n)
#        break
#from itertools import product
#k=0
#l=[]
#for i in product('ВАЙФУ',repeat=4):
#    s=''.join(i)
#    if (s[0]!='Й') and (s.count('ВФ')==0) and (s.count('ФВ')==0) and s.count('Й')<=1 and s.count('В')<=1 and s.count('А')<=1 and s.count('Ф')<=1 and s.count('У')<=1:
#        #if s not in l:
#        #    l.append(s)
#        k+=1
#
#        print(k,s)
#print(len(l))
#def f(n):
#    if n<=5:
#        return 5
#    if n>5 and n%5==0:
#        return n + f(n//5 + 1)
#    if n>5 and n%5!=0:
#        return n + f(n + 6)
#for i in range(100,140):
#    try:
#        if f(i)>1000:
#            print(i,f(i))
#    except:
#        print('not')

#f=open('C:/Users/qwe/Downloads/17-5.txt')
#l=[]
#k=0
#m=-100
#for i in f:
#    l.append(int(i))
#for i in range(len(l)-1):
#    if abs(l[i])%10==7 or abs(l[i+1])%10==7:
#        k+=1
#        w=l[i]+l[i+1]
#        m=max(m,w)
#print(k,m)

#f=open('C:/Users/qwe/Downloads/27-58a.txt')
#l=[]
#k=0
#n=f.readline()
#for i in f:
#    l.append(int(i))
#print(l)
#for i in range(len(l)-1):
#    s=0
#    for j in range(i,len(l)):
#        s+=l[j]
#        if s%3==0:
#            k+=1
#print(k)
#
#from itertools import permutations
#f=open('C:/Users/qwe/Downloads/27-58a.txt')
#l=[]
#k=0
#n=int(f.readline())
#for i in f:
#    l.append(str(int(i)))
#for u in range(1,11):
#    for i in permutations(list(l),u):
#        w=0
#        for z in i:
#            w+=int(z)
#        if w%3==0:
#            k+=1
#print(k)

#from itertools import combinations
#from functools import *
#@lru_cache(None)
#def f():
#    f=open('C:/Users/qwe/Downloads/27-58b.txt')
#    l=[]
#    k=0
#    n=int(f.readline())
#    for i in f:
#        l.append(str(int(i)))
#    for u in range(1,31):
#        for i in combinations(list(l),u):
#            w=0
#            for z in i:
#                w+=int(z)
#            if w%10==5:
#                k+=1
#    return k
#print(f())

#for q1 in range(100):
#    for q2 in range(100):А
#        for q3 in range(100):
#            o='0'+'1'*q1+'2'*q2+'3'*q3+'0'
#            while '00' not in o:
#                o=o.replace('01','210',1)
#                o = o.replace('02', '3101', 1)
#                o = o.replace('03', '2012', 1)
#            if o.count('1')==111 and o.count('2')==101 and o.count('3')==35:
#                print(q1+q2+q3+2,q1,q2,q3)

f=open('C:/Users/qwe/Downloads/24-111.txt')
n=f.readline()
l=[]
m=0
s=''
for i in n:
    l.append(i)
    s=s+i
    a=s.count('A')
    b=s.count('B')
    x=s.count('X')
    if a+b+x>=6:
        m=max(m,len(s))
        s=''
print(m)
#k=0
#from functools import *
#@lru_cache(None)
#def f(n):
#    if n==0:
#        return 1
#    elif n>0 and n%2!=0:
#        return 1+f(n-1)
#    elif n%2==0:
#        return f(n//2)
#
#for i in range(352321537, 500000000):
#    try:
#        if f(i)==4:
#            k+=1
#            print(k,i)
#    except:
#        o=o

