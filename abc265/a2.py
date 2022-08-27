# A - Apple

import math

X, Y, N = map(int, input().split())
ans = 0
if X < math.floor(Y / 3):
    # Xの方が安い
    ans = X * N
else:
    buy_x = X * math.floor(N % 3)
    buy_y = Y * math.floor(N / 3)
    ans = buy_x + buy_y

print(ans)
