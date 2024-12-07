#def g(s,n):
#    if s>164 or n>4:
#        return n==4 or n==2
#    if n%2==0:
#        return g(s+1,n+1) and g(s*2,n+1)
#    return g(s+1,n+1) or g(s*2,n+1)
#
#for i in range(1,165):
#    if g(i,0):
#        print(i)
def f(n,osn):
    s=''
    while n>0:
        s=str(n%osn)
        n=n//osn
    return int(s)
print(oct(123))
print(f(123,8))
k=0
for q in '123456789':
    for w in '0123456789':
        for e in '0123456789':
            for r in '0123456789':
                for t in '0123456789':
                    for y in '0123456789':
                        s=q+w+e+r+t+y
                        if int(s)%f(int(s),12)==0:
                            k+=1
print(k)

