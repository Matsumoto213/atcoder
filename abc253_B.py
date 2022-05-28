H,W = map(int, input().split())
S = [input() for _ in range(H)]

# 最小の値を出さなければならない
mi_ = 10 ** 15
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            if cnt == 0:
                temp_i = i
                temp_j = j
            else:
                dif = abs(temp_i - i) + abs(temp_j - j)
                mi_ = min(mi_,dif)
                temp_i = i
                temp_j = j
            cnt += 1
print(mi_)