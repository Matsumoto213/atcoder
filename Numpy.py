import numpy as np
# 0~99の数字からランダムに10個取ってくる
arr = np.random.randint(0, 100, 10)
# > array([74, 29,  6, 79, 76, 13,  3, 56, 25, 50])

# 奇数番目の数値をarrから除外したい
odd = [1,3,5,7,9]

# 方法① リスト内包表記
index = [i for i in np.arange(len(arr)) if i not in odd]
arr_even = arr[index]

# 方法② True/Falseでマスキングする
index = np.ones(len(arr), dtype=bool)
index[odd] = False
arr_even = arr[index]

# 方法③ np.delete
arr_even = np.delete(arr, odd)
