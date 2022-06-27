N = int(input())
L = list(map(int, input().split()))

import itertools
ans = 0

for v in itertools.combinations(L, 3):
    v = list(v)
    v.sort()
    if len(set(v)) == len(v) and v[0] + v[1] > v[2]:
        ans += 1
print(ans)