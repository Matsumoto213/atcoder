from collections import defaultdict
N,M = map(int, input().split())
dct = defaultdict(int)
for i in range(N):
    a,b = map(int, input().split())
    dct[a] += b

d = sorted(dct.items(), key=lambda x:x[0])
ans = 0
for key,value in d:
    min_ = min(M,value)
    ans += key * min_
    M -= min_
    
    if M == 0:
        break
    
print(ans)