H,W = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(H)]
ans = [[0 for _ in range(W)] for _ in range(H)]

sum_row = []
sum_line = []
line = list(zip(*L))

for i in range(H):
    sum_row.append(sum(L[i]))

for j in range(W):
    sum_line.append(sum(line[j]))

for i in range(H):
    for j in range(W):
        print(sum_row[i] + sum_line[j] - L[i][j], end = " ")
    print()