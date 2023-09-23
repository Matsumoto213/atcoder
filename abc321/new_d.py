from bisect import bisect_right

# 入力を受け取る
n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 副菜の価格をソートし、累積和を取る
b.sort()
cum_sum_b = [0]  # 累積和の初項は0
for bj in b:
    cum_sum_b.append(cum_sum_b[-1] + min(bj, p))

# 各主菜に対して、定食の価格の総和を求める
total = 0
for ai in a:
    # ai + bj <= p となるbjの最大のindexを求める
    idx = bisect_right(b, p - ai)
    # idx は ai + bj > p となるbjの最小のindexなので、
    # 0からidx-1までのbjで定食の価格の総和を計算する
    total += idx * min(ai, p) + cum_sum_b[idx]

print(total)
