R,C = map(int, input().split())
B = []

for i in range(R):
    temp = input()
    B.append(temp)

def manhattan_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def explode(board, R, C):

    new_board = [list(row) for row in board]
    
    for r in range(R):
        for c in range(C):
            if board[r][c].isdigit():
                bomb_power = int(board[r][c])
                
                for r2 in range(R):
                    for c2 in range(C):
                        if manhattan_distance(r, c, r2, c2) <= bomb_power:
                            new_board[r2][c2] = "."
                            
    return ["".join(row) for row in new_board]

result = explode(B,R,C)

for row in result:
    print(row)