#print("Задача ")
#def game(s,n):
#    if s>=29 and n==2:
#        return True
#    if s>=29 and n>2:
#        return False
#    if n%2==0:
#        return game(s+1,n+1) and game(s*2,n+1)
#    return game(s+1,n+1) or game(s*2,n+1)
#
#for i in range(1,28):
#    if game(i,0):
#        print(i)
#def game(s,n):
#    if s>=29 or n>3:
#        return n==3
#    #if s>=29 and n>3:
#    #    return False
#    if n%2!=0:
#        return game(s+1,n+1) and game(s*2,n+1)
#    return game(s+1,n+1) or game(s*2,n+1)
#
#for i in range(1,28):
#    if game(i,0):
#        print(i)
#def game(s,n):
#    if s>=29 or n>4:
#        return n==4 or n==2
#    #if s>=29 and n>3:
#    #    return False
#    if n%2==0:
#        return game(s+1,n+1) and game(s*2,n+1)
#    return game(s+1,n+1) or game(s*2,n+1)
#
#for i in range(1,28):
#    if game(i,0):
#        print(i)
#def game(s,n):
#    if s>=129 and n==2:
#        return True
#    if s>=129 and n>2:
#        return False
#    if n%2==0:
#        return game(s+1,n+1) and game(s*2,n+1)
#    return game(s+1,n+1) or game(s*2,n+1)
#for i in range(1,128):
#    if game(i,0):
#        print(i)
#
def game(s,n):
    if s>=129 or n>4:
        return n==4 or n==2
    #if s>=29 and n>3:
    #    return False
    if n%2==0:
        return game(s+1,n+1) and game(s*2,n+1)
    return game(s+1,n+1) or game(s*2,n+1)
for i in range(1,128):
    if game(i,0):
        print(i)