def judge():
    for row2 in range(H):
        for row1 in range(row2):
            for col2 in range(W):
                for col1 in range(col2):
                    if A[row1][col1] + A[row2][col2] > A[row2][col1] + A[row1][col2]:
                        return False
    return True


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

print("Yes" if judge() else "No")