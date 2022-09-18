S = [input() for _ in range(10)]
cnt = 0
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            if cnt == 0:
                A = i + 1
                C = j + 1
            B = i + 1
            D = j + 1
            cnt += 1

print(A,B)
print(C,D)
