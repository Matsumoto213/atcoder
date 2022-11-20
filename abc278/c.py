N,Q = map(int, input().split())

from collections import defaultdict
A = defaultdict(set)

for _ in range(Q):
    T,a,b = map(int, input().split())
    # フォロー
    if T == 1:
        A[a].add(b)
    # フォロー解除
    elif T == 2:
        A[a].discard(b)
    # チェック
    elif T == 3:
        if b in A[a] and a in A[b]:
            print('Yes')
        else:
            print('No')