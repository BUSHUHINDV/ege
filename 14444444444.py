'''
Задание 14 № 2329
Укажите наименьшее основание системы счисления, в которой запись числа 50 трехзначна.
'''
for i in range (3, 8):
    s=''
    s1=''
    n = 50
    while n>0:
        s=str(n%i)
        s1=s+s1
        n=n//i
    print (s1, i)