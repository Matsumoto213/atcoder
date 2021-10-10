n = int(input())
dp = [[0]*3 for _ in range(n+1)]


dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, n + 1):
    a,b,c = map(int, input().split())
    dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][2] + a)
    dp[i][1] = max(dp[i - 1][1] + b, dp[i - 1][2] + b)
    dp[i][2] = max(dp[i - 1][1] + c, dp[i - 1][1] + c)
print(max(dp[-1]))