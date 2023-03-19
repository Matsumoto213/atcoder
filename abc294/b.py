H,W = map(int, input().split())
A = [input().split() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == '0':
            print('.', end = "")
        else:
            temp = int(A[i][j])
            print(chr(temp + 64), end = "")
    print()