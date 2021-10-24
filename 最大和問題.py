# dpでやってみる
# n = int(input())
# a = list(map(int, input().split()))
n = 3
a = [7,-6,9]
x = n + 1
dp = [0] * x


def main():
    for i in range(n):
        dp[i + 1] = max(dp[i],dp[i] + a[i])
    print(dp[n])


if __name__ == '__main__':
    main()