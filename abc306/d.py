def solve(N, dishes):
    # dp[i][j] は i 番目の料理までで、j 回毒を飲んだときの美味しさの総和の最大値
    dp = [[-1e18] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        x, y = dishes[i]
        for j in range(i + 1):
            if dp[i][j] == -1e18:
                continue
            # 下げてもらう場合
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            # 食べる場合
            if x == 1:
                # 毒を飲む場合
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + y)
            else:
                # 解毒剤を飲む場合
                dp[i + 1][max(j - 1, 0)] = max(dp[i + 1][max(j - 1, 0)], dp[i][j] + y)

    # 美味しさの総和の最大値を求める
    max_deliciousness = max(dp[N])

    return max_deliciousness

N = int(input())
dishes = [list(map(int, input().split())) for _ in range(N)]
print(solve(N, dishes))
