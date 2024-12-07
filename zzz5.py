#k=0
#z=0
#a=[]
#for i in range(10000):
#    n=bin(i)[2:]
#    if int(n,2)%2==0:
#        n='1'+n+'10'
#    else:
#        n = '11' + n + '0'
#    z=int(n,2)
#    if 800<=z and z<=1500:
#
#        if z not in a:
#            a.append(z)
#            k+=1
#            print(k,z)
#print(k)

# variant 1
n=1
for i in range(1,3516+1):
    n*=(2*i-1)*i
m=1
for i in range(1,3513+1):
   m*=(2*i-1)*i
print(n//m)

# variant 2
nn=1
for i in range(3514,3516+1):
    nn*=(2*i-1)*i
print(nn)

shoppingList = ['шоколадный торт', 'пирожное', 'конфеты']
shoppingList.append('воздушные шары')
shoppingList.append('розовое платье')
shoppingList.append('молочный коктейль')

shoppingList.remove('пирожное') # удаляет элемент - по знаению - если не знаем номер



