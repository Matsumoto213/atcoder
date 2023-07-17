N,M = map(int, input().split())
P = []
C = []
F = []
for i in range(N):
    # p:値段 c:機能 *f:機能の詳細
    p,c,*f = map(int, input().split())
    P.append(p)
    C.append(c)
    F.append(f)

judge = False
for i in range(N):
    for j in range(N):
        if P[j] <= P[i]:
            inOrOut = True
            for k in range(C[i]):
                if F[i][k] not in F[j]:
                    inOrOut = False
            if inOrOut and ((P[j] < P[i]) or (len(F[i]) < len(F[j]) )):
                judge = True
print('Yes' if judge else 'No')