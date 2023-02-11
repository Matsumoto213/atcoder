def count_subsets(N, M, C, S):
    bit = 1 << M
    cnt = [0] * (N + 1)
    for i in range(M):
        for j in S[i]:
            cnt[j] += 1
    dp = [0] * bit
    dp[0] = 1
    for i in range(1, bit):
        t = i
        j = 0
        flag = True
        while t > 0:
            if t & 1:
                # 修正箇所
                k = cnt[j+1]
                if k == 0:
                    # 集合がないのでループを抜ける
                    flag = False
                    break
                dp[i] += dp[i ^ (1 << j)]
            t >>= 1
            j += 1
        if not flag:
            dp[i] = 0
    ans = dp[bit - 1]
    return ans

N,M = map(int, input().split())
C = []
S = []
for i in range(M):
    c = int(input())
    c_list = list(map(int, input().split()))
    C.append(c)
    S.append(c_list)
print(count_subsets(N, M, C, S))