for A in range(1,100):
    f=1
    for x in range(1,100):
        for y in range(1, 100):
            #(x + y ≤ 22) ∨ (y ≤ x – 6) ∨ (y ≥ A))
            if ((x+y<=22)or(y<=x-6)or(y>=A))==0:
                f=0
    if f==1:
        print(A)

# (ДЕЛ(x, 2) → ¬ДЕЛ(x, 3)) ∨ (x + A ≥ 80)
# def d(m,n):
#     if m%n==0:
#         return True
#     else:
#         return False
# for A in range(1,100):
#     f=1
#     for x in range(1,100):
#         if ((d(x,2)<=(not d(x,3))or (x+A>=80)))==0:
#             f=0
#     if f==1:
#         print(A)

# def d(m,n):
#     if m%n==0:
#         return True
#     else:
#         return False
# for A in range(1,100):
#     f=1
#     for x in range(1,100):
#         if (d(x,A)or ((39<x<51)<=(not d(x,12))))==0:
#             f=0
#     if f==1:
#         print(A)