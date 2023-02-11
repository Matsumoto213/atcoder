N, M = map(int, input().split()) # N : 頂点の数、M：レの数
A = list(map(int, input().split())) # A: 各頂点間にあるレのインデックスを持つリスト

graph = [[] for _ in range(N + 1)] # 頂点1 ~ Nまでのグラフを作成
for i in range(M):
    graph[A[i]].append(A[i] + 1) # 接続される頂点間にエッジを追加
    graph[A[i] + 1].append(A[i])

# BFSを使用して未訪問の要素を取得する
answer = []
visited = set()
for i in range(1, N + 1):
    if i not in visited:
        temp = [] # 同じ連結成分を保存する
        q = [i] # queue
        while q:
            curr = q.pop(0)
            if curr not in visited:
                visited.add(curr)
                temp.append(curr)
                q.extend(graph[curr])
        answer.extend(temp[::-1]) # 取得した頂点をreverseして追加

print(*answer)
