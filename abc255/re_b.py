n,k = map(int, input().split())
a = list(map(int, input().split()))
xy = []
import numpy as np
max_ = -10 ** 18 + 17
for i in range(n):
    x,y = map(int, input().split())
    xy.append([x,y])

for i in range(n):
    # iが光を持っている時
    idx = i + 1
    if idx in a:
        for j in range(n):
            if j == i:
                continue
            x = np.array(xy[i])
            y = np.array(xy[j])
            temp = np.linalg.norm(x - y)
            max_ = max(temp,max_)
print(max_)