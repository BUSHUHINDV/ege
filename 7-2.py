import random
game=['камень','ножницы','бумага']
comp=random.choice(game)
print('Сделай свой выбор:')
user=input('1-камень 2-ножницы 3-бумага\n')
user_choice=game[int(user)-1]
if user_choice=='камень' and comp=='бумага' or \
    user_choice == 'ножницы' and comp == 'камень'or\
    user_choice == 'бумага' and comp == 'ножницы':
    print('Победил компьютер',' компьютер выбрал: ',comp)
elif user_choice=='бумага' and comp=='камень' or \
    user_choice == 'камень' and comp == 'ножницы'or\
    user_choice == 'ножницы' and comp == 'бумага':
    print('Ты победил',' компьютер выбрал: ',comp)
elif user_choice == comp:
    print('Ничья',' компьютер выбрал: ',comp)