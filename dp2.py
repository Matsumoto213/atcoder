N,K = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] * N
dp[0] = 0

for i in range(1, N):
    temp = []
    for m in range(max(0, i - K), i):
        temp.append(abs(h[m] - h[i] ) + dp[m])
    dp[i] = min(temp)
print(dp[N - 1])