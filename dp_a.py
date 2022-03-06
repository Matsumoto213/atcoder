n = int(input())
h = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(h[0] - h[1])


for i in range(2, n):
    dp[i] = min(dp[i - 1] + (h[i] + h[h - 1]), dp[i - 2] + (h[i]) - h[i - 2])
print(dp[-1])