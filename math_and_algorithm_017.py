import math
from functools import reduce
N = int(input())
a = list(map(int, input().split()))

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

print(my_lcm(*a))