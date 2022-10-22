N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
ab = defaultdict(list)

for i in range(N):
    Int = i +  1
    ab[A[i]].append(Int * 2)
    ab[A[i]].append(Int * 2 + 1)
for i in range(2 * N + 1):
    if i == 0:
        print(0)
    else:
        cnt = 0
        ans = i + 1
        for j in range(len(ab)): 
            for key,value in ab.items():
                if i in value:
                    ans = key
                    cnt += 1
                    if ans == 1:
                        break
        print(cnt)