H,W = map(int, input().split())
L = []

for i in range(H):
    mass = list(map(int, input().split()))
    L.append(mass)

h = []
w = []
for i in range(H):
    height = []
    temp = 0
    for j in range(W):
        temp += L[i][j]
    w.append(temp)

for i in range(W):
    temp = 0
    for j in range(H):
        temp += L[j][i]
    h.append(temp)

for i in range(H):
    for j in range(W):
        print(w[i] + h[j] - L[i][j], end = " ")
    print()