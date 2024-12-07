f=open('C:/Users/qwe/Downloads/17-7 (5).txt')
e=[int(i) for i in f]
print (e)
k=0
res=0
for i in range (len(e)-2):
    q=hex(e[i])[2:]
    w = hex(e[i+1])[2:]
    r = hex(e[i+2])[2:]
    if (q[-1]=='0' and w[-1]=='0') or (q[-1]=='0' and r[-1]=='0') or (w[-1]=='0' and r[-1]=='0') or (q[-1]=='0' and r[-1]=='0' and w[-1]=='0'):
        #res.append(e[i]+e[i+1]+e[i+2])
        res+=max(int(e[i]),int(e[i+1]),int(e[i+2]))
        k+=1
print (k,res)