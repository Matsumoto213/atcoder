N = int(input())
T = [int(input()) for _ in range(N)]

import math
from functools import reduce

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

print(my_lcm(*T))