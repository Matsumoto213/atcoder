import itertools
N = int(input())
xy = [0]

# 座標平面上の3点の三角形の面積を求める公式
# https://mathwords.net/x1y2hikux2y1

def calc_triangle_area(a,b,c):
    (ax, ay), (bx, by), (cx, cy) = a,b,c
    return abs((ax - cx) * (by - ay) - (ax - bx) * (cy - ay)) / 2

for _ in range(N):
    x,y = map(int, input().split())
    xy.append((x,y))

l = []
for i in range(1, N + 1):
    l.append(i)

ans = 0
for v in itertools.combinations(l, 3):
    a,b,c = list(v)
    print(a,b,c)
    circle = calc_triangle_area(xy[a],xy[b],xy[c])
    if circle > 0:
        ans += 1
print(ans)