n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2,n):
    dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]),dp[i - 1] + abs(h[i] - h[i - 1]))
print(dp[-1])
