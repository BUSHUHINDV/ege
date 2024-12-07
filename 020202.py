#(x ≡ ¬y) → ((x ∧ w) ≡ z)
print('x y z w')
for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    if not((x == (not y)) <= ((x and w) == z)):
                        print (x, y, z, w, (x == (not y)) <= ((x and w) == z))