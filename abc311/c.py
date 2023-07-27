# 関数再帰呼び出し上限回数対策
import sys
sys.setrecursionlimit(10**7)
def find_cycle(N, edges):
    graph = [0] + edges
    visited = [0]*(N+1)
    stack = []
    def dfs(v):
        visited[v] = 1
        stack.append(v)
        for nv in [graph[v]]:
            print(visited,stack,nv)
            if visited[nv] == 0:
                return dfs(nv)
            elif visited[nv] == 1:
                return stack[stack.index(nv):]
        stack.pop()
        visited[v] = 2
        return []
    for i in range(1, N+1):
        if visited[i] == 0:
            cycle = dfs(i)
            if cycle:
                return cycle

    return []

N = int(input())
edges = list(map(int, input().split()))
cycle = find_cycle(N, edges)
print(len(cycle))
for v in cycle:
    print(v, end=" ")
print()