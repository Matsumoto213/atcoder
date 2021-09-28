def main():
    mod = 998244353

    N = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * 10 for _ in range(N)]
    dp[0][A[0]] = 1
    
    for i in range(1, N):
        for j in range(10):
            f = (j + A[i]) % 10  # 一番左のjと、二番目に左のA[i]に操作Fをしたとき、新たに一番左になる数字
            g = (j * A[i]) % 10  # 操作G
            dp[i][f] += dp[i - 1][j]
            dp[i][g] += dp[i - 1][j]
            dp[i][f] %= mod
            dp[i][g] %= mod
    
    for i in range(10):
        print(dp[N - 1][i])

if __name__ == '__main__':
    main()