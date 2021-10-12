n,m = map(int, input().split())
a = [int(input()) for _ in range(m)]

mod = 10 ** 9 + 7
dp = [0]* n + 1
dp[0] = 1


for i in a:
    dp[i] = -1


for i in range(n):
    if dp[i] == -1:
        continue
    
    if dp[i + 1] != -1:
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod

    
    if i + 2 <= n:
        if dp[i + 2] != -1:
            dp[i + 2] += dp[i]
            dp[i + 2] %= mod
print(dp)
print(dp[-1])
