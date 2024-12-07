# #from ipaddress import *
# #net = ip_network(f'105.224.200.224/255.255.255.224',0)
# #print(net)
# from itertools import *
# # k=0
# # for q in '01':
# #     for w in '01':
# #         for e in '01':
# #             for r in '01':
# #                 for t in '01':
# #                     s=q+w+e+r+t
# #                     s='1101001.111000000.11001000.111'+s
# #                     print(s)
# #                     if s.count('1')%4==0:
# #                         k+=1
# # print(k)
# print('x,y,z,w,F')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 F=(x and (not z)) or (y==z) or (not w)
#                 if F==0:
#                     print(x,y,z,w,F)
'''
k=0
s = '01111010.10011111.10001000.10010'
for x in '0','1':
    for y in '0','1':
        for z in '0', '1':
            s+=x+y+z
            if s.count('1')%4!=0:
                k+=1
print(k)

n = 2*729**2014+2*243**2016-2*81**2018+2*27**2020-2*9**2022-2024
print(n)
a=[]
while (n>0):
    a.append(n%27)
    n=n//27
print(a)
k=0
for i in a:
    if i>9:
        k+=1
print(k)


import sys
sys.setrecursionlimit(100000)
def F(n):
    if n==1:
        return 1
    if n>1:
        return n*F(n-1)
print ((F(2024)-F(2023))/F(2022))


def F(n):
    if n==15:
        return 1
    if n>15:
        return 0
    return F(n+1)+F(n+2)+F(n*2)
print (F(13))
s = '112'*4+'1'*2
while '11' in s:
    if '112' in s:
        s=s.replace('112','6',1)
    else:
        s=s.replace('11','3',1)
print(s)
print(s.count('1')+s.count('2')*2+s.count('6')*6+s.count('3')*3)


def F(n):
    if n==0:
        return 0
    if n%2!=0:
        return F(n-1)+1
    if n>0 and n%2==0:
        return F(n/2)
k=0
for i in range(100000000):
    if F(i)==2:
        k+=1
        print(i)
print (k)

def F(n):
    if n==18:
        return 1
    if n>18 or n==14:
        return 0
    return F(n+1)+F(n+2)
print (F(9))
'''
# print('x,y,z,w,F')
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F=((x and y) or (y and z))==((x<=w) and (w<=z))
#                 if F==1:
#                     print(x,y,z,w,F)
# s = 49**7+7**20-28
# a=[]
# while s>0:
#     a.append(s%7)
#     s=s//7
# print(a.count(6))
# import functools
# @functools.lru_cache()
# def F(n):
#     if n==0:
#         return 0
#     if n%2!=0:
#         return F(n-1)+1
#     if n>0 and n%2==0:
#         return F(n/2)
# k=0
# for i in range(100000000,1000000000):
#     if F(i)==2:
#         k+=1
#         print(i)
# print (k)
def F(n):
    if n==19:
        return 1
    if n>19 or n==12:
        return 0
    return F(n+1)+F(n+2)+F(n*3)
print(F(9))