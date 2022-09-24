x,y,z = map(int, input().split())
# xとyともに+にある場合
if y > 0 and x > y:
    if z > y:
        print(-1)
    else:
        if z > 0:
            print(x)
        else:
            print(abs(z * 2) + x)
# 壁がマイナスにあり、xの通り道に壁がある場合
elif y < 0 and x < y:
    # ハンマーが通り道がある場合
    if z < y:
        print(-1)
    else:
        if z < 0:
            print(abs(x))
        else:
            print(abs(z * 2) + abs(x))
else:
    print(abs(x))