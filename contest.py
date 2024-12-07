# n=int(input())
# s=input()
# a = [int(i) for i in s.split()]
#
# tmp=summ=sum_m=0
# n1=n2=0
# for i in range(n):
#     summ=0
#     for j in range(i,n):
#         summ+=a[j]
#         if summ>sum_m:
#             sum_m=summ
#             n1=i; n2=j
# print(n1,n2)

# a=input()
# a="".join(set(a))
# b=input()
# s=0
# for i in a:
#     s+=b.count(i)
# print(s)
# a,b=map(int, input().split())
# print(a+b)
f=open('input.txt')
s=f.readline()
l=s.split()
ss=0
for i in l:
    ss+=int(i)
print(ss)