def pr(n):
    k=0
    nn=n//2+1
    for y in range (2,nn):
        if n % y ==0:
            k=1
        if k==0:
            return True
        else:
            return False
o=1
s=0
d=0
z=0
for i in range(264871,322990):
    z=0; x1=0; x2=0; kk=0
    for l in range(1,i//2+5):
        if i%l==0:
            x1=l%10; x2=(i/l)%10; kk=i//l
            #if not(pr(l)) or not(pr(kk)):
            #    continue
            #     break
            if (x1==x2) and pr(l) and pr(kk):
                z=1
                continue
                #o+=1
                #s+=i
    if z==1 and (x1==x2) and pr(l) and pr(kk):
        print(o,i,x1,'*',x2)
        o+=1
        s+=i
d=s/o
print('kol=',o,'sr=',d)


