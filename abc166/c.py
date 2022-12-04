N,M = map(int, input().split())
H = list(map(int, input().split()))

from collections import defaultdict
ab = defaultdict(set)

for _ in range(M):
    a,b = map(int, input().split())
    ab[a].add(b)
    ab[b].add(a)
ans = 0
for i in range(N):
    judge = True
    for j in ab[i + 1]:
        if H[i] <= H[j - 1]:
            judge = False
    if judge:
        ans += 1
print(ans)