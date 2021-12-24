N,K = map(int, input().split())
T = []

t = [i for i in range(1, N + 1)]
i = 0
n = 0

while True:
    if i == N:
        break
    t[i] *= 2
    n += 1
    if t[i] >= K:
        T.append(n)
        i += 1
        n = 0
ans = 0
temp = 1 / N
for i in range(N):
    ans += temp * (0.5) ** T[i]
print(ans)
