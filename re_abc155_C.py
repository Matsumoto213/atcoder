#Counter関数の使い方を改めて考える
# Counter関数で作成したvaluesなどはそのままの形ではsort
# することができず、一度リストの型に変換しなければならない
#Counter関数の使い方を改めて考える
from collections import Counter
N = int(input())
S = [input() for _ in range(N)]

L = Counter(S)
L = dict(sorted(L.items(), key=lambda x:x[0]))

val = list(L.values())
val.sort(reverse = True)
max_ = val[0]
for key,value in L.items():
    if max_ == value:
        print(key)
