'''s='1'*81
while ('11111' in s) or ('888' in s):
    if '11111' in s:
        s =s.replace('11111','88',1)
    else:
        s = s.replace('888', '8', 1)
    print(s)
print(s)
'''

# s='9'*81
# while ('33333' in s) or ('999' in s):
#     if '33333' in s:
#         s=s.replace('33333','99',1)
#     else:
#         s = s.replace('999','3',1)
# print(s)
for n in range(3,10000):
    s='1'+'8'*n
    while ('18' in s) or ('388' in s) or ('888' in s):
        if '18'in s:
            s=s.replace('18','8',1)
        if '388'in s:
            s=s.replace('388','81',1)
        if '888'in s:
            s=s.replace('888','3',1)
    if s.count('1') == 3:
        print(n)
        break