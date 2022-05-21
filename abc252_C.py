N = int(input())
S = [input() for _ in range(N)]
L = []
for i in range(10):
    ma = -10 ** 15
    for j in range(N):
        i = str(i)
        ma = max(S[j].index(i),ma)
    if i == str(ma):
        ma += 10 * N - 10
    L.append(ma)
print(min(L))
