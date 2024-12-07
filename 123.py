a=int(input("введите первое число: "))
b=int(input("введите второе число: "))
q=input("введите знак операции + - * /")
if q=='+':
    print(a,'+',b,'=',a+b)
if q=='-':
    print(a,'-',b,'=',a-b)
if q=='*':
    print(a,'*',b,'=',a*b)
if q=='/':
    if b != 0:
        print(a,'/',b,'=',a/b)
    else:
        print('на ноль делить нелья')