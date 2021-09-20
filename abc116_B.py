# 素数判定

import math
x = int(input())


def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1


