# ランレングス圧縮
from itertools import groupby
S = [(k, len(list(g))) for k, g in groupby(list(input()))]
T = [(k, len(list(g))) for k, g in groupby(list(input()))]

if len(S) != len(T):
    print('No')
    exit()

for (s, m), (t, n) in zip(S, T):
    print(s,m,t,n)
    if not (s == t and (m == n == 1 or 1 < m <= n)):
        print('No')
        exit()
print('Yes')