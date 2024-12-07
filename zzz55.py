for i in range(2,100):
    N=bin(i)[2:]
    #print(N)
    if N.count('1')%2==0:
        N=N+"0"
        N='10'+N[2:]
        print(' ',N)
