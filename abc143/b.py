N = int(input())
d = list(map(int, input().split()))

ans = 0

import itertools
a = [i for i in range(1, N + 1)]
for v in itertools.combinations(a, 2):
    v = list(v)
    ans += d[v[0] - 1] * d[v[1] - 1]
print(ans)