def f(num):
    if num==1:
        return 1
    else:
        return f(num-1)*num
number=int(input('введите число'))
print('факториал числа: ', f(number))
