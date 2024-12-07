#def f(n, m, t):
#    if n == m:
#        return 1
#    elif n > m or n == 12 or n == 20:
#        return 0
#    else:
#        if t == 3:
#            return f(n + 1, m, 1) + f(n + 2, m, 2)
#        else: return f(n + 1, m, 1) + f(n + 2, m, 2) + f(n * 3, m, 3)
#print (f(2, 15, 0) * f(15, 30, 0) * f(30, 38, 0))
alf = 'ABX'
f = open('C:/Users/qwe/Downloads/24-1.txt')
s = f.readline()
i = p = k = count = countm = 0
for e in s:
    if e in alf:
        if p == 0:
            p = 1
            ind = i
        k += 1
    if k <= 5:
        count += 1
        countm = max(count, countm)
    else: p = k = count = 0; i = ind
    i += 1
print (countm)