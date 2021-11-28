#  どうやって計算量を減らすか？
#  C問題は一貫してその傾向が強い気がする
N = int(input())
d = list(map(int, input().split()))

d.sort()

len_d = len(d)
x = int((len_d / 2) - 1)

d = d[x:x + 2]
set_d = len(set(d))
len_d = len(d)

if len_d % 2 != 0 or set_d != len_d:
    print(0)
else:
    print(d[-1] - d[0])