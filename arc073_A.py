N, T = map(int,input().split())
t = list(map(int,input().split()))

ans = N * T

for i in range(N - 1):
    t[i] += T
    if t[i] > t[i + 1]:
        ans -= t[i] - t[i + 1]
print(ans)