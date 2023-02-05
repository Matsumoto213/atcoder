N = int(input())
A = list(map(int, input().split()))
A.sort()
mod = 10 ** 9 + 7
ans = 1
for i in range(N):
    ans *= A[i] - i
    ans %= mod
print(ans)