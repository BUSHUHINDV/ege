name=input('Добрый день, пожалуйста, введите ваше имя: ')
print('Рады вас приветствовать в нашем банке, ',name, '!')
try:
    age=int(input('Введите, пожалуйста, ваш возраст: '))
except ValueError:
    print('Вы ввели не число, данные будут обнулены')
    age=0
if int(age)>=18:
    try:
        money=int(input('Введите ваш среднемесячный доход: '))
    except ValueError:
        print('Вы ввели не число, данные будут обнулены')
        money = 0
    if (money>20000) and(money<40000):
        print('Вы можете получить потребительский кредит на сумму 15000 рублей')
    elif (money>=40000) and(money<80000):
        print('Вы можете получить потребительский кредит на сумму 75000 рублей')
    elif (money>=80000):
        print('Вы наш золотой клиент, давайте подробней наши предложения ')
else:
    print('Вам нужно немного подрасти, так как мы не можем выдать вам кредит\
несовершеннолетнему. Ждем вас через ', 18-int(age), 'лет')