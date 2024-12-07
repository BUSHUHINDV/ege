f= open('18-j5.txt','r')
a=[]
a1=[]
y=0
x=0
for line in f:
    a1=[]
    lst_tmp = line.split()
    for x in range(len(lst_tmp)):
        a1.append(int(x))
    a.append(a1)
i=0; j=0
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end= ' ');
    print('\n')
