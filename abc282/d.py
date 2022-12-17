
from collections import deque
from collections import defaultdict

N,M = list(map(int,input().split()))
G = defaultdict(set)

color = [0 for i in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    G[A].add(B)
    G[B].add(A)

color[1] = 1
que = deque([1])#始点を追加
bipartite = True

while len(que):
    p = que.popleft()#直近で追加したグラフの頂点を取得
    for q in list(G[p]):#結合しているグラフの頂点を参照
        if color[q] == 0:#塗られていないなら別の色で塗る
            color[q] = -color[p]
            que.append(q)
        elif color[q] == color[p]:#同じ色だったら2部グラフではないと返し終了させる
            bipartite = False
            break
    print(bipartite)