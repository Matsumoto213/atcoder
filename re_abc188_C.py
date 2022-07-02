N = int(input())
a = list(map(int, input().split()))

# 2jと2j - 1でどちらがレートが低いのかを判定し、そのレートが高い人同士が対決する
# ただ入力例が10(9)あるので、計算量を減らす方法を考える
# 左の山と右の山で一番レートが高いindexを見つける
# それを決勝戦で戦わせ、敗者を見つけそのindexが答えになる
left = a[2**(N-1):]
right = a[:2**(N - 1)]

win_left_idx = left.index(max(left))
win_right_idx = right.index(max(right))

final_loser = min(left[win_left_idx],right[win_right_idx])
print(a.index(final_loser) + 1)