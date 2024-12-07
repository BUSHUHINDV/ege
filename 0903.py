#k=0
#s=['О', 'Н', 'И', 'К', 'С']
#for a in s:
#    for b in s:
#        for c in s:
#            for d in s:
#                ss=a+b+c+d
#
#                if ss.count('С')==3 and ss.count('О')==1:
#                    k+=1
#print (k)
#for a in s:
#    for b in s:
#        for c in s:
#            for d in s:
#                for e in s:
#                    ss=a+b+c+d+e
#                    if ss.count('С')==3 and ss.count('О')==1:
#                        k+=1
#print(k)
#for a in s:
#    for b in s:
#        for c in s:
#            for d in s:
#                for e in s:
#                    for i in s:
#                        ss=a+b+c+d+e+i
#                        if ss.count('С')==3 and ss.count('О')==1:
#                            k+=1
#print(k)
''' В файле 17-7.txt содержится последовательность целых чисел.
Элементы последовательности могут принимать значения от 0 до 200 включительно.
Рассматривается множество элементов последовательности, для которых сумма цифр кратна 3.
Найдите количество таких чисел и максимальное из них.
'''
#f=open('C:/Users/qwe/Downloads/17-7.txt')
#k=0
#mm=0
#l=[]
#for i in f:
#    l.append(int(i))
#for q in l:
#    e=str(q)
#    z=0
#    for s in e:
#        z=z+int(s)
#        #print(z)
#    if z%3==0:
#        k+=1
#        mm=max(mm,q)
#print (k,mm )

#def f(x,y,p):
#    if x+y>=142 and p==3:
#        return True
#    else:
#        if x+y<142 and p==3:
#            return False
#        return f(x+2,y,p+1) or f(x*2,y,p+1) or f(x,y+2,p+1) or f(x,y*2,p+1)
#for i in range(1,139):
#    if f(2,i,1):
#        print(i)
#
#def f(x,y,p):
#    if x+y>=142 and (p==3 or p==5):
#        return True
#    else:
#        if x+y<142 and  p==5:
#            return False
#        else:
#            if x+y>=142:
#                return False
#    if p%2==0:
#        return f(x+2,y,p+1) or f(x*2,y,p+1) or f(x,y+2,p+1) or f(x,y*2,p+1)
#    else:
#        return f(x + 2, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 2, p + 1) and f(x, y * 2, p + 1)
#
#for i in range(1,139):
#    if f(2,i,1):
#        print(i)

print('19задание')
def f(x,p):
    if x>=29 and p==3:
        return True
    else:
        if x<29 and p==3:
            return False
        return f(x+1,p+1) or f(x*2,p+1)
for i in range(1,29):
    if f(i,1):
        print(i)


print('20задание')
def f(x,p):
    if x>=29 and p==4:
        return True
    else:
        if x<29 and p==4:
            return False
        else:
            if x>=29:
                return False
        if p%2==1:
            return f(x+1,p+1) or f(x*2,p+1)
        else:
            return f(x + 1, p + 1) and f(x * 2, p + 1)
for i in range(1,29):
    if f(i,1):
        print(i)

print('21задание')
def f(x,p):
    if x>=29 and (p==3 or p==5):
        return True
    else:
        if x<29 and p==5:
            return False
        else:
            if x>=29:
                return False
        if p%2==0:
            return f(x+1,p+1) or f(x*2,p+1)
        else:
            return f(x + 1, p + 1) and f(x * 2, p + 1)
for i in range(1,29):
    if f(i,1):
        print(i)

print('19ppp')
def f(x,y,p):
    if x+y>=77 and p==3:
        return True
    else:
        if x+y<=77 and p==3:
            return False
        return f(x+1,y,p+1) or f(x*2,y,p+1) or f(x,y+1,p+1) or f(x,y*2,p+1)
for i in range(1,70):
    if f(7,i,1):
        print(i)

print('20ppp')
def f(x,y,p):
    if x+y>=77 and p==4:
        return True
    else:
        if x+y<77 and p==4:
            return False
        else:
            if x+y>=77:
                return False
    if p%2==1:
         return f(x+1,y,p+1) or f(x*2,y,p+1) or f(x,y+1,p+1) or f(x,y*2,p+1)
    else:
        return f(x+1,y,p+1) and f(x*2,y,p+1) and f(x,y+1,p+1) and f(x,y*2,p+1)
for i in range(1,70):
    if f(7,i,1):
        print(i)

print('21ppp')
def f(x,y,p):
    if x+y>=77 and (p==3 or p==5):
        return True
    else:
        if x+y<77 and p==5:
            return False
        else:
            if x+y>=77:
                return False
    if p%2==0:
         return f(x+1,y,p+1) or f(x*2,y,p+1) or f(x,y+1,p+1) or f(x,y*2,p+1)
    else:
        return f(x+1,y,p+1) and f(x*2,y,p+1) and f(x,y+1,p+1) and f(x,y*2,p+1)
for i in range(1,70):
    if f(7,i,1):
        print(i)