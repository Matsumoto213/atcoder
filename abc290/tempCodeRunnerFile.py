N,K = map(int,input().split())
A = list(map(int,input().split()))
import itertools
ans = -10 ** 10 + 8
for pattern in itertools.combinations(A, K):
    # Bを昇順にソート
    B = sorted(list(pattern))
    # 条件を満たすmの値を求める
    m = 0
    for i in range(K):
        if B[i] == m:
            m += 1
        else:
            break
    ans = max(ans,m)
print(ans)