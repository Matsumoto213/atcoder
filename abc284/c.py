import sys
sys.setrecursionlimit(10**7)
N,M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    a -= 1 # 0-indexedにする
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False for _ in range(N)]
def dfs(current):
    visited[current] = True
    for next_node in graph[current]:
        if not visited[next_node]:  # 未訪問の場合
            dfs(next_node)

for i in range(N):
    if not visited[i]: # 未訪問の場合
        dfs(i) # 連結成分を探索
        count += 1
print(count)