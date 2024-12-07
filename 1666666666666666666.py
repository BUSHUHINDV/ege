def F(n):
    if n > 0:
        F(n // 3)
        print(n,end='')
        F(n - 3)
F(9)