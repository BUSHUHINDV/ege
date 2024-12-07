# def f1(n):
#     if n==10:
#         return 1
#     if n > 10:
#         return 0
#     if n<10:
#         return f1(n+1)+f1(n*2)
# def f2(n):
#     if n==21:
#         return 1
#     if n > 21:
#         return 0
#     if n<21:
#         return f2(n+1)+f2(n*2)
# print(f1(1)*f2(10))
# def f(n):
#     if n==10:
#         return 1
#     if n>10:
#         return 0
#     return f(n+1)+f(n*2)
#
# def f2(n):
#     if n==35:
#         return 1
#     if n>35 or n==17:
#         return 0
#     return f2(n + 1) + f2(n * 2)
# print(f(1)*f(10))

def f(n):
    if n==1:
        return 1
    if n<1 or n==12:
        return 0
    return f(n-2)+f(n//2)
print(f(26))