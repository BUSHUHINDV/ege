for i in range(1,2000):
    for i1 in range(1,2000):
        x = i
        y = i1
        a = 0
        b = 0
        while x * y > 0:
            if x > 0:
                a = a + 1
            if y > 0 and y%7 > b:
                b = y % 7
            x = x // 10
            y = y // 7
        #print(a,b)
        if a==4 and b==5:
            print('i=',i,'i1=',i1,i*i1)