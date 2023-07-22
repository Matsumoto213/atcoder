H,W = map(int, input().split())
S = [input() for _ in range(H)]

first_i = 10 ** 8
fisrt_j = 10 ** 8
last_i = -10 ** 8
last_j = -10 ** 8

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            first_i = min(first_i,i)
            fisrt_j = min(fisrt_j,j)
            last_i = max(last_i,i)
            last_j = max(last_j,j)   

for i in range(first_i,last_i + 1):
    for j in range(fisrt_j,last_j + 1):
        if S[i][j] == '.':
            print(i + 1,j + 1)