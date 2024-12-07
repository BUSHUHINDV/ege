# z2
# print('a b c d F')
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 F=c and (a or d) and (d <= b)
#                 if F==1:
#                     print(a,b,c,d,F)

# z5
# for n in range(1,500):
#     s=bin(n)[2:]
#     s=s+str(s.count('1')%2)
#     s=s+str(s.count('1')%2)
#     r=int(s,2)
#     if r>198:
#         print(r)
#         break

# z6
# from math import *
# from turtle import *
# k=20
# left(90)
# tracer(0)
# screensize(5000,5000)
# pendown()
# for i in range(5):
#     forward(35*k)
#     right(90)
#     forward(24*k)
#     right(90)
# penup()
# right(90)
# forward(7*k)
# right(90)
# forward(5*k)
# pendown()
# for i in range(1001):
#     right(90)
#     forward(20*k)
#     right(90)
#     forward(36*k)
# penup()
# for x in range(0,100):
#     for y in range(0,100):
#         setpos(x*k,y*k)
#         dot()
# done()

# z8
# from itertools import *
# g=['А','Ё']
# k=0
# for i in permutations('АРТЁМ',5):
#     if (i[0] in g) and (i[-1] in g):
#         k+=1
# print(k)
# z12
# for n in range(3,10000):
#     s='4'*50
#     while '444' in s or '333' in s:
#         if '444' in s:
#             s=s.replace('444','3',1)
#         else:
#             s=s.replace('333','3344',1)
#         if '3443' in s:
#             s=s.replace('3443','0',1)
#     sum=s.count('4')*4+s.count('3')*3 + s.count('0')*0
# print(s,sum)

# z13
# from ipaddress import *
# print(len([ip for ip in ip_network( '172.30.0.0/255.254.0.0') if f'{ip:b}'.count('1')%12!=0]))

# z14
# k=[]
# for x in range(1,1950):
#     a=72070+7400-x
#     o=[]
#     while a>0:
#         o.append(a%9)
#         a=a//9
#     #print(o.count(0))
#     k.append(o.count(0))
# print(max(k))

# z15
# def ДЕЛ(n,m):
#     if n%m==0:
#         return True
#     else:
#         False
# for a in range(2,500):
#     F=True
#     for x in range(1,500):
#         o=((not ДЕЛ(x,a)) and (x<=150 and x>=132))<=(not ДЕЛ(x,13))
#         if o==False:
#             F=False
#     if F==True:
#         print(a)


# z16
from sys import *
setrecursionlimit(1000000000)
def F(n):
    #print(n)
    if n==41:
        return 41
    if n>41 and n%2==0:
        return F(n-1)-n
    if n>41 and n%2!=0:
        return n*F(n-2)

print(F(5094)/F(5089))

# z17
# f=open('17 (2).txt')
# o=[]
# k=0
# m42=-100000
# ms=-100000
# for i in f:
#     o.append(int(i))
# print(o)
# for i in o:
#     if str(i)[-2:]=='42' and len(str(i))==4:
#         m42=max(m42,i)
# print(m42)
# for i in range(len(o)-2):
#     if (len(str(abs(o[i])))==4  and len(str(abs(o[i+1])))==4  and str(i)[-2:]=='42'   and str(i+1)[-2:]=='42')\
#     or (len(str(abs(o[i])))==4  and len(str(abs(o[i+2])))==4  and str(i)[-2:]=='42'   and str(i+2)[-2:]=='42')\
#     or (len(str(abs(o[i+1])))==4 and len(str(abs(o[i+2])))==4 and str(i+1)[-2:]=='42' and str(i+2)[-2:]=='42'):
#         print('*')
#         if (o[i]+o[i+1]+o[i+2])>m42:
#             k+=1
#             ms=max(o[i]+o[i+1]+o[i+2],ms)
# print(k,ms)
# from math import *
# print('задание 19')
# def f(s,n):
#     if s<=35 or n>2:
#         return n==2
#     if n%2==0:
#         return f(s-2,n+1) and f(s-4,n+1) and f(ceil(s/2),n+1)
#     else:
#         return f(s-2,n+1) or f(s-4,n+1) or f(ceil(s/2),n+1)
# for i in range(1,500):
#     if f(i,0):
#         print(i)
#
# print('задание 20')
# def f(s,n):
#     if s<=35 or n>3:
#         return n==3
#     if n%2!=0:
#         return f(s-2,n+1) and f(s-4,n+1) and f(ceil(s/2),n+1)
#     else:
#         return f(s-2,n+1) or f(s-4,n+1) or f(ceil(s/2),n+1)
# for i in range(1,500):
#     if f(i,0):
#         print(i)
#
# print('задание 21')
# def f(s,n):
#     if s<=35 or n>4:
#         return n==4 or n==2
#     if n%2==0:
#         return f(s-2,n+1) and f(s-4,n+1) and f(ceil(s/2),n+1)
#     else:
#         return f(s-2,n+1) or f(s-4,n+1) or f(ceil(s/2),n+1)
# for i in range(1,500):
#     if f(i,0):
#         print(i)

# z23
# def f(n):
#     if n==42:
#         return 1
#     if n>42 or n==35:
#         return 0
#     return f(n+1)+f(n+2)+f(n+4)
# print(f(33))

# z25
# from fnmatch import  *
# for i in range(0,10**10,96437):
#     if fnmatch(str(i),'7?2*4??9?'):
#         print(i,i//96437)