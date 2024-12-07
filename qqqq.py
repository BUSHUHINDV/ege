s=['A','B','C','D']
k=0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                s=a+b+c+d
                if s.count('A')==1 and s.count('B')==1 and s.count('C')==1 and s.count('D')==1:
                    print(a,'=',b,' & ',c,'=',d)