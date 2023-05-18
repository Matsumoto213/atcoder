L = int(input())

import math
def count_ways(L):
    return math.comb(L - 1, 11)
print(count_ways(L))