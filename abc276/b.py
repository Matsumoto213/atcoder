n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a - 1].append(b)
    graph[b - 1].append(a)

for i in range(n):
    graph[i].sort()

for i in range(n):
    print(len(graph[i]), *graph[i])