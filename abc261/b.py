N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (A[i][j] == 'W' and (A[j][i] == 'W' or A[j][i] == 'D')) or (A[i][j] == 'D' and (A[j][i] == 'W' or A[j][i] == 'L')) or (A[i][j] == 'L' and (A[j][i] == 'D' or A[j][i] == 'L')) or (A[i][j] == '-' and (A[j][i] == 'D' or A[j][i] == 'L' or A[j][i] == 'W')):
            print('incorrect')
            exit()

print('correct')