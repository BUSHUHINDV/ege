# from functools import *
# @lru_cache(None)
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n//10)+f(n%10)
# k=0
# for i in range(99,100):#range(765432015,1542613240):
#     if f(i)>f(i+1):
#         k+=1
#         print(i)
# print(k)
#for n in range(300000000,300100000):
#    a=0
#    for i in range(2,n//2+1):
#        if n%i==0:
#            a+=1
#        if a==5:
#            print(i)
#def f(n):
#    if n==10:
#        return 1
#    elif n>10:
#        return 0
#    else:
#        return f(n+1)+f(n+2)+f(n*2)
#
#def f2(n):
#    if n==12:
#        return 1
#    elif n>12:
#        return 0
#    else:
#        return f2(n+1)+f2(n+2)+f2(n*2)
#print(f(3)*f2(10))
#5!=1*2*3*4*5
#def f(n):
#    if n==1:
#        print(n)
#        return 1
#    else:
#        return f(n-1)*n
#print(f(5))
# import math
# def f(n):
#     if math.sqrt(n)==int(math.sqrt(n)):
#         return math.sqrt(n)
#     else:
#         return f(n+1)+1
# print(f(4850)+f(5000))

# def f(n,p,s):
#     if n==600 and (p==3 and s%11==0):
#         return 1
#     elif n<600 and (p==3 and s%11!=0):
#         p=0
#         s=0
#     elif n>600:
#         return 0
#     else:
#         return f(n+2,p+1,s+n)+f(n*3,p+1,s+n)+f(n*4,p+1,s+n)
# print(f(1,0,0))
# def f(n):
#     if n==0:
#         return 0
#     elif n>0 and n%2==0:
#         return f(n/2)
#     elif n%2!=0:
#         return 1+f(n-1)
# k=0
# for i in range(1,1001):
#     if f(i)==3:
#         k+=1
# print(k)
from sys import *
setrecursionlimit(100000000)
def f(n):
    if n==1:
        return 1
    if n>1:
        return (n-1)*f(n-1)
print((f(2024)+2*f(2023))/f(2022))

