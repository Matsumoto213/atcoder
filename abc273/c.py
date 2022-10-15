N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
ab = defaultdict(list)
l = set()
for i in range(N):
    l.add(A[i])

l = list(l)
l.sort()
temp = len(l)

if N == 1:
    print(1)
    exit()

for i in range(N - 1):
    t = l.index(A[i])
    tem = temp - t - 1
    ab[tem] = A[i]


for i in range(N):
    print(A.count(ab[i]))