# for i in range(124065,10**8):
#     n=str(i)
#     if n[0]=='1' and n[1]=='2' and n[-1]=='5' and n[-2]=='6' and n[-4]=='4':
#         if i%161==0:
#             print(i,i/161)

'''задача: Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины;
 в том числе «*» может задавать и пустую последовательность.
Найдите 5 наименьших натуральных чисел, которые кратны 73 и
соответствуют маске 12345*76. Выведите эти числа в порядке возрастания,
справа от каждого числа выведите результат деления числа на 73.'''
# for i in range(1234576,10**10):
#     n=str(i)
#     if n[0]=='1' and n[1]=='2' and  n[2]=='3' and n[3]=='4' and n[4]=='5' and n[-2]=='7'and n[-1]=='6' :
#         if i%73==0:
#             print(i,i/73)

# f=h=k=0
# for i in range(550000,1000000):
#     h = k = 0
#     for x in range(2,i):
#         if i%x==0:
#             k+=1
#             h+=x
#     if k!=0:
#         f=h//k
#     if f%31==13:
#         print(i,f)

# for n in range(11000000,11100000):
#     a=[]
#     s=0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             a.append(i)
#     if len(a)==0:
#         s=0
#     if len(a)>1:
#         s=a[-1]+a[-2]
#     if 0<s<10000:
#         print(s)

# for i in range(3520,10**7):
#     n=str(i)
#     if n[0]=='3' and n[-2]=='2' and  n[-3]=='5':
#         k=0
#         d=0
#         for x in range(2,i//2+1):
#             if i%x==0:
#                 k+=1
#                 d=x
#         if k%2!=0:
#             print(i,d)
# for i in range(1200361,10**8):
#     n=str(i)
#     if n[0]=='1' and n[1]=='2' and n[4]=='3' and n[5]=='6' and n[-1]=='1':
#         if i%273==0:
#             print(i,i//273)
# def min_d(x):
#     for i in range(2,x//2+1):
#         if x%i==0:
#             return i
#     return 1
#
# for n in range(800000,800100):
#
#     if min_d(n)==1:
#         continue
#     min_dd=min_d(n)
#     max_d=n//min_dd
#     m=max_d+min_dd
#     if m%10==4:
#         print(n,m)

# for n in range(3012015,10**10):
#     s=str(n)
#     if s[0]=='3' and s[2]=='1' and s[3]=='2' and s[5]=='1' and s[6]=='4' and s[-1]=='5':
#         if n%1917==0:
#             print(n,n//1917)

# from fnmatch import  *
# for n in range(3012015,10**10):
#     if fnmatch(str(n),'3?12?14*5'):
#         if n%1917==0:
#             print(n,n//1917)

for n in range(700000,800000):
    d7=0
    for d in range(17,n//2+1):
        if n%d==0 and d%10==7:
            d7=d
            break
    if d7==0:
        continue
    print(n,d7)
