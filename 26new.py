#f=open('C:/Users/qwe/Downloads/17-199.txt')
#k=0
#m=0
#s=0
#l=[]
#for i in f:
#    l.append(int(i))
#for i in range(len(l)-2):
#    if (1000>l[i+1]>99 and l[i+1]%2!=0) \
#            and (100>l[i] or l[i]>999 or l[i]%2==0) \
#            and (100>l[i+2] or l[i+2]>999 or l[i+2]%2==0):
#        k+=1
#        s=l[i]+l[i+1]+l[i+2]
#        m=max(s,m)
#print(k,m)
#

#def f(n):
#    if n%2==0 and n<100:
#        return 1
#    if n%2!=0 and n>100:
#        return 0
#    if n<100:
#        return f(n+3)+f(n*3)
#print(f(3))
#k=0
#for i in range (3,100):
#    if i%3==0 and i%2==0:
#        k+=1
#        print(k,i)
#
