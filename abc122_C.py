N,Q = map(int, input().split())
S = input()
L = []
for i in range(N - 1):
    if S[i: i + 2] == 'AC':
        L.append(i + 1)

import bisect
for _ in range(Q):
    l,r = map(int, input().split())
    a = bisect.bisect_left(L,l)
    b = bisect.bisect_left(L,r)
    print(b - a)