# for q in range(100):
#     for w in range(100):
#         for e in range(100):
#
#             i='0'+'1'*q+'2'*w+'3'*e
#             while '01' in i or '02' in i or '03' in i:
#                 i=i.replace('01','302',1)
#                 i=i.replace('02', '3103', 1)
#                 i=i.replace('03', '20', 1)
#             if i.count('1')==30 and i.count('2')==39 and i.count('3')==42:
#                 print(i,'\n 2=',w)
#5
for i in range(750):
    n=bin(i)[2:]
    if n.count('1')==n.count('0'):
        n=n+n[-1]
    else:
        if n.count('1')>n.count('0'):
            n=n+'0'
        if n.count('1')<n.count('0'):
            n=n+'1'
    if n.count('1')==n.count('0'):
        n=n+n[-1]
    else:
        if n.count('1')>n.count('0'):
            n=n+'0'
        if n.count('1')<n.count('0'):
            n=n+'1'
    g=int(n,2)
    if g%2==0 and g%4!=0:
        print(i)