from itertools import product

N, W = map(int, input().split())
A = list(map(int, input().split()))

# i番目がA[i]を使って合計にたす

def judge(pro):
    S = 0
    for i in range(N):
        if pro[i]:
            S += A[i]
    if S == W:
        return 1
    else:
        return 0


for pro in product((0,1), repeat = N):
    ans += judge(pro)
print(ans)