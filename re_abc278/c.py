N,Q = map(int, input().split())
from collections import defaultdict
relation = defaultdict(set)

for _ in range(Q):
    t,a,b = map(int, input().split())
    # フォロー
    if t == 1:
        relation[a].add(b)
    # フォロー解除
    elif t == 2:
        relation[a].discard(b)
    # 相互フォローか確かめる
    elif t == 3:
        if b in relation[a] and a in relation[b]:
            print('Yes')
        else:
            print('No')