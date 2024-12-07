print('задание 19')
def game(n,s):
    if n>2 or s>=129:
        return n==2
    if n%2==0:
        return game(n+1,s+1) and game(n+1,s*2)
    return game(n+1,s+1) or game(n+1,s*2)

for i in range(1,128):
    if game(0,i):
        print(i)
        break

print('задание 20')
def game(n,s):
    if n>3 or s>=129:
        return n==3
    if n%2==1:
        return game(n+1,s+1) and game(n+1,s*2)
    return game(n+1,s+1) or game(n+1,s*2)

for i in range(1,128):
    if game(0,i):
        print(i)
