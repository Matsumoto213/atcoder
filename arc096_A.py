A,B,C,X,Y = map(int, input().split())
xy = [X,Y]

max_ = max(xy)
min_ = min(xy)

# 全てABピザを買って分けるパターン
all_ab = max_ * C * 2

# 途中で買い換えるパターン
if X >= Y:
    half = A * (X - Y) + (C * Y * 2)
else:
    half = B * (Y - X) + (C * X * 2)

# 単品のパターン
single = (A * X) + (B * Y)
print(min(all_ab,half,single))