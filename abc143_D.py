import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        p = L[i]
        q = L[j]
        x = bisect.bisect_left(L, p + q)
        ans += x - j - 1
print(ans)