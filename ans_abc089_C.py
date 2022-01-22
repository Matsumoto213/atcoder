from collections import Counter
from itertools import combinations
n = int(input())
s = [input()[0] for _ in range(n)]
c = Counter(s)
l = []

for i in "MARCH":
  if i in c:
    l.append(c[i])

ans = 0
for a,b,c in combinations(l,3):
    print(a,b,c)
    ans += a*b*c
print(ans)