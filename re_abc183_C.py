N,K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

import itertools
l = []
for i in range(2,N + 1):
    l.append(i)

L = itertools.permutations(l,N - 1)

ans = 0
for city in L:
    city = [1]+list(city)+[1]
    temp = 0
    for j in range(len(city) - 1):
        temp += T[city[j] - 1][city[j + 1] - 1]
    
    if temp == K:
        ans += 1
        
print(ans)  
        
        
        
            