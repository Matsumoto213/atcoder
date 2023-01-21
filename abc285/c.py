# 入力の受け取り
S=input()

# 各文字を数値へ変換したものを格納するリスト
d=[]

# x：Sの各文字について
for x in S:
    # (文字コード-64)を格納
    d.append(ord(x)-64)

# ひっくり返す
# 左から順に処理したいため
d=d[::-1]
# print(d)
# 答え
ans=0

# i=0~(dの長さ-1)
for i in range(len(d)):
    # 26^i*数値
    ans+=26**i*d[i]

# 答えの出力
print(ans)