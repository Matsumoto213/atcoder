import math

def is_prime(n):
    # 2 以下は素数ではない
    if n <= 2:
        return False
    # 2 以上の奇数は奇数で割り切れるかどうかで判定
    if n % 2 == 1:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    # 偶数は素数ではない
    else:
        return False

def solution(N):
    # N の素因数分解を行う
    for i in range(2, int(N ** 0.5) + 1):
        # N を i で割り切れる場合、素因数分解を行う
        if N % i == 0:
            # 素因数分解の結果、p ** 2 を見つけた場合
            if is_prime(i) and (N // i) % i == 0:
                p = i
                q = N // (p ** 2)
                print(p, q)
                break
            # 素因数分解の結果、q を見つけた場合
            elif is_prime(N // i):
                p = (N // i) ** 0.5
                q = N // (p ** 2)
                print(int(p), q)
                break

T = int(input())
for i in range(T):
    N = int(input())
    solution(N)
