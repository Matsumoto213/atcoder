N,M = map(int, input().split())
import itertools
L = []

for i in range(1, M + 1):
    L.append(i)

def judge(L):
    for i in range(N - 1):
        if L[i + 1] < L[i]:
            return False
    return True

ans = 0
for v in itertools.combinations(L, N):
    v = list(v)
    if judge(v):
        print(*v)