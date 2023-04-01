S = [input() for _ in range(8)]

def find_piece_position(grid):
    for row_index, row in enumerate(grid):
        if '*' in row:
            column_index = row.index('*')
            column_letter = chr(column_index + 97)
            row_number = 8 - row_index
            return column_letter + str(row_number)

position = find_piece_position(S)
print(position)