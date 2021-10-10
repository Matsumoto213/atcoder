n,k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0]*n
dp[0] = 0

for i in range(1,n):
    # iを現在いる足場と考える
    # i番目の足場へ行く方法はmax(k, i - k)通りある
    temp = []
    for m in range(max(0, i - k), i):
        temp.append(abs(h[m] - h[i] ) + dp[m])
    dp[i] =min(tmp)
print(dp[-1])
