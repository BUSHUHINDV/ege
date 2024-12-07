# k=0
# for i in range(1000,10000):
#     n=str(i)
#     if int(n[0])%2==0:
#         n1=int(n[0])+int(n[2])
#         n2=abs(int(n[1])-int(n[3]))
#         m=n1+n2
#         if m>20:
#             k+=1
# print(k)

# a=0
# for m in range(500):
#     s='>'+'1'*17+34*'2'+'3'*m
#     while '>1' in s or '>2' in s or '>3' in s:
#         if '>1' in s:
#             s=s.replace('>1','22>',1)
#         if '>2' in s:
#             s=s.replace('>2','2>',1)
#         if '>3' in s:
#             s = s.replace('>3', '1>', 1)
#     a=s.count('1')+s.count('2')*2+s.count('3')*3
#     k=0
#     for i in range(2,a//2+1):
#         if a%i==0:
#             k+=1
#     if k==3:
#         print(m)
# s=1
# for i in range(1,5000+1):
#     s*=i
# d=0
# for i in range(5,5001):
#     d+=i
# print(2*s//d)

# def f(n,p):
#     if n==600:
#         return 1
#     if n>600 or (n%2==0 and p%2==0):
#         return 0
#     return f(n+2,n)+f(n*3,n)+f(n*4,n)
# print(f(1,1))
#
# for i in range(100):
#     n=bin(i)[2:]
#     #print(n)
#     if i%3==0:
#         n+=n[-3:]
#         #print(n[-3:])
#         #print(n)
#     else:
#         l=bin((i%3)*3)[2:]
#         n+=l
#     if int(n,2)<100:
#         print(i)


# rr=[]
# for i in range(10,200):
#     n=bin(i)[2:]
#     #print(n)
#     if i%3==0:
#         n=n+n[-3:]
#     else:
#         ost=i%3
#         n=n+(bin(ost*3)[2:])
#     R=int(n,2)
#     if R>151:
#         rr.append(R)
# print(min(rr))

# f=open('9-218.csv')
# l=[]
# for i in f:
#     #s=f.readline()
#     tmp=list(map(int,i.split(';')))
#     l.append(tmp)
# print(l)
# k=0
# file = open("9-218.csv").readlines()
# for i in range(len(file)):
#     file[i] = file[i].split(";")
#     file[i] = [line.rstrip() for line in file[i]]
#     file[i] = [int(q) for q in file[i]]
# #print(file)
# for i in l:
#     #if i[0]!=min(i) and i[-1]!=max(i):
#     if i[0]!=min(i) and i[-1]!=max(i) and i[0]!=max(i) and i[-1]!=min(i):
#         tmp=sorted(i)
#         #print(tmp)
#         #print(tmp[-1] - tmp[0], tmp[3] - tmp[1])
#         r_max=(tmp[-1]-tmp[0])
#         r_ost=(tmp[2]-tmp[1])
#         if r_ost!=0:
#             if r_max%r_ost==0:
#                 k+=1
# print(k)
# s=0
# for n in range(10000,100000):
#     tmp=oct(n)[2:]
#     # 1 3 5 7 print(tmp)
#     tmp=tmp.replace('1','2')
#     tmp = tmp.replace('3', '2')
#     tmp = tmp.replace('5', '2')
#     tmp = tmp.replace('7', '2')
#     tmp+=str(n%8)
#     r=int(tmp,8)
#     tmp = oct(r)[2:]
#     tmp = tmp.replace('1', '2')
#     tmp = tmp.replace('3', '2')
#     tmp = tmp.replace('5', '2')
#     tmp = tmp.replace('7', '2')
#     tmp += str(n % 8)
#     r=int(tmp,8)
#     if r%2023==0:
#         s+=n
# print(s)

for n in range(26,40):
    r=bin(n)[2:]
    #print(r)
    if int(r,2)%2!=0:
        r=r[:-2]+'10'
    else:
    #if int(r, 2) % 2 == 0:
        r='10'+r[2:]+'1'
    #if
    print(n, int(r,2))
















