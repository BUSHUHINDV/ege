def f(x,p):
    if (x>=65 and x<100 and (p==3 or p==5)) or (x>100 and (p==4 or p==2)):
        return True
    elif (x>=65 and x<100 and (p==2 or p==4)) or x>100:
        return False
    if p%2==0:
        return f(x+1,p+1) or f(x*3,p+1)
    else:
        return f(x+1,p+1) and f(x*3,p+1)
for i in range(1,65):
    if f(i,1):
        print(i,end=' ')
print('******')
def f1(x,p):
    if x>=65 and x<100 and (p==5 or p==3):
        return True
    elif x>100 and (p==4 or p==2):
        return True
    else:
        if x<65 and p==5:
            return False
        else:
            if x>=65:
                return False

    if p%2==0:
        return f1(x+1,p+1) or f1(x*3,p+1)
    else:
        return f1(x+1,p+1) and f1(x*3,p+1)
for i in range(1,65):
    if f1(i,1):
        print(i,end=' ')