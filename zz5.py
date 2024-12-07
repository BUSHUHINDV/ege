'''
k=0
r=0
st=''
for i in range(1000,10000):
    if (i//1000)%4==0:
        #print(i, i//1000, end=" ")
        r=9*1000+i%1000
       # print(r)
        st = oct(r)
        if st[-1] == '4':
           print(st, k)
           k += 1
    if (i//1000)%2==0 and (i//1000)%4!=0:
        print(i, i // 1000, end=" ")
        r = 3000 + i % 1000
        print(r)
        st=oct(r)
    #    print(st)
  #  if r//1000==9 and st[-1]=='4':

    #    print(st)
print(k)
'''
'''
#import math
from math import sqrt
def f(n):
    if sqrt(n)==int(sqrt(n)):
        return sqrt(n)
    else:
        return f(n+1)+1
print(f(4850)+f(5000))
'''
'''
def ДЕЛ(a,b):
    if a%b==0:
        return True
    else:
        return False

for a in range(1,1000):
    fl=True
    for x in range(1,1000):
        if ((ДЕЛ(x,2) <=(not(ДЕЛ(x,3))))or((x + a)>=100))==False:
            fl=False
    if fl:
        print(a)
        break
        '''
'''
Григорий составляет 16-буквенные слова из букв А, Н, Т, И, У, О, П, Я, 
выбирая такие, в которых содержится комбинация АНТИУТОПИЯ, 
причем первая буква – не А, а последняя – не Я. Сколько слов сможет составить Григорий?
'''
from itertools import product
k=0
for x in product('АНТИУОПЯ', repeat=16):
    s = ' '.join(x)
    if (s[0] != 'А') and (s[-1] != 'Я') and ('АНТИУОПЯ' in s):
        print(s)
        k=k+1
print(k)