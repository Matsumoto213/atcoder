N = int(input())
A = list(map(int, input().split()))

from collections import Counter

def fac(n):
    m = 0
    for i in range(1, n):
        m += i
    return m


l = Counter(A)
key = l.values()

ans = 0
for a in key:
    ans += fac(a)
print(ans)
