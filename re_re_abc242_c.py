N = int(input())

mod = 998244353

dp = [[0] * 9 for _ in range(N)]
dp[0] = [1] * 9

for i in range(1,N):
    for d in range(9):
        if d > 0:
            dp[i][d] += dp[i - 1][d - 1]
        
        dp[i][d] += dp[i - 1][d]

        if d + 1 < 9:
            dp[i][d] += dp[i - 1][d + 1]
        
        dp[i][d] %= mod
print(sum(dp[N - 1]) % mod)