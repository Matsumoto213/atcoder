# 途中の計算結果をうまく再利用する
max_n = 1000
max_w = 5000
n, w = map(int, input().split())


# dp[i][j]はi番目以降の品物から重さの和がj以下なるように選んだときの価値の和の最大値を表す。
def solve_dp2():
    for i in range(w + 1):
        # 初期値を設定する
        dp[n][j] = 0
    
    for i in range(n - 1, 0, -1):
        for j in range(w + 1):
            if j < w[i]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
    print(dp[0][w])

