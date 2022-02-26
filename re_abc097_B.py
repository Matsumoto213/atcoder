x = int(input())

A = set()

for a in range(1, 32):
    for b in range(2,101):
        if a ** b <= x:
            A.add(a ** b)
        else:
            break

a = list(sorted(A))
print(a[-1])