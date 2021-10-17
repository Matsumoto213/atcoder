# 動的計画法

n = int(input())
a = []

for i in range(2):
    a.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(2)]


# 初期値として最初のマスを設定
dp[0][0] = a[0][0]

for i in range(1,n):
    dp[0][i] = dp[0][i - 1] + a[0][i]

dp[1][0] = a[0][0] + a[1][0]

for i in range(1,n):
    dp[1][i] = max(dp[1][i - 1],dp[0][i]) + a[1][i]
print(dp[1][n - 1])