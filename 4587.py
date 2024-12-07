def D(x,A):
    if x%A==0:
        return True
    else:
        return False
A=45
p=0
for x in range(100):
    #if not(D(45,A) and ((D(x,30) and D(x,12))<=D(x,A))):
        #p = 1
        #break
#if p == 0:
    print("x=",x,D(45,A) and ((D(x,30) and D(x,12))<=D(x,A)))