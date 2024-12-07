f=open('C:/Users/qwe/Downloads/24-215.txt')
b=['A','B','C']
c=['1','2','3']
k=kmax=0
s=f.readline()
# print(s,len(s))
i=0
while i<len(s)-3:
    if s[i] in b and s[i+1] in c and s[i+2] in c:
        k+=1
        i+=3
    else:
        kmax=max(k,kmax)
        k=0
        i+=1
print(kmax)