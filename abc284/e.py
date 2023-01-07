import math
def find_p_q(N):
    p = int(math.sqrt(N))
    # p ** 2 で割り切れるか判定
    while N % (p ** 2) != 0:
        p -= 1
        # p ** 2 で割った余りを q とする
        q = N // (p ** 2)
    return p, q

T = int(input())

for i in range(T):
    N = int(input())
    p, q = find_p_q(N)
    print(p, q)