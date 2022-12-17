N,M = map(int, input().split())
s = [input() for _ in range(N)]
L= []
for i in range(N):
    L.append(i)

import itertools
ans = 0
for key,value in itertools.combinations(L, 2):
    ans_num = 0
    for j in range(M):
        if s[key][j] == 'o' or s[value][j] == 'o':
            ans_num += 1
    if ans_num == M:
        ans += 1
print(ans)