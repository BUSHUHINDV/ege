b=input()
s2=0
for i in range(1, len(b), 2):
    s2 += int(b[i])
#if abs(s1 - s2) == 13:
print(s2)