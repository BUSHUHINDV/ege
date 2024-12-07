
for q in range(100):
    for w in range(100):
        for e in range(100):
            t = '0' + '1' * q + '2' * w + '3' * e
            while '01' in t or '02' in t or '03' in t:
                t=t.replace('01','2302',1)
                t = t.replace('02', '10', 1)
                t = t.replace('03', '201', 1)
            if t.count('1')==60 and t.count('2')==22 and t.count('3')==17:
                print(q)