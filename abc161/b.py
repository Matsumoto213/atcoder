N,M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    temp = sum(A) / (4 * M)
    if A[i] >= temp:
        ans += 1
    
    if ans >= M:
        print('Yes')
        exit()
print('No')