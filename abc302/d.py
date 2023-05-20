import bisect

# 入力を受け取る
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 贈り物のリストをソートする
A.sort()
B.sort()

# すぬけ君への贈り物の累積和を計算する
B_cumsum = [0] * (M + 1)
for i in range(M):
    B_cumsum[i+1] = B_cumsum[i] + B[i]

max_value = 0

# すべての青木君への贈り物についてループを回す
for i in range(N):
    # 制約D以下の価値のすぬけ君への贈り物を二分探索で見つける
    j = bisect.bisect_right(B, A[i] + D)

    # 価値の和が最大となる組み合わせを見つける
    if j > 0:
        max_value = max(max_value, A[i] + B[j-1])

# 結果を出力する
print(max_value)
