N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]

H.sort()

ans = 10000000000

for i in range(N - K + 1):
    n = H[i + K - 1] - H[i]
    ans = min(n,ans)
print(ans)