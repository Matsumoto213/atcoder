k,s = map(int,input().split())
L = [i for i in range(k + 1)]

ans = 0
for a in range(k + 1):
    if a + k + k < s:
        continue

    for b in range(k + 1):
        if a + b + k < s:
            continue
        c = abs(s - a - b)

        if c > k:
            continue
        
        if a + b + c == s:
            ans += 1
print(ans)

