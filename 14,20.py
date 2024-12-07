ii=4**503 + 3 * 4**244 - 2 * 4**444 - 95
#4**503+3*4**244-2*4**444-95
print(ii)
s=''
ss=''
while ii > 0:
    s=str(ii%4)
    ss=s+ss
    ii=ii//4
print(ss.count('3'))


