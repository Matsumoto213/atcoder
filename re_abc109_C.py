import math
import bisect
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


N,x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 一番近い点との差分を求める
idx = bisect.bisect_left(a, x)
a.insert(idx,x)

L = []
for i in range(1,N + 1):
    temp = a[i] - a[i - 1]
    L.append(temp)

print(my_gcd(*L))