N, M, X = map(int,input().split())
C = list()
A = list()
for i in range(N):
    CA = list(map(int,input().split()))
    C.append(CA[0])
    A.append(CA[1:])
ans = 10 ** 11
for i in range(2 ** N):
    judge = [0] * M
    money = 0
    for j in range(N):
        if i & (1 << j):
        # if ((i >> j) & 1):
            money += C[j]
            for m in range(M):
                judge[m] += A[j][m]

    # 全て超えているかを確かめるためには一番小さい数字のみを見ればいい
    if min(judge) >= X:
        ans = min(ans,money)

print(-1 if ans == 10 ** 11 else ans)