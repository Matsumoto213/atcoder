N,M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

import bisect
B.sort()
ans = 10 ** 15 + 7
for i in range(N):
    idx = bisect.bisect_left(B, A[i])
    if idx == 0:
        temp = abs(B[idx] - A[i])
    elif idx == M:
        temp = abs(B[idx - 1] - A[i])
    else:
        temp = min(abs(B[idx] - A[i]),abs(B[idx - 1] - A[i]))
    ans = min(temp,ans)
print(ans)