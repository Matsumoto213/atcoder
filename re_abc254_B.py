N = int(input())
L = [[0] * (i + 2) for i in range(N)]

for i in range(N):
    for j in range(i + 2):
        if j == i + 1:
            L[i][j] = 0
        elif j == 0:
            L[i][j] = 1
        else:
            L[i][j] = L[i - 1][j - 1] + L[i - 1][j]

for i in range(N):
    for j in range(i + 1):
        print(L[i][j], end = " ")
    print()