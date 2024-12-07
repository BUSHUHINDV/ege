#f = open ('C:/Users/qwe/Downloads/17-204.txt')
#e = [int (i) for i in f]
#res = []
##print (e)
#for i in range (len(e) - 2):
#    if (e[i + 1] > 0 and e[i + 1] % 10 == 9) and (e[i] < 0 or e[i] % 10 != 9) and (e[i + 2] < 0 or e[i + 2] % 10 != 9):
#        res.append (e[i] + e[i + 1] + e[i + 2])
#print (len(res), max(res))
#def f(n):
#    if n == 5:
#        return 1
#    elif n < 5:
#        return 0
#    else:
#        return f(n - 8) + f(n // 2)
#print (f(43))
#f = open ('C:/Users/qwe/Downloads/24-179.txt')
#s = f.readline()
#c = 0
#for i in range (len(s) - 4):
#    if s[i] == 'C' and s[i + 1] == 'B' and s[i + 2] == 'C' and s[i + 3] == 'B' and s[i + 4] == 'C':
#        c += 1
#print (c)
# for i in range (522000, 523000):
#     s = 0
#     k = 0
#     for j in range (2, i // 2 + 1):
#         if i % j == 0:
#             k = j
#             s += j
#     if str(s) == str(s) [::-1] and k != 0:
#         print (i, k)

k=s=0
ms=-10000
f=open('C:/Users/qwe/Downloads/17-1.txt')
a=[]
for i in f:
    a.append(int(i))
# print(a)
for i in range(len(a)):
    s+=a[i]
r=s/len(a)
# print(r)
for i in range(len(a)-2):
    if a[i]<r or a[i+1]<r or a[i+2]<r:
        if (a[i]%7==0 and a[i+1]%7==0) or (a[i]%7==0 and a[i+2]%7==0) or (a[i+2]%7==0 and a[i+1]%7==0):
            k+=1
            m=a[i]+a[i+1]+a[i+2]
            ms=max(m,ms)
print(k,ms)