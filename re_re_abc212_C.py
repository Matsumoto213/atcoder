N,M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
import bisect
b.sort()

ans = 10 ** 15 + 7

for i in range(N):
    idx = bisect.bisect_left(b, a[i])
    if idx == 0:
        temp = abs(a[i] - b[idx])
    elif idx == M:
        temp = abs(a[i] - b[idx - 1])
    else:
        temp = min(abs(a[i] - b[idx]),abs(a[i] - b[idx - 1]))
    ans = min(temp,ans)
print(ans)
