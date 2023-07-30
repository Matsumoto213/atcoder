N,M = map(int, input().split())
S = [input() for _ in range(N)]

def ismatch_tak_code(grid):
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
            if tak_code[i][j] != '?' and grid[i][j] != tak_code[i][j]:
                return False
    return True

ans = []
for i in range(N - 8):
    for j in range(M - 8):
        new_grid = []
        for row in S[i:i + 9]:
            sub_row = row[j:j + 9]
            new_grid.append(sub_row)
        if ismatch_tak_code(new_grid):
            ans.append([i + 1,j + 1])

for i in ans:
    print(*i)
