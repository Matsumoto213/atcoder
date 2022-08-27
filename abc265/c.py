H,W = map(int, input().split())

G = [input() for _ in range(H)]
i,j = 0,0
cnt = 0
position = [[False] * W] * H
position[i][j] = True
while(1):
    if G[i][j] == 'U' and i != 0:
        i -= 1
        if position[i][j]:
            cnt += 1
        else:
            position[i][j] = True
    elif G[i][j] == 'D' and i != H - 1:
        i += 1
        if position[i][j]:
            cnt += 1
        else:
            position[i][j] = True
    elif G[i][j] == 'L' and j != 0:
        j -= 1
        if position[i][j]:
            cnt += 1
        else:
            position[i][j] = True
    elif G[i][j] == 'R' and j != W - 1:
        j += 1
        if position[i][j]:
            cnt += 1
        else:
            position[i][j] = True
    else:
        break
    if cnt > H * W:
        print(-1)
        exit(0)
print(i + 1,j + 1)