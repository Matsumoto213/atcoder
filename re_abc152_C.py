N = int(input())
P = list(map(int, input().split()))
mi = 10 ** 8
ans = 0

for i in range(N):
    mi = min(mi,P[i])
    if mi == P[i]:
        ans += 1
print(ans)