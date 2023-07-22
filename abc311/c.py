N = int(input())
edges = list(map(int, input().split()))

from collections import defaultdict

def find_cycle(N, edges):
    graph = defaultdict(list)
    for i in range(N):
        graph[i+1] = edges[i]

    visited = [0] * (N + 1)
    stack = []

    def dfs(v):
        visited[v] = 1
        stack.append(v)
        for nv in [graph[v]]:
            if visited[nv] == 0:
                return dfs(nv)
            elif visited[nv] == 1:
                return stack[stack.index(nv):]
        stack.pop()
        visited[v] = 2
        return []

    for i in range(1, N + 1):
        if visited[i] == 0:
            cycle = dfs(i)
            if cycle:
                return cycle

    return []

ans = find_cycle(N, edges)
print(len(ans))
print(*ans)