N,D = map(int, input().split())
import math
# D以下のものを数える
ans = 0
for i in range(N):
    x,y = map(int, input().split())
    temp = math.sqrt((x ** 2) + (y ** 2))
    if temp <= D:
        ans += 1
print(ans)