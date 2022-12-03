N,K = map(int, input().split())
A = list(map(int, input().split()))
xy = []
import numpy as np
max_ = -10 ** 18 + 17
for i in range(N):
    x,y = map(int, input().split())
    xy.append([x,y])

print(xy)
for i in range(N):
    x,y = xy[i]
    for a in A:
        a -= 1
        min_ = max(max_, )