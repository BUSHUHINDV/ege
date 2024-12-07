ii= 81**18 - (81**8 - 1)*((8 + 1)**8 + 1) / 8 - 8
#ii=2.25283995449292*10**34
#ii=2.25283995449292e+34
i=int(ii)
print(i)
s=''
ss=''
while i>0:
    s=str(i%3)
    ss=s+ss
    i=i//3
print(ss)
print(ss.count('1'))