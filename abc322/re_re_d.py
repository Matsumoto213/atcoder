def rotate(polyomino):
    return list(zip(*reversed(polyomino)))


def get_positions(polyomino):
    positions = []
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == '#':
                positions.append((i, j))
    return positions


def fit(grid, positions, x_offset, y_offset):
    new_grid = [row[:] for row in grid]
    for x, y in positions:
        x += x_offset
        y += y_offset
        if x < 0 or x >= 4 or y < 0 or y >= 4 or new_grid[x][y] == '#':
            return None
        new_grid[x][y] = '#'
    return new_grid


def solve(grid, polyominoes):
    if not polyominoes:
        return all(cell == '#' for row in grid for cell in row)

    polyomino = polyominoes[0]
    positions = get_positions(polyomino)
    for x_offset in range(-min(x for x, y in positions), 4 - max(x for x, y in positions) + 1):
        for y_offset in range(-min(y for x, y in positions), 4 - max(y for x, y in positions) + 1):
            new_grid = fit(grid, positions, x_offset, y_offset)
            if new_grid is not None and solve(new_grid, polyominoes[1:]):
                return True
    polyomino = rotate(polyomino)
    for _ in range(3):
        positions = get_positions(polyomino)
        for x_offset in range(-min(x for x, y in positions), 4 - max(x for x, y in positions) + 1):
            for y_offset in range(-min(y for x, y in positions), 4 - max(y for x, y in positions) + 1):
                new_grid = fit(grid, positions, x_offset, y_offset)
                if new_grid is not None and solve(new_grid, polyominoes[1:]):
                    return True
        polyomino = rotate(polyomino)
    return False


def main():
    grid = [['.'] * 4 for _ in range(4)]
    polyominoes = []
    for _ in range(3):
        polyomino = [list(input().strip()) for _ in range(4)]
        polyominoes.append(polyomino)

    if solve(grid, polyominoes):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
