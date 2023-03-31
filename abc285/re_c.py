S = input()

# 各文字を数値へ変換したものを格納するリスト
d=[]

# x：Sの各文字について大文字からasciiコードがいくつ離れているかを数える
for x in S:
    # (文字コード-64)を格納
    d.append(ord(x)-64)

d = d[::-1]
ans = 0
for i in range(len(d)):
    ans += 26 ** i * d[i]
print(ans)