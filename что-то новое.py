#f=open('C:/Users/qwe/Downloads/27-99b.txt')
#n=int(f.readline())
#l=[]
#nz=0
#k=0
#s=0
#m=1000
#for i in f:
#    l.append(int(i))
#for z in range(len(l)):
#     s=0
#     #print(z)
#     for j in range(len(l)):
#         s+=l[j]*(abs(z-j))
#         #print(l[j],(abs(z-j)), ' ',end=' ')
#     if s<m:
#         k=z+1
#     m=min(m,s)
#     print(z,m ,s)
#print()
#print(k,'   ',m,'otvet')
#
#'''20:26-1 hous'''

f=open('C:/Users/qwe/Downloads/27-99b.txt')
n=int(f.readline())
l=[]
nz=0
k=0
s=0

for i in f:
    l.append(int(i))
#for z in range(len(l)):
#     s=0
#     #print(z)
#     for j in range(len(l)):
#         s+=l[j]*(abs(z-j))
#         #print(l[j],(abs(z-j)), ' ',end=' ')
#     if s<m:
#         k=z+1
#     m=min(m,s)
#     print(z,m ,s)
#print()
#print(k,'   ',m,'otvet')
#
'''20:26-1 hous'''
m=0
mm=[]
tmp=[]
for i in range(len(l)):
   if l[i]>=m:
       m=l[i]
       tmp=[i,m]
       mm.append(tmp)
       #print(mm)
#mm.sort()
print(mm)



