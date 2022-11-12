H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
for i in range(H - 1):
    for j in range(i + 1,H):
        for k in range(W - 1):
            for l in range(k + 1,W):
                # print(i,j,k,l)
                # print(A[i][j],A[j][l],A[j][k],A[i][l])
                if A[i][k] + A[j][l] > A[j][k] + A[i][l]:
                    print('No')
                    exit()
print('Yes')