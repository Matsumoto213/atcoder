N = int(input())
A = list(map(int, input().split()))

import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

min_ = my_gcd(*A)

a = 0
for i in A:
    a += min_ / i

print(min_ / a)