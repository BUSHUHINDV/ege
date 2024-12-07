f = open ('C:/Users/qwe/Downloads/24-157.txt')
s = f.readline()
l = lmax = 0
for i in range (len(s)-1):
    if not((s[i] == 'P' and s[i + 1] == 'R') or (s[i] == 'R' and s[i + 1] == 'P')):
        l += 1
        if lmax < l:
            lmax = l
    else: l = 1
print (lmax)