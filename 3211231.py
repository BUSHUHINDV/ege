## a ∧ ¬b ∨ (a ∨ b) ∧ c ∨ d
#print ('a b c d')
#for a in range (2):
#    for b in range(2):
#        for c in range(2):
#            for d in range(2):
#                if not(a and (not b) or (a or b) and c or d):
#                    print (a, b, c, d)
#for i in range (100):
#    n=bin(i)[2:]
#    r=0
#    if i%2==0:
#        n=n+'1'
#    else: n=n+'0'
#    if int(n,2)%2==0:
#        n=n+'1'
#    else: n=n+'0'
#    r=int(n,2)
##    if n < 171:
#    print (i, r, n)
#k=0
#for i in range (10000):
#    n = 1
#    s = i
#    while s > n:
#      s = s - 15
#      n = n * 5
#    if n==125:
#        k+=1
#        print(i, n)
#print(k)
for a in range ( 1000):
    for b in range ( 1000):
        s = '1' * b + '3' * a
        while '12' in s or '13' in s:
            s=s.replace('12', '21', 1)
            s=s.replace('31', '23', 1)
            s = s.replace('13', '23', 1)
            if s.count ('1')<1:
                k=0
                for i in s:
                    k = k + int(i)
                if k==404:
                    print (len(s), k)