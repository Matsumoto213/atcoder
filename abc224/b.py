H,W = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(H)]

for i1 in range(H-1):
    for i2 in range(i1+1,H):
        for j1 in range(W-1):
            for j2 in range(j1+1,W):
                print(i1,i2,j1,j2)
                print(L[i1][i2],L[i2][j2],L[i2][j1],L[i1][j2])
