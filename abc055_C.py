n = int(input())
mod = 10 ** 9 + 7

ans = 1
for i in range(1,n + 1):
    ans *= i
    ans = ans % mod
print(ans)

