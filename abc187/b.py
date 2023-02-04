N = int(input())
L = []
for i in range(N):
    x,y = map(int, input().split())
    L.append((x,y))

def slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (y2 - y1) / (x2 - x1)

ans = 0
for i in range(N - 1):
    for j in range(i + 1,N):
        Slope = slope(L[i],L[j])
        if -1 <= Slope <= 1:
            ans += 1
print(ans)