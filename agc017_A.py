N,P = map(int, input().split())
A = list(map(int, input().split()))

# 初期値に偶数の変数をeven = Falseにする
even = True
for a in A:
    # 奇数の場合
    if a % 2 == 1:
        even = False
        # 奇数が出た時点で終了
        break

# evenがTrueの場合 = 最後まで奇数が出なかった場合 = 全て偶数
if even:
    if p == 1:
        print(0)
    else:
        print(2 ** n)
# evenがfalseの場合 = 途中で一つでも奇数が出た場合
else:
    print(2 ** (N - 1))
