N,M = map(int, input().split())
from collections import defaultdict

wa = defaultdict(int)
l = set()
pena = 0
ac = 0
for i in range(M):
    p,s = input().split()
    p = int(p)

    if s == 'WA':
        wa[p] += 1
    else:
        if p not in l:
            pena += wa[p]
            ac += 1
            l.add(p)
print(ac, pena)