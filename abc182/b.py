from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
dct = defaultdict(int)
for i in range(2,max(A) + 1):
    num = 0
    for j in range(N):
        if A[j] % i == 0:
            num += 1
    dct[i] = num
ans = sorted(dct.items(), key=lambda x:x[1],reverse = True)
print(ans[0][0])