N,W = map(int, input().split())
w = []
v = []


dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    x,y = map(int,input().split())
    w.append(x)
    v.append(y)

for i in range(N):
    for j in range(W + 1):
        # 選ばない時
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        # 選ぶ時
        else:
            dp[i + 1][j] = max(dp[i][j],dp[i][j - w[i]] + v[i])


