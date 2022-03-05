N,M = map(int, input().split())
from collections import defaultdict

penalty = 0
ans = defaultdict(int)
dct = defaultdict(int)

# 例外処理をきちんと書く
for i in range(M):
    PS = input().split()
    p = int(PS[0])
    s = PS[1]

    if s == "WA":
        dct[p] += 1
    else:
        ans[p] += 1
        penalty += dct[p]

print(len(ans), penalty)