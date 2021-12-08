# 素数判定

import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

N = int(input())
ans = 0

for i in range(N + 1):
    ans += i

if is_prime(ans):
    print("WANWAN")
else:
    print("BOWWOW")