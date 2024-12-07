# z2
# print('a b c d F')
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 F=(a<=b)and(b<=c)and(c<=d)
#                 if F==1:
#                     print(a,b,c,d,F)

# z5
# def F(n):
#     s=''
#     while n>0:
#         s=s+str(n%5)
#         n=n//5
#     return s[::-1]
# for n in range(1,1000):
#     s=F(n)
#     if n%25==0:
#         s=s[:-1]+s[:-2]+s[:-3]+s
#     else:
#         s=s+F(n%25)
#     r=int(s,5)
#     if r>=10000:
#         print(n,r)
#         break

# z6
# from math import *
# from turtle import *
# k=20
# left(90)
# tracer(0)
# screensize(5000,5000)
# pendown()
# right(60)
# forward(4*k)
# right(120)
# for i in range(4):
#     forward(3*k)
#     right(240)
#     forward(3*k)
#     right(120)
# forward(4*k)
# right(90)
# forward((8*sqrt(4))*k)
# right(90)
# forward(8)
# for x in range(0,100):
#     for y in range(0,100):
#         setpos(x*k,y*k)
#         dot()
# done()

# z8
# k=0
# for x1 in 'АЕКПТЧ':
#     for x2 in 'АЕКПТЧ':
#         for x3 in 'АЕКПТЧ':
#             for x4 in 'АЕКПТЧ':
#                 for x5 in 'АЕКПТЧ':
#                     for x6 in 'АЕКПТЧ':
#                         for x7 in 'АЕКПТЧ':
#                             s=x1+x2+x3+x4+x5+x6+x7
#                             if s>'АПТЕЧКА' and s<'ПЕЧАТКА':
#                                 k+=1
# print(k)

# z12
# for n in range(3,10000):
#     s='5'+'2'*n
#     while '52' in s or '2222' in s or '1112' in s:
#         if '52' in s:
#             s=s.replace('52','11',1)
#             s=s.replace('2222', '5', 1)
#         else:
#             s=s.replace('1112','2',1)
#     sum=s.count('1')*1 + s.count('2')*2 + s.count('5')*5
#     if sum==1685:
#         print(n)
#         break

# z13
# from ipaddress import *
# print(len([ip for ip in ip_network( '10.112.0.0/255.248.0.0') if f'{ip:b}'.count('1')]))

# z14
# a=18*7**108-5*49**76+343**35-50
# a=abs(a)
# print(a)
# o=[]
# while a>0:
#     o.append(a%49)
#     a=a//49
# print(sum(o))

# z16
from sys import *
setrecursionlimit(100000)
def F(n):
    if n>10000:
        return 1
    if n<=10000 and n%2==0:
        return 2*n+F(n+3)+F(n+4)+F(n+6)
    if n<=10000 and n%2!=0:
        return -1*(n+F(n+1)+F(n+3))
print(F(9996))
print(F(9994))
print(F(9996)-F(9994))

# z17
# a=open('17 (1).txt')
# o=[]
# k=0
# min_pr=40000
# for i in a:
#     o.append(int(i))
# for i in range(len(o)-3):
#     s0=o[i]+o[i+1]
#     s1=o[i-1]+o[i-2]
#     s2 = o[i+2] + o[i+3]
#     if s0>s1 and s0>s2 and s0>=0 and s1>=0 and s2>=0:
#         k+=1
#         min_pr=min(min_pr,o[i]*o[i+1])
# print(k,min_pr)
# z19
from math import *
# print('задание 19')
# def f(a,b,n):
#     if a+b>=231 or n>2:
#         return n==2
#     if n%2==0:
#         return f(a+4,b,n+1) and f(a*3,b,n+1) and f(a,b+4,n+1)and f(a,b*3,n+1)
#     else:
#         return f(a+4,b,n+1) or f(a*3,b,n+1) or f(a,b+4,n+1) or f(a,b*3,n+1)
# for s in range(1,217):
#     if f(10,s,0):
#         print(s)
#
# print('задание 20')
# def f(a,b,n):
#     if a+b>=231 or n>3:
#         return n==3
#     if n%2!=0:
#         return f(a+4,b,n+1) and f(a*3,b,n+1) and f(a,b+4,n+1) and f(a,b*3,n+1)
#     else:
#         return f(a+4,b,n+1) or f(a*3,b,n+1) or f(a,b+4,n+1) or f(a,b*3,n+1)
# for s in range(1,217):
#     if f(10,s,0):
#         print(s)
#
# print('задание 21')
# def f(a,b,n):
#     if a+b>=231 or n>4:
#         return n==2 or n==4
#     if n%2==0:
#         return f(a+4,b,n+1) and f(a*3,b,n+1) and f(a,b+4,n+1) and f(a,b*3,n+1)
#     else:
#         return f(a+4,b,n+1) or f(a*3,b,n+1) or f(a,b+4,n+1) or f(a,b*3,n+1)
# for s in range(1,217):
#     if f(10,s,0):
#         print(s)

# z23
# def f(n):
#     if n==89:
#         return 1
#     if n>89 or n==81:
#         return 0
#     return f(int(str(n)[0])+n)+f(n+3)+f(2*n-1)
# print(f(73))

# z25
# from fnmatch import  *
# for i in range(2*10**8,240,-1):
#     if fnmatch(str(i),'?2*4*0') and not(fnmatch(str(i),'1*7*')) and i%42==0:
#         print(i,i//42)
