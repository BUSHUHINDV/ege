# f=open('C:/Users/qwe/Downloads/24 (1).txt')
# s=f.readline()
# a=[]
# k=kmax=0
# for i in range(len(s)-1):
#     if s[i]=='E':
#         a.append(s[i+1])
# p=[]
# z=''
# for i in range(len(a)):
#     k=0
#     if a[i] not in p:
#         p.append(a[i])
#     else:
#         continue
#     for x in range(0,len(a)):
#         if a[x]==a[i]:
#             k+=1
#     if k>kmax:
#         kmax=k
#         z=a[i]
# print(z)
# for n in range(4,100):
#     s='3'+'5'*n
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s=s.replace('25','3',1)
#         if '355' in s:
#             s=s.replace('355','52',1)
#         if '555' in s:
#             s=s.replace('555','23',1)
#     if s.count('2')*2+s.count('3')*3+s.count('5')*5==27:
#         print(n)
# к














# for n in range(4,10001):
#     s='5'+'2'*n
#     while "52" in s or '2222' in s or '1122' in s:
#         if '52' in s:
#             s=s.replace('52','11',1)
#         if '2222' in s:
#             s=s.replace('2222','5',1)
#         if '1122' in s:
#             s=s.replace('1122','25',1)
#     k=1*s.count('1')+2*s.count('2')+5*s.count('5')
#     if k==64:
#         print(n)

for n in range(4,10000):
    s='0'+'2'*n
    while '002'in s or '22' in s:
        if '002' in s:
            s=s.replace('002','44',1)
        else:
            s=s.replace('22', '0', 1)
        if '222' in s:
            s=s.replace('222', '2', 1)
    if (s.count('4')*4+s.count('2')*2)==42:
        print(n)









