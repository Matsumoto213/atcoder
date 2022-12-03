n,k = map(int, input().split())
a = list(map(int, input().split()))
xy = []
import numpy as np
max_ = -10 ** 18 + 17
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])

# 二点間の距離を求める関数(インデックスを引数として渡す)
def calc_dist(a, b):
  x1, y1 = xy[a]
  x2, y2 = xy[b]
  return ((x1-x2)**2+(y1-y2)**2)**0.5

for i in range(n):
    # iが光を持っている時
    val = 10 ** 18 + 9
    for idx in a:
        idx -= 1
        val = min(calc_dist(i,idx),val)
    max_ = max(val,max_)
print(max_)