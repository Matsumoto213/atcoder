N,M = map(int, input().split())
ans = 0

if N * 2 <= M:
    ans += N
    M -= (N * 2)
    ans += (M // 4)
else:
    ans += (M // 2)

print(ans)