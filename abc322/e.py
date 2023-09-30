N, K, P = map(int, input().split())

# 費用と各パラメータの値を格納するリストを初期化
plans = [(0, [0] * K)] + [(int(input().split()[0]), list(map(int, input().split()))) for _ in range(N)]

INF = float('inf')
dp = [[INF] * (1 << K) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    dp[i] = dp[i - 1].copy()
    cost, values = plans[i]
    for s in range(1 << K):
        ns = s
        for j in range(K):
            if (s >> j) & 1:
                continue
            ns |= 1 << j
            if values[j] >= P:
                break
        dp[i][ns] = min(dp[i][ns], dp[i - 1][s] + cost)

ans = min(dp[i][(1 << K) - 1] for i in range(N + 1))
print(ans if ans != INF else -1)
