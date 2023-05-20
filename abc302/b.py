H,W = map(int, input().split())
S = [input() for _ in range(H)]

def find_word(grid):
    H = len(grid)
    W = len(grid[0])
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    word = "snuke"
    positions = []

    for i in range(H):
        for j in range(W):
            for dx, dy in directions:
                try:
                    if all(0 <= i + k * dx < H and 0 <= j + k * dy < W and grid[i + k * dx][j + k * dy] == word[k] for k in range(5)):
                        positions = [(i+dx*n+1, j+dy*n+1) for n in range(5)]
                        return positions
                except IndexError:
                    continue
    return None

ans = find_word(S)

for i in ans:
    print(*i)