N = int(input())
A = list(map(int, input().split()))
N = len(A)
A = [0] + A + [0]
l = [0] * (N + 2)
r = [0] * (N + 2)
for i in range(1, N + 1):
    l[i] = min(l[i - 1] + 1, A[i])

for i in range(N, 0, -1):
    r[i] = min(r[i + 1] + 1, A[i])
    
ans = 0
for i in range(1, N + 1):
    ans = max(ans, min(l[i], r[i]))

print(ans)