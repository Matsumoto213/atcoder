N,k = map(int, input().split())
S = [list(input()) for _ in range(N)]
from collections import Counter
from itertools import product
print(S)
ans = 0

# 全探索
for pro in product((0, 1), repeat = N):
    t = []
    for i, p in enumerate(pro):
        if p:
            t.extend(S[i])
    print(t)

