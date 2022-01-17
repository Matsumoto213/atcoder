n,s = map(int, input().split())

l = []
for i in range(1, n + 1):
    l.append(i)

ans = 0
for i in range(n):
    for j in range(n):
        temp = l[i] + l[j]
        if temp <= s:
            ans += 1
print(ans)