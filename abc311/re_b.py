N,D = map(int, input().split())
S = [list(input()) for _ in range(N)]

free = [True] * D
for i in range(N):
    for j in range(D):
        if S[i][j] == 'x':
            free[j] = False

ans = 0
consecutive = 0
for i in range(D):
    if free[i]:
        consecutive += 1
    else:
        ans = max(ans,consecutive)
        consecutive = 0

    # 末尾まで#がないケース
    if i == D - 1:
        ans = max(ans,consecutive)

print(ans)
