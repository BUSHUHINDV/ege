for i in range (100):
    a=i
    s=bin(a)[2:]
    s=s+s[-1]
    if s.count('1')%2==0:
        s=s+'0'
    else:
        s=s+'1'
    if s.count('1')%2==0:
        s=s+'0'
    else:
        s=s+'1'
    print(int(s,2))