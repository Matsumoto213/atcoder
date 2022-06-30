H,W = map(int, input().split())

ans = 0
for i in range(H):
    for j in range(W):
        # 縦が偶数の場合
        if i % 2 == 0:
            if j % 2 == 0:
                ans += 1
        # 縦が奇数の場合
        else:
            if j % 2 != 0:
                ans += 1
print(ans)
