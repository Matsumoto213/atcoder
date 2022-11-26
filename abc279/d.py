a,b = map(int, input().split())
import math
ans = 10 ** 18 + 7
for i in range(10):
    temp = (b * i) + (a / math.sqrt(i + 1))
    ans = min(temp,ans)
print(ans)