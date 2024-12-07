#ДЕЛ(45, A) ∧ ((ДЕЛ(x, 30) ∧ ДЕЛ(x, 12)) → ДЕЛ(x, A))
# def D(x,A):
#     if x%A==0:
#         return True
#     else:
#         return False
# A=45
# for x in range(100):
#     print('при x=',x ,(D(45,A) and ((D(x,30) and D(x,12))<=D(x,A))))

# def con(a,b):
#     n1=bin(a)[2:]
#     n2=bin(b)[2:]
#     s=''
#     n1='0'*(8-len(n1))+n1
#     n2 = '0' * (8 - len(n2)) + n2
#     for i in range(len(n2)):
#         if n1[i]=='1' and n2[i]=='1':
#             s+='1'
#         else:
#             s+='0'
#     return int(s,2)
#
# for a in range(100):
#     f=1
#     for x in range(100):
#         if ((con(x,39)==0) or ((con(x,11)==0)<=(not (con(x,a)==0))))==0:
#             f=0
#     if f==1:
#         print(a)
# def Del(n, m):
#     return (n % m) == 0
#
# for i in range(1,1000):
#     Good = True
#     A = i
#     for j in range(1,1000):
#         x = j
#         #print(A, x)
#         if not ((Del(x, 2) <= (not Del(x, 13))) or (x + A >= 1000)):
#             Good = False
#             break
#     if Good:
#         print(i)


# def ДЕЛ(n, m):
#     if n%m==0:
#         return True
#     else:
#         return False
#
#
# for A in range(1,200):
#     F=True
#     for x in range(1,200):
#         #ДЕЛ(x, А) \/ ((x ∈ B) → ¬ДЕЛ(x, 22))
#         if (ДЕЛ(x, A) or ((70<=x<= 90) <= (not(ДЕЛ(x, 22)))))==0:
#             F=False
#     if F:
#         print(A)


for A in range(1,200):
    F=True
    for x in range(1,200):
        for y in range(1, 200):
        #(x&39 = 0 ∨ (x&11 = 0 → ¬(x&А = 0)))
        #(x + y ≤ 30) ∨ (y ≤ x+2) ∨ (y ≥ A)
        #if(x&39 == 0 or ((x&11 == 0) <= (not(x&A == 0))))==0:
            if (((x + y) <= 30) or (y <= (x+2)) or (y >= A))==0:
                F=False
    if F:
        print(A)


















