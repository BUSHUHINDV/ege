ans = []
for x in range(1000000, 10000000):
    xs = list(map(int, str(x)))
    if xs[0]**2 == xs[1]*10 + xs[2]:
        if 0 <= xs[-1]**3 <= 9 and xs[-1]**3 == xs[-2] or \
             9 < xs[-1]**3 < 100 and xs[-1]**3 == xs[-3]*10 + xs[-2] or \
             xs[-1]**3 >= 100 and xs[-1]**3 == xs[-4]*100 + xs[-3]*10 + xs[-2]:
            ans.append(x)
print(len(ans))