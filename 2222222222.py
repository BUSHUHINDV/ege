#¬(y → x) \/ (z → w) \/ ¬z,
'''
print('x y w z F')
for x in range(0,2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if (not(y<=x) or(z<=w)or (not z))==False:
                    print(x,y,w,z,not(y<=x) or(z<=w)or (not z))

'''
for i in range(1,100):
    n=bin(i)[2:]
    print('******')
    print(n,' ',end='')
    if n.count('1')%2==0:
        n=n+'0'
        n='10'+n[2:]
        print(n,' ',end='')#n[0]='1';n[1]='0'
    else:
        #n.count('1')%2!=0:
        n=n+'1'
        n='11'+n[2:]
        print(n, ' ', end='')
    if int(n,base=2)>40:
        print('n=',i,'!!!!!!!!!!!!!!!','R= ',int(n,base=2))
    print()