# from itertools import *
# s='1010110.00010000.10101'
# k=0
# for i in product('01',repeat=3):
#     s2=''.join(i)
#     #print(s+s2)
#     for i2 in product('01', repeat=8):
#         s3=''.join(i2)
#         ss=s+s2+'.'+s3
#         if ss.count('1')%5!=0:
#             k+=1
# print(k)

# from itertools import  *
# s='00001010.01110'
# k=0
# for i1 in product('01',repeat=3):
#     s1 = ''.join(i1)
#     for i2 in product('01',repeat=8):
#         s2 = ''.join(i2)
#         for i3 in product('01',repeat=8):
#             s3 = ''.join(i3)
#             s=s+s1+s2+s3
#             if s.count('1')%3==0:
#                 k+=1
# print(k)
from ipaddress import *
k=0
#print(len([ip for ip in ip_network( '10.112.0.0/255.248.0.0') if f'{ip:b}'.count('1') % 3 == 0]))
ip=ip_network('115.192.0.0/255.192.0.0')
for i in ip:
    if f'{i:b}'.count('1')%3!=0:
        k+=1
print(k)