N,Q = map(int, input().split())
a = list(map(int, input().split()))
from collections import defaultdict
C = defaultdict(list)

for i in range(N):
    C[a[i]].append(i)
for _ in range(Q):
    x,k = map(int, input().split())
    if len(C[x]) < k:
        print(-1)
    else:
        print(C[x][k - 1] + 1)