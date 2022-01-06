from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


# distは頂点からの距離を表す
dist = [-1] * N
dist[0] = 0

d = deque()
d.append(0)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = v + 1
        d.append(i)

print("Yes")
for ans in dist[1:]:
    print(ans)