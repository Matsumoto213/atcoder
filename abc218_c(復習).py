n = int(input())

# グリッドを読み込んで#の位置の集合を返す
def read():
    s = set()
    for y in range(n):
        l = input()
        for x in range(n):
            if l[x] == "#":
                s.add((x,y))
    return s

s = read()
t = read()




#　入力例１では
# s = {(3, 2), (1, 2), (2, 1), (2, 2)}
# t = {(4, 4), (3, 3), (4, 2), (4, 3)}
# になる


for _ in range(4):
    # もっとも左の#を(0,0)にする
    mx, my = min(s)
    s = set((x - mx, y - my) for x, y in s)
    mx, my = min(t)
    t = set((x - mx, y - my)for x, y in t)


    if s == t:
        print("Yes")
        exit(0)

    # tを回転させる
    t = set((y, -x)for x, y in t)

  
print("No")

# この課題のポイント
# 平行移動は、各要素から値を足し引きするだけで良く、範囲外アクセスを気にする必要が無くなります。
# 90度の回転は、各要素 (x,y) を (y,−x) に置き換えるだけです。