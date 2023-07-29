def solve(S):
    MOD = 998244353
    n = len(S)
    dp = [[0] * (n+2) for _ in range(n+2)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(i+2):
            if S[i] in {'(', '?'}:
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % MOD
            if S[i] in {')', '?'} and j > 0:
                dp[i+1][j-1] = (dp[i+1][j-1] + dp[i][j]) % MOD
    return dp[n][0]

S = input()
print(solve(S))