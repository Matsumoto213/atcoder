def max_binary_under_n(S, N):
    S = S[::-1]
    L = len(S)
    dp = [[[-1]*2 for _ in range(61)] for _ in range(L+1)]
    dp[0][0][0] = 0
    
    for i in range(L):
        for j in range(60):
            for k in range(2):
                if dp[i][j][k] == -1:
                    continue
                for b in range((2 if S[i]=='?' else 1)):
                    ni, nj, nk = i+1, j, k
                    if S[i]=='?' and b==1 or S[i]=='1':
                        nj += 1
                    if k==0 and ((N>>j)&1) < (b if S[i]=='?' else int(S[i])):
                        nk = 1
                    dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (b<<j))
    return max(dp[i][j][k] for i in range(L+1) for j in range(60) for k in range(2) if dp[i][j][k] != -1)