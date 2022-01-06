# リストの全てを足して出力する方法
# 累積和
import itertools

L = [1,2,3,4,5,6]

for idx,i in enumerate(itertools.accumulate(L)):
    if idx == len(L) - 1:
        print(i)
    