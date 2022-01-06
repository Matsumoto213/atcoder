from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 全頂点を「未訪問」に初期化
dist = [-1] * (n + 1)

# 初期条件【頂点0を初期ノードとする】
dist[0] = 0
# 0を橙色頂点にする
dist[1] = 0

# その時点での橙色頂点 (発見済みだが未訪問な頂点) を格納するキュー
d = deque()
d.append(1)

# distとは頂点1から距離iまでの距離
while d:
    # キューから先頭頂点を取り出す
    v = d.popleft()
    
    # vから辿れる頂点を全て調べる
    for i in graph[v]:
        # すでに発見済みの頂点は探査しない
        if dist[i] != -1:
            continue
        # これがこの実装の全単位の根幹部分
        # iから辿れるということは、つまりiから1つ動くと辿れるということだから+1にする
        dist[i] = v + 1
        
        # iはもう訪問したという意味のコードになる
        d.append(i)
ans = dist[1:]
# print(*ans)

