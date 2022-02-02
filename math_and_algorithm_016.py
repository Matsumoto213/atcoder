N = int(input())
a = list(map(int, input().split()))

from functools import reduce
import math

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

print(my_gcd(*a))