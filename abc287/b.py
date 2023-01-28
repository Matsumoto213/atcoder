N,M = map(int, input().split())
S = [input() for i in range(N)]
T = [input() for j in range(M)]
ans = 0
for i in range(N):
    temp = S[i][3:]
    if temp in T:
        ans += 1
print(ans)