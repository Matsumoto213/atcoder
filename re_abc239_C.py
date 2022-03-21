a,b,c,d = map(int,input().split())
import math
judge = [0,0,0,0,0,0,0,0]
for j in range(2):
    if j == 0:
        xy = [(a + 2,b + 1),(a + 1,b + 2),(a - 1,b + 2),(a - 2,b + 1),(a - 2,b - 1),(a - 1,b - 2),(a + 1,b - 2),(a + 2,b - 1)]
    else:
        xy = [(c + 2,d + 1),(c + 1,d + 2),(c - 1,d + 2),(c - 2,d + 1),(c - 2,d - 1),(c - 1,d - 2),(c + 1,d - 2),(c + 2,d - 1)]

    for i in range(len(xy)):
        x,y = xy[i]
        temp = math.sqrt((a - x) ** 2 + (b - y) ** 2)
        if temp == math.sqrt(5):
            judge[i] += 1

    if 2 in judge:
        print('Yes')
        exit()
            
print('No')