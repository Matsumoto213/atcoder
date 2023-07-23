N, M = map(int, input().split())
S = []
ans = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    s = list(input())
    S.append(s)

from collections import deque

#止まれるますbfsをする
queue = deque([(1, 1)])  #スタートノード
visited = set()

dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

while queue:
    node = queue.popleft()
    #今いる場所
    node_n = node[0]
    node_m = node[1]
    ans[node_n][node_m] = 1
    if node in visited:
      continue
    visited.add(node)
    #直線で移動する。
    for d in dir:
        dn = d[0]
        dm = d[1]
        if dn != 0:
            n = node_n
            m = node_m
            while S[n][m] != "#":#壁にぶつかるまで動かす
                ans[n][m] = 1
                n += dn
            #ぶつかったところで１歩戻す
            n -= dn
            stop = (n, m)
            if stop not in visited:
                queue.append(stop)
        else:
            n = node_n
            m = node_m
            while S[n][m] != "#":#壁にぶつかるまで動かす
                ans[n][m] = 1
                m += dm
            #ぶつかったところで１歩戻す
            m -= dm
            stop = (n, m)
            if stop not in visited:
                queue.append(stop)

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += ans[i][j]
print(ans)
print(cnt)

