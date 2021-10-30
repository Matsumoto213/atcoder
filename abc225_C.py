N,M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]

lst = [[]*N for _ in range(M)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            lst[i][j] = B[0][0]
        elif j == 0:
            lst[i][j] = lst[i - 1][j] + 7
        else:
            lst[i][j] = lst[i][j - 1] + 1

if lst == B:
    print("Yes")
else:
    print("No")

