def solution():
    C = [list(map(int, input().split())) for _ in range(3)]
    L = [C[0][0] - C[0][1],C[0][1] - C[0][2]]
    
    for i in range(1,3):
        for j in range(2):
            if j == 0:
                if C[i][j] - C[i][j + 1] != L[0]:
                    return False
            else:
                if C[i][j] - C[i][j + 1] != L[1]:
                    return False
    return True

print("Yes" if solution() else "No")