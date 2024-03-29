A,B,C,X,Y = map(int, input().split())

# AピザとBピザの購入金額
ab = A + B
AB = C * 2

ans = 0
if ab > AB:
    # 最低限枚数のabピザを購入する。
    min_ = min(X,Y)
    X -= min_
    Y -= min_
    # 残りの枚数をABピザを買う方が安いのかそれぞれのピザを買う方が安いのかで比較する
    ans = C * (min_ * 2) + min(X * A, X * 2 * C) + min(Y * B, Y * 2 * C)
else:
    ans = A * X + B * Y

print(ans)