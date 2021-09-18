card = []

for _ in range(3):
    card.append(list(map(int, input().split())))

# 3 * 3　の数だけFalseを書き出す
marked = [[False for _ in range(3)] for _ in range(3)]


# 関数の使い方
# ビンゴの関数として再利用可能だ
def check(marked):
    for i in range(3):
        if all([marked[i][j] for j in range(3)]):
            return True
 
        if all([marked[j][i] for j in range(3)]):
            return True
    
    if marked[0][0] and marked[1][1] and marked[2][2]:
        return True
 
    if marked[0][2] and marked[1][1] and marked[2][0]:
        return True

n = int(input())

for _ in range(n):
    b = int(input())

    for i in range(3):
        for j in range(3):
            if card[i][j] == b:
                marked[i][j] = True


if check(marked):
    print("Yes")
else:
    print("No")