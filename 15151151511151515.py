#o= 16**44 * 16**30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
#print(o)
#n=hex(o)[2:]
#print(n)
#while 'f' in n:
#    n=n.replace('f','0',1)
#print(n)
#
#print(n.count('0')-3)

#for i in range(10000000,100000000):
#    x = i
#    x = (x - x % 8) * 10
#    a = 1
#    b = 0
#    while x > 0:
#        if x % 2 != 0:
#            a = a * (x % 4)
#        else:
#            b = b + (x % 4)
#        x = x // 8
#    if a==9 and b==5:
#        print(i)
#        #print(a)
#        #print(b)
#
#
#
#s=''
#for i in n:
#    if i=='f':
#        s=s+'0'
#    else:
#        s=s+i
#print(s.count('0')-3)

#f= open('C:/Users/qwe/Downloads/17-202.txt','r')
#l=[]
#k=0
#p=0
#ml=0
#for s in f:
#    l.append(int(s))
#for i in range(len(l)):
#    print(l[i])
#for i in range(len(l)-2):
#    if l[i+1]%1000==0 and l[i+1]%10==5 and l[i+1]>0:
#        ll=l[i]+l[i+1]+l[i+2]
#        k+=1
#        ml=max(ml,ll)
#print(k,ml)
#

#q='32'*15
#w='42'*5
#e='4'*5
#o=q+w+e
##o=q+e+w
##o=w+q+e
##o=w+e+q
##o=e+q+w
##o=e+w+q
#while '32'in o or '42' in o:
#    if '42' in o:
#        o=o.replace('42','51',1)
#    else:
#        o=o.replace('32','61',1)
#print(o)
#s=0
#for u in o:
#   s+=int(u)
#print(s)
#
#s=0
#ss=''
#o=(64**25 + 4**10) - (16**20 + 32**3)
#while o>0:
#    s=o%4
#    ss=str(s)+ss
#    o=o//4
#print(ss)
#
#def F(n):
#    if n==0:
#        return 1
#    if n==1:
#        return 3
#    if n%2==0 and n>1:
#        return F(n-1) - F(n-2) + 3*n
#    if n>1 and n%2!=0:
#        return F(n-2) - F(n-3) + 2*n
#print(F(40))

#def f1(n):
#    if n==5:
#        return 1
#    if n>5:
#        return 0
#    if n<5:
#        return f1(n-8)+f1(n//2)
#print(f1(102))
#
'''Текстовый файл состоит из символов P, Q, R и S.
Определите максимальное количество идущих подряд символов
в прилагаемом файле, среди которых нет идущих подряд символов P.
Для выполнения этого задания следует написать программу.'''
#f=open('C:/Users/qwe/Desktop/147852.txt','r')
#z=f.read()
#k=0
#d=''
#m=0
#for i in range(len(z)-1):
#    if z[i]=='P' and z[i+1]=='P':
#        k= 1
#    else:
#        k+=1
#        m=max(m,k)
#print(m)
f=open('c:/Users/qwe/Downloads/24.txt','r')
z=f.read()
k=0
q='P' # ;)))
m=0
for i in z:
    if q[-1]=='P' and i=='P':
        k= 1
        p=i
    else:
        q+=i
        k+=1
        m=max(m,k)
print(m)