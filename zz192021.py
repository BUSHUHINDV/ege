# for x in range(158):
#     s=(2*158**4+7*158**3+3*158**2+x*158+2)+(1*158**4+x*158**3+3*158**2+9*158)
#     if s%73==0:
#         print(s/73,x)
#
# s=29017200+32961670
# print(s)

# s='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'#abcdefghijklmnopqrstuvwxyz
# for i in range(len(s)):
    # print(i,s[i])

#for i in range(55):
#    s=(35*55**3+i*55**2+34*55+33*1)-(2*55**3+33*55**2+i*55+34*1)
#    if s%29==0:
#        print(i,s)
#s=5546859-5460729
#print(s)

# (F(1006) – F(1004)) / F(1005)?
#f1=0
#for i in range(1,1006,-1):
#    f1+=i
#for i in range(1,1006,-2):
#    f1+=i
#
f=open('C:/Users/qwe/Downloads/17-339.txt')
s=[]
for i in f:
    s.append(int(i))
#print(s)
min19=100000
for i in s:
    if i%19==0 and i<min19 and i>0:
        min19=i
print(min19)
k=0
ms=-100000
for i in range(len(s)-1):
    if s[i]+s[i+1]<min19:
        k+=1
        ms=max(ms,(s[i]+s[i+1]))
print(k,ms)


