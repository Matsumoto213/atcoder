N,k = map(int, input().split())
S = [input() for i in range(N)]
import itertools
from collections import Counter

ma = - 10 ** 9
for i in range(N):
    for v in itertools.permutations(S,i + 1):
        C = Counter()
        ans = 0
        v = list(v)
        for l in v:
            C += Counter(l)
        val = list(C.values())
        ma = max(val.count(k),ma)
print(ma)