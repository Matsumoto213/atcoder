# 正答数とペナルティ数も答える
N,M = map(int, input().split())
from collections import defaultdict
WA = defaultdict(int)
AC = defaultdict(int)
for _ in range(M):
    L = input().split()
    p = int(L[0])
    s = L[1]
    if s == "AC":
        AC[p] = 1
    else:
        if AC[p] == 0:
            WA[p] += 1
    
ans = len(AC)
penalty = sum(WA.values())
print(ans,penalty)