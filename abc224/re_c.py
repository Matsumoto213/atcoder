N = int(input())
xy = []

for _ in range(N):
    x,y = map(int, input().split())
    xy.append((x,y))

def calc_triangle_area(a,b,c):
    (ax, ay), (bx, by), (cx, cy) = a,b,c
    return abs((ax - cx) * (by - ay) - (ax - bx) * (cy - ay)) / 2

ans = 0
for a in range(N - 2):
    for b in range(a + 1,N - 1):
        for c in range(b + 1,N):
            if calc_triangle_area(xy[a],xy[b],xy[c]):
                ans += 1
print(ans)