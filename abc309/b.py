N = int(input())
a = []

for i in range(N):
    a.append(list(input()))
ans = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0:
            if j == 0:
                ans[i][j] = a[i + 1][j]
            else:
                ans[i][j] = a[i][j - 1]
        elif i == N - 1:
            if j == N - 1:
                ans[i][j] = a[i - 1][j]
            else:
                ans[i][j] = a[i][j + 1]
        else:
            if j == N - 1:
                ans[i][j] = a[i - 1][j]
            elif j == 0:
                ans[i][j] = a[i + 1][j]
            else:
                ans[i][j] = a[i][j]
for i in range(N):
    for j in range(N):
        print(ans[i][j], end = "")
    print()

