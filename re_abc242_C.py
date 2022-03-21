MOD = 998244353
N = int(input())
dp = [[0] * 9 for _ in range(N)]
dp[0] = [1] * 9

for i in range(1, N):
    for j in range(9):
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
        
        dp[i][j] += dp[i - 1][j]

        if j + 1 < 9:
            dp[i][j] += dp[i - 1][j + 1]
        
        dp[i][j] %= MOD
print(sum(dp[N - 1]))