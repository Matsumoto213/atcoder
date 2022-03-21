a,b,c,d = map(int, input().split())
takahashi = [i for i in range(a, b + 1)]
aoki = [i for i in range(c, d + 1)]
judge = [False] * (b - a + 1)

import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

for i in range(len(takahashi)):
    for j in range(len(aoki)):
        temp = takahashi[i] + aoki[j]
        if is_prime(temp):
            judge[i] = True

print('Aoki' if judge.count(True) == b - a + 1 else 'Takahashi')