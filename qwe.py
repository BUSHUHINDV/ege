#n=int(input())
#spisok=[]
#for i in range(n):
#    spisok.append(input())
#
#print(spisok)
'''
s = input()
spisok = [x for x in s.split()]
fnd=input()
k=-1
for i in range(len(spisok)):
    if spisok[i]==fnd:
        k=i+1
        break
if k==-1:
    print('Error')
else:
    print(k)
'''
'''
str1=input()
str2=''
print(len(str1))
for i in range(len(str1)-1,-1,-1):
    print(str1[i],"- ",i)
    str2=str2+str1[i]
print(str2)
print(list(range(0,5,1)))
'''

#print(input()[::-1])
#print("Privet"[::2])
'''
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)
    '''
a = list(map(int, input().split()))
#3, 5, 7 и 9.
if a.count(3)>0:
    a.remove(3)

print(a)

