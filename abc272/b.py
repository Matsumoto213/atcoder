N,M = map(int, input().split())

import itertools
L = []
for i in range(1,N + 1):
    L.append(i)

l = {}
for v in itertools.combinations(L,2):
    l[v] = False

for i in range(M):
    L = list(map(int, input().split()))
    k = L[0]
    x = L[1:]
    for v in itertools.combinations(x,2):
        l[v] = True


for i in l:
    if l[i] != True:
        print('No')
        exit()

print('Yes')