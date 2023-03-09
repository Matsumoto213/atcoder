N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import defaultdict
ab = defaultdict(list)

for i in range(N):
    for j in range(A[i],B[i] + 1):
        if j not in ab:
            ab[j] = 1
        else:
            ab[j] += 1

ans = list(ab.values())
print(ans.count(N))