N,M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

G = [[] for _ in range(M)]

count = [0] * (M + 1)
for i in range(N):
    G[C[i] - 1].append(S[i])

for i in range(N):
    if count[C[i]] == 0:
        print(G[C[i] - 1][-1], end = "")
    else:
        print(G[C[i] - 1][count[C[i]] - 1],end = "")
    count[C[i]] += 1
print()