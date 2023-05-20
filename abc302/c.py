N,M = map(int, input().split())
S = [input() for _ in range(N)]

def can_be_arranged(strings,N,M):
    graph = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            # If strings differ by one character, add an edge
            if sum(a != b for a, b in zip(strings[i], strings[j])) == 1:
                graph[i].append(j)
                graph[j].append(i)

    # Try to find a hamiltonian path using DFS
    visited = [False] * N

    def dfs(node, depth):
        visited[node] = True
        if depth == N:
            return True
        for neighbor in graph[node]:
            if not visited[neighbor] and dfs(neighbor, depth + 1):
                return True
        visited[node] = False
        return False

    # Try starting DFS from each node
    for start_node in range(N):
        if dfs(start_node, 1):
            return True

    return False
print('Yes' if can_be_arranged(S,N,M) else 'No')

