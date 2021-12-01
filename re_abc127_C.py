import collections
N,M = map(int, input().split())

L = 0
R = N
for _ in range(M):
    li, ri = map(int, input().split())
    L = max(li, L)
    R = min(ri, R)

print(max(R - L + 1), 0)