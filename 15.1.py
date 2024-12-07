'''
ДЕЛ(A, 5) ∧ (¬ДЕЛ(2020, A) → (ДЕЛ(x, 1718) → ДЕЛ(2023, A)))
'''
def ДЕЛ(a, b):
    if a%b==0:
        return True
    else:
        False
e=1
for A in range(1,7):
    e=1
    for x in range(1,5000):
        if ДЕЛ(A, 5) and ((not ДЕЛ(2020, A)) <= (ДЕЛ(x, 1718) <= ДЕЛ(2023, A))):
            o=1
        else:
            e=0
    print(A)
