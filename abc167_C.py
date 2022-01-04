from itertools import product
INF = 1 << 60

def judge(pro):
    S = 0
    L = [0] * M
    for i in range(N):
        # 0の場合スキップする
        if not pro[i]:
            continue
        S += C[i]
        for j in range(M):
            L[j] += A[i][j]
    
    for i in range(M):
        if L[i] < X:
            return INF
    return S

N,M,X = map(int, input().split())
C = [0] * N
A = [[] for _ in range(N)]


for i in range(N):
    C[i], *A[i] = map(int, input().split())
    
ans = INF
for pro in product((0,1), repeat = N):
    ans = min(ans, judge(pro))
    print(ans)
print(ans if ans != INF else -1)
