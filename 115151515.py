'''
16	(№ 3493) (Е. Джобс) Алгоритм вычисления значения функции F(n),
где n – целое число, задан следующими соотношениями:
F(n) = 1, при n < -100000,
F(n) = F(n–1) + 3·F(n–3) + 2, при n > 10,
F(n) = -F(n–1) для остальных случаев.
Чему равно значение F(20)?
'''
def F(n):
    if n < -100000:
        return 1
    if n > 10:
        return F(n-1) + 3 * F(n - 3)+ 2
    else: #n>=-100000 and n<=10:
        #return F(n-1)*(-1)
        if n%2 ==0:
            return -1
        else:
            return 1

print(F(20))
