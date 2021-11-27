# dp方の練習をします　

N,W = map(int, input().split())
w = []
v = []

for i in range(N):
    a,b = map(int, input().split())
    w.append(a)
    B.append(b)

dp = [[0]*(W + 1) for j in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])
print(dp[N][W])
            