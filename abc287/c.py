n,m = map(int, input().split())

def create_edges(n, m):
    edges = []
    for i in range(m):
        u,v = map(int, input().split())
        edges.append((u,v))
    return edges
edges = create_edges(n,m)
def is_path_graph(n, m, edges):
    if m != n-1:
        return False
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        cur = queue.pop(0)
        for v in graph[cur]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    for i in range(n):
        if not visited[i]:
            return False
    return True
if is_path_graph(n,m,edges):
    print('Yes')
else:
    print('No')