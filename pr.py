'''x=int(input())
if 100<=x<=999:
    print('трехзначное')
else:
    print('нетрехзначное')
'''
'''
import math
x=float(input('x='))
a=float(input('a='))
if x>1:
    y=2/3*a**x+5*math.cos(x)
elif x<-1:
    y=math.tan(x)-a*x
elif -1<=x<=1:
    y=math.sqrt(abs(1+x-a))
print('y=',y)
'''
'''
a,b,c=map(int, input().split())
print(min(a,b,c),a+b+c-min(a,b,c)-max(a,b,c),max(a,b,c))
'''
'''
a=int(input('a='))
x1=a%100 //10;
x2=a%10
x3=a//100
print("сотни", x3)
print("десятки", x1)
print("ндиниы", x2)
'''

# x = int(input())
# if x > 0:
#     print(x)
# else:
#     print(-x)

# from itertools import *
#
# def f(x,y,w,z):
#     return (x or not(y))and (not(y==z))and not(w)
#
# for a in product([0,1],repeat=4):
#     table = [(1,1,a[0],a[1]),(a[2],1,0,0),(1,a[3],1,0)]
#     if len(table) ==len(set(table)):
#             for p in permutations('xywz'):
#                 if [f(**dict(zip(p,r))) for r in table]==[1,1,1]:
#                     print(p)

from itertools import *
def f(a,b,c):
    return ((b or c)==a)==b
for a in product([0,1],repeat=4):
    table = [(a[0],0,0),(0,a[1],a[2]),(0,a[3],0)]
    if len(table) ==len(set(table)):
            for p in permutations('abc'):
                if [f(**dict(zip(p,r))) for r in table]==[1,1,1]:
                    print(p)
# print('a b c')
# for a in 0,1:
#     for b in 0, 1:
#         for c in 0, 1:
#             f=(a==(b or c==b)
#             if f:
#                 print(a,b,c,f)
# def f(n):
#     if n<3:
#         return 2*n
#     if n%2==0:
#         return 3*n+5+f(n-2)
#     if n%2!=0:
#         return n+2*f(n-6)
#
# print(f(61))
# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n==1:
#         return 5
#     if n>1:
#         return 2*n+f(n-1)
#
# a=f(2048);b=f(1024)
# print(a-b)
