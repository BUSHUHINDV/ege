for i in range(15,17):
    n=i
    n=bin(n)[2:]
    n+=n[-1]
    if n.count('1')%2==0:
        n+='0'
    elif n.count('1')%2!=0:
        n+='1'
    if n.count('1') % 2 == 0:
        n += '0'
    elif n.count('1') % 2 != 0:
        n += '1'
    print(n)
    if int(n,2) >114:
        print('i=',i ,'',int(n,2))
