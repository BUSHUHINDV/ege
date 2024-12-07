i='5'*12+'4'*23+'53'*17
print(i)
while i.count('43')>0 or (i.count('53')>0):
    if i.count('43')>0:
        i=i.replace('43','33',1)
    else:
        i=i.replace('53','433',1)
    print(i)
print(i)
print(i.count('3'))
