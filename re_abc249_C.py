import itertools
import collections
 
N,K = map(int,input().split())
S = [input() for _ in range(N)]
ans = 0

for i in range(K,N + 1):
    l = list(itertools.combinations(range(N),i))
    for s in l:
        wk = []
        for tar in s:
            wk += list(S[tar])
        c = collections.Counter(wk)
        wkans = 0
        for key,val in c.items():
            if val == K:
                wkans += 1
        ans = max(ans,wkans)
print(ans)