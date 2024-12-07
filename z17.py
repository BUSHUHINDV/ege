# f=open("C:/Users/qwe/Desktop/inf_11_2023/Доп.файлы/Задание 17/17.txt")
# l=[]
# for i in f:
#     l.append(int(i))
# #print(l)
# #print(len(l))
# max3=-10000
# for i in l:
#     if i >max3 and abs(i)%10==3:
#         max3=i
# print(max3)
# k=0
# maxs2=0
# for i in range(len(l)-1):
#     if (abs(l[i])%10==3 and abs(l[i+1])%10!=3) or (abs(l[i])%10!=3 and abs(l[i+1])%10==3):
#         if max3**2<=l[i]**2+l[i+1]**2:
#             k+=1
#             maxs2=max(l[i]**2+l[i+1]**2,maxs2)
# print(k,maxs2)

# f=open("17_10100 (1).txt")
# a=[]
# for i in f:
#     a.append(int(i))
# m13=0
# for i in a:
#     if i%100==13:
#         if i>m13:
#             m13=i
# k=0
# sm=0
# for i in range(len(a)-2):
#     if (99<a[i]<1000 and 99<a[i+1]<1000 and not(99<a[i+2]<1000)) or \
#         (99 < a[i+1] < 1000 and 99 < a[i + 2] < 1000 and not (99 < a[i] < 1000)) or \
#             (99 < a[i] < 1000 and 99 < a[i + 2] < 1000 and not (99 < a[i + 1] < 1000)) :
#             s=a[i]+a[i+1]+a[i+2]
#             if s<m13:
#                 k+=1
#                 sm =max(sm,s)
#
# print(k,sm)
# f=open('demo_2025_17.txt')
# l=[]
# min_el=100000
# for i in f:
#     l.append(int(i))
#     min_el=min(min_el,int(i))
# #print(l)
# #print(len(l))
# k=0
# max_sum=0
# for i in range(len(l)-1):
#     if l[i]%16==min_el or l[i+1]%16==min_el:
#         k+=1
#         max_sum=max(max_sum,l[i]+l[i+1])
#
#
# print(k, max_sum)

f=open('17_17611 (1).txt')
l=[]
max_el7_4=0
k=0
max_sum=0
for i in f:
    l.append(int(i))
    if 999<int(i)<10000 and int(i)%10==7:
        max_el7_4=max(max_el7_4, int(i))
print(max_el7_4)
for i in range(len(l)-2):
    if (l[i]%10==7 and l[i+1]%10==7 and 999<l[i]<10000 and 999<l[i+1]<10000 ) or \
       (l[i]%10==7 and l[i+2]%10==7 and 999<l[i]<10000 and 999<l[i+2]<10000 ) or \
        (l[i+2]%10==7 and l[i+1]%10==7 and 999<l[i+2]<10000 and 999<l[i+1]<10000) :
        if l[i]+l[i+1]+l[i+2] > max_el7_4:
            k+=1
            max_sum=max(max_sum,l[i]+l[i+1]+l[i+2])
            print(l[i],l[i+1],l[i+2])
print(k, max_sum)