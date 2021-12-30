import itertools
N, K = map(int,input().split())
T=[list(map(int,input().split())) for _ in range(N)]

nums = list(range(1,N))
ans = 0
print(T)
for idx in itertools.permutations(nums):
    idx = [0] + list(idx)
    time = 0
    for i in range(N):
        ti = T[idx[i]][idx[(i + 1) % N]]
        time += ti
    if time == K:
        ans += 1
print(ans)
        
    