for i in range(1000):
    s = i
    n = 4
    while s <= 96:
        s = s + 8
        n = n + 5
    if n==54:
        print('i=',i,n)