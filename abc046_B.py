n,k = map(int, input().split())

ans = 0
idx = 0

for i in range(n):
    if idx == 0:
        ans += k
    else:
        ans *= k - 1
    idx += 1
print(ans)
