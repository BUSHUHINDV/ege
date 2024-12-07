for i in range (1, 1000):
    n = i #int(input())
    s = 350
    while 2*s+n < 1100:
        s = s - 5
        n = n + 15
    if s==45:
        print (i)
    #print(s)