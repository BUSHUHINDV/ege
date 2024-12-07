# f=open('9_10091 (1).csv')
# a=[]
# for i in f:
#     tmp=[]
#     tmp=list(map(int,i.split(";")))
#     a.append(tmp)
# k=0
#
# for i in a:
#     if (i.count(i[0])+i.count(i[1])+i.count(i[2])+i.count(i[3])+i.count(i[4])+i.count(i[5])+i.count(i[6]))==11:
#         sv=sum(i)/7
#         k2 = 0
#         sp=0
#         for j in i:
#             if i.count(j)>1:
#                 sp+=j
#                 k2+=1
#
#         if k2>0:
#             srp = sp / k2
#             if srp<sv:
#                 k+=1
# print(k)
# f=open('9999.txt')
# l=[]
# k=0
# for i in f:
#     #print(i)
#     l=(list(map(int ,i.split())))
#     #print(l)
#     l3=[x for x in l if l.count(x)==3]
#     l1=[x for x in l if l.count(x)==1]
#     # for x in l:
#     #     if l.count(x)==3:
#     #         l3.append(x)
#     #     if l.count(x)==1:
#     #         l1.append(x)
#     if len(l3)==3 and len(l1)==3:
#         #print(l3,l1)
#         if sum(l3)**2 > sum(l1)**2:
#             k+=1
# print(k)

f=open('9.txt')
l=[]
k=0
for i in f:
    l=(list(map(int, i.split())))
    print(l)
    nech=0
    for i in l:
        if i%2!=0:
            nech+=1
    if (l.count(l[0]) > 1 or l.count(l[1]) > 1 or l.count(l[2]) > 1 or l.count(l[3]) > 1) and nech!=3:
        k+=1
    if nech == 3 and not(l.count(l[0]) > 1 or l.count(l[1]) > 1 or l.count(l[2]) > 1 or l.count(l[3]) > 1):
        k+=1
print(k)