N,K = map(int, input().split())
ans = [0] * N
for i in range(K):
    D = int(input())
    L = list(map(int, input().split()))
    for j in L:
        ans[j - 1] += 1

print(ans.count(0))