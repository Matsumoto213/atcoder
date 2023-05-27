X,Y,Z = map(int, input().split())
S = input()

def min_time_to_type(X, Y, Z, S):
    N = len(S)
    # DPテーブルの初期化
    dp = [[float('inf')] * 2 for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(2):
            # aキーのみを押す場合
            if (S[i] == 'a' and j == 0) or (S[i] == 'A' and j == 1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + X)
            # Shiftキーとaキーを同時に押す場合
            if (S[i] == 'A' and j == 0) or (S[i] == 'a' and j == 1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + Y)

            # CapsLockキーを押す場合
            dp[i][1-j] = min(dp[i][1-j], dp[i][j] + Z)

    # 最小の時間を返す
    return min(dp[N])

print(min_time_to_type(X, Y, Z, S))