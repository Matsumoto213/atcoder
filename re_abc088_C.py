C = []
N = 3
for _ in range(N):
    s = list(map(int, input().split()))
    C.append(s)
cal = []

def judge():
    for i in range(N):
        for j in range(N - 1):
            if i == 0:
                temp = C[i][j] - C[i][j + 1]
                cal.append(temp)
            else:
                if C[i][j] - C[i][j + 1] != cal[j]:
                    return False
            
    return True

print('Yes' if judge() else 'No')
    