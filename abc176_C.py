N = int(input())
A = list(map(int, input().split()))
ans = 0
ma = A[0]

for i in range(1, N):
    
    if A[i - 1] > A[i]:
        ans += A[i - 1] - A[i]
        A[i] = A[i - 1]
    else:
        ma = A[i]
print(ans)