N = int(input())
L = [input() for _ in range(N)]
print()
flag = False

for i in range(N):
    for j in range(N - 6 + 1):
        # 横の条件式
        weight = L[i][j:j + 6]
        we = weight.count('#')
        
        if we >= 4:
            flag = True
            break

# 横の条件式
for i in range(N - 6 + 1):
    for j in range(N):
        mass = []
        for k in range(6):
            mass.append(L[k][i])
        if mass.count('#') >= 4:
            flag = True
            break






print('Yes' if flag else 'No')

