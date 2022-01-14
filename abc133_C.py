L,R = map(int, input().split())
ans = 10 ** 11 + 7

# 最小値を求める場合0が最も少ないので0になった瞬間0を出力すると計算量を減らすことができる
# 0になったらすぐ返す
for i in range(L, R):
    for j in range(L + 1, R + 1):
        temp = (i * j) % 2019
        if temp == 0:
            print(0)
            exit()
            
        ans = min(ans,temp)
print(ans)