N = int(input())
C = list(map(int, input().split()))
mod = 10 ** 9 + 7
C.sort()
ans = 1

for i in range(N):
    if C[i] - i == 0:
        print(0)
        exit()
    ans *= C[i] - i
    ans %= mod
print(ans)