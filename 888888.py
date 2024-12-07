l=['З','Е','Р','К','А','Л','О']
k=0
for q in l:
    for w in l:
        for e in l:
            for r in l:
                for t in l:
                    for y in l:
                        s=q+w+e+r+t+y
                        if (s.count('К')>=1 and s.count('K')<=4) and s.count('З')<=1 and s.count('Е')<=1 and s.count('Р')<=1 \
                                and s.count('А')<=1 and s.count('Л')<=1 and s.count('О')<=1 :
                            k+=1
                            print(q,w,e,r,t,y)
print(k)