N = int(input())

import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


for i in range(1, N + 1):
    if is_prime(i):
        print(i,end = " ")
        