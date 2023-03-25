N = int(input())
G = []

def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    slope1 = (y2 - y1) * (x3 - x2)
    slope2 = (y3 - y2) * (x2 - x1)

    return slope1 == slope2

for i in range(N):
    x,y = map(int, input().split())
    G.append([x,y])

for i in range(N - 2):
    for j in range(i + 1,N - 1):
        for l in range(j + 1,N):
            if is_collinear(G[i],G[j],G[l]):
                print('Yes')
                exit()
print('No')