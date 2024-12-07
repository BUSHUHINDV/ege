# k=0
# for q in range(8):
#     for w in range(8):
#         for e in range(8):
#             for r in range(8):
#                 for t in range(8):
#                     s=str(q)+str(w)+str(e)+str(r)+str(t)
#                     #print(s)
#                     if s.count('6')==1:
#                         if s[0]=='6' and int(s[1])%2==0  :
#                             k+=1#
#                             print(k,s)# k=k+1
#                         elif s[4]=='6' and int(s[3])%2==0 and s[0]!=0:
#                             k+=1# k=k+1
#                             print(k, s)
#                         elif s[1]=='6' and int(s[2])%2==0 and int(s[0])%2==0 and s[0]!=0:
#                             k+=1# k=k+1
#                             print(k, s)
#                         elif s[2]=='6' and int(s[1])%2==0 and int(s[3])%2==0 and s[0]!=0:
#                             k+=1# k=k+1
#                             print(k, s)
#                         elif s[3]=='6' and int(s[2])%2==0 and int(s[4])%2==0 and s[0]!=0:
#                             k+=1# k=k+1
#                             print(k, s)
# print(k)
'''
k=0
from itertools import *
for i in product('0123456789ab',repeat=5):
    #print(i)
    n=''.join(i)
    print(n)
    if n[0]!='0' and n.count('7')==1 and (n.count('9')+n.count('a')+n.count('b')<=3):
        k+=1
print(k)
'''
# k=0
# from itertools import *
# for i in product("01234567", repeat=5):
#     n=''.join(i)
#     if int(n[0])%2==0 and n[0]!='0' and (n[4]!='2' and n[4]!='6') and n.count('7')<=2:
#         k+=1
#         print(n)
# print(k)

k=0
for q in 'БИКНОПР':
    for w in 'БИКНОПР':
        for e in 'БИКНОПР':
            for r in 'БИКНОПР':
                for t in 'БИКНОПР':
                    for y in 'БИКНОПР':
                        s=q+w+e+r+t+y
                        k += 1
                        #print(k, s)
                        if 'ООО' in s and s.count('Б')<=1 and s.count('И')<=1 and s.count('К')<=1 and s.count('Н')<=1 and s.count('П')<=1 and s.count('Р')<=1 and s.count('О')==3:
                            print(k,s)


