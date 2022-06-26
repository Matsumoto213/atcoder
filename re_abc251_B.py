N,W = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict
cnt = defaultdict(int)

A.sort()
ans = 0

if N == 1:
    print(1)
    exit(0)

if N == 2:
    for i in range(N):
        temp = A[i]
        if temp > W:
            break
        else:
            cnt[temp] += 1
            temp += A[i + 1]
            if temp <= W:
                cnt[temp] += 1    
else:
    for i in range(N - 2):
        temp = A[i]
        if temp > W:
            break
        else:
            cnt[temp] += 1
            temp += A[i + 1]
            if temp <= W:
                cnt[temp] += 1
                temp += A[i + 2]
                if temp <= W:
                    cnt[temp] += 1
            else:
                continue
print(cnt)



