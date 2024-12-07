# '''(x ≡ ¬y) → ((x ∧ w) ≡ z)'''
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x == (not y)) <= ((x and w)==z)):
#                     print (x,y,z,w,not((x == (not y)) <= ((x and w)==z))Z)
''' задание 2
F = (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w'''
# print('x y z w')
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 #print(x, y, z, w)
#                 F=(x and (not y))or (y==z)or (not w)
#                 if F==0:
#                     print(x, y, z, w, F)
# print('A B C ')
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#            print(x, y, z,)
#
# from itertools import *
# print('a b c')
# for a,b,c in product([0,1],repeat=3):
#     F= a== ((b or b )<= c)
#     if F==1:
#         print(a, b, c, F)

from itertools import *

def f(a,b,c,d):
    return c and (a or d) and(d<=b)

for n in product([0,1],repeat=6):
    table=[(n[0],n[1],n[2], 0),
           (n[3], 1,   0,  n[4]),
           (0,   n[5], 1,   0)]
    if len(table)==len(set(table)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p,r))) for r in table]==[1,1,1]:
                print(p)