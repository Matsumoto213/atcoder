R,C = map(int, input().split())
B = [input() for _ in range(R)]

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

ans = [list(row) for row in B]
for r in range(R):
    for c in range(C):
        # マス目が数字であれば、マンハッタン距離がN以下のますを空きマスに変更する
        if B[r][c].isdigit():
            bomb_power = int(B[r][c])
            for r2 in range(R):
                for c2 in range(C):
                    if manhattan_distance(r,c,r2,c2) <= bomb_power:
                        ans[r2][c2] = '.'


for i in range(R):
    for j in range(C):
        print(ans[i][j],end = "")
    print()