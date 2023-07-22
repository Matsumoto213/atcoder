N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False]*M for _ in range(N)]

def dfs(x, y):
    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not (0 <= nx < N and 0 <= ny < M) or grid[nx][ny] == '#':
                break
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)

dfs(1, 1)

count = sum(row.count(True) for row in visited)
print(count)
