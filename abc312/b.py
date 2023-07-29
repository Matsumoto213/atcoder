N,M = map(int, input().split())
S = [input() for _ in range(N)]

def matches_tak_code(grid_section):
    tak_code = [
        "###.?????",
        "###.?????",
        "###.?????",
        "....?????",
        "?????????",
        "?????....",
        "?????.###",
        "?????.###",
        "?????.###"
    ]

    for i in range(9):
        for j in range(9):
            if tak_code[i][j] != '?' and tak_code[i][j] != grid_section[i][j]:
                return False
    return True

def find_tak_codes(N, M, grid):
    result = []
    for i in range(N-8):
        for j in range(M-8):
            sub_grid = [row[j:j+9] for row in grid[i:i+9]]
            if matches_tak_code(sub_grid):
                result.append((i+1, j+1))  # 1-indexed

    return result

ans = find_tak_codes(N, M, S)

for i in ans:
    print(*i)