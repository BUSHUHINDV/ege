'''
(№ 3457) (Е. Джобс) При каком наибольшем
введённом значении переменной S программа выведет число 257?
'''

for i in range(1000):
    S=i
    #S = int(input())
    S = S // 8
    N = 2
    while S <= 102:
      S = S + 4
      N = N * 2 - 1
    if N==257:
        print('при S=',i,'N=', N)