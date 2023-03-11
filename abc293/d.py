n, m = map(int, input().split())  # ロープの本数と操作の回数を入力する
color = ['R' if i == 0 else 'B' for i in range(n)]  # ロープの色を設定する（最初は赤青交互に並んでいる）
parent = [i for i in range(n)]  # 初期状態では各ロープがそれぞれ別々のグループに属しているとする

# 指定されたロープを結ぶ操作を行う関数
def unite(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py

# xが属するグループの代表元を求める関数
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# 操作を順番に実行する
for i in range(m):
    a, b, c, d = input().split()
    b, d = b == 'R', d == 'R'  # 色をbool値に変換する
    if b == d:  # 同じ色同士の結合は不要
        continue
    x, y = int(a) - 1, int(c) - 1  # ロープの番号を0-indexedに変換する
    unite(x, y)

# それぞれのグループに属するロープの数を数える
counts = {}
for i in range(n):
    p = find(i)
    if p not in counts:
        counts[p] = 0
    counts[p] += 1

# 結果を出力する
loop_count = 0
nonloop_count = 0
for c in counts.values():
    if c > 1:
        loop_count += 1
        nonloop_count += c
    else:
        nonloop_count += 1
if loop_count > 0:
    print(loop_count, nonloop_count)
else:
    print(0, n)
