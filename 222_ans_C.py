n,m = map(int, input().split())

hands = []

for _ in range(2 * n):
    s = input()
    hands.append(s)

rank = [[0, i] for i in range(2 * n)]

#  D[h1][h2]: じゃんけんでh1, h2を出して、h1が勝つなら1, h2が勝つなら2
D = {"G":{"C":1, "P":2},
    {"C":{"P":1, "G":2},
    {"P":{"G:":1, "C":2 }}

for j in range(m):
    for i in range(n):
        p1 = 

