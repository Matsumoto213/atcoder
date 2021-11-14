N,M = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    a,b = map(int, input().split())
    ans = (sum(A[a - 1:b])) // len(A[a - 1:b])
    result = abs(ans - M)
    if ans < M:
        for j in range(a - 1,b):
            A[j] += result
print(*A)
