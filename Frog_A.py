n = int(input())
h = list(map(i t, input().split()))


# DP配列を用意する
# dp[i]にはi番目の足場にたどり着くために必要な最低コストを入れる

dp = [0]*n

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2,n):
    # iを現在いる足場と捉える
    # i番目の足場へ行く方法としてi - 1 からのジャンプとi - 2 ばんめのジャンプがある
    # 2通りの生き方のうちコストの少ない方をdp[i]とする

    dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]),dp[i - 1] + abs(h[i] - h[i - 1]))
print(dp)