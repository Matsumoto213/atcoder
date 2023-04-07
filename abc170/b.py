x,y = map(int, input().split())

def exist_tsuru_kame(X, Y):
    for i in range(X + 1):  # 鶴の数を0からXまで変化させる
        j = X - i  # 亀の数を計算する
        if 2 * i + 4 * j == Y:  # 足の総数がYと等しい場合
            return True  # 鶴と亀の数の組合せが存在する
    return False  # 存在しない場合

# 例として、X=10, Y=28の場合を考える
if exist_tsuru_kame(x, y):
    print("Yes")
else:
    print("No")