from bisect import bisect_right, bisect_left
from itertools import product

def solve(W, H, strawberries, A, cuts_x, B, cuts_y):
    cuts_x.sort()  # xのカットをソート
    cuts_y.sort()  # yのカットをソート
    cuts_x = [0] + cuts_x + [W]
    cuts_y = [0] + cuts_y + [H]
    strawberries = [(bisect_right(cuts_x, x), bisect_right(cuts_y, y)) for x, y in strawberries]

    grid = [[0] * (B+2) for _ in range(A+2)]
    for x, y in strawberries:
        grid[x][y] += 1

    for i, j in product(range(A+2), range(1, B+2)):
        grid[i][j] += grid[i][j-1]

    for i, j in product(range(1, A+2), range(B+2)):
        grid[i][j] += grid[i-1][j]

    min_strawberries = float('inf')
    max_strawberries = -float('inf')

    for ax, bx in product(range(A+1), range(B+1)):
        for ay, by in product(range(ax+1, A+2), range(bx+1, B+2)):
            strawberries_in_piece = grid[ay][by] - grid[ay][bx] - grid[ax][by] + grid[ax][bx]
            min_strawberries = min(min_strawberries, strawberries_in_piece)
            max_strawberries = max(max_strawberries, strawberries_in_piece)

    return min_strawberries, max_strawberries


W,H = map(int, input().split())
N = int(input())
strawberries = [list(map(int, input().split())) for i in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))
print(solve(W, H, strawberries, A, a, B, b))
