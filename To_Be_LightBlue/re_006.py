N = int(input())
S = input()

ans = 0
for i in range(1000):
    ln = S
    password = str(i).zfill(3)
    a = password[0]
    b = password[1]
    c = password[2]

    if a in ln:
        idx_a = ln.index(a)
    else:
        continue

    if b in ln[idx_a + 1:]:
        idx_b = ln[idx_a + 1:].index(b)
    else:
        continue

    if c in ln[idx_a + idx_b + 2:]:
        ans += 1
    else:
        continue
print(ans)