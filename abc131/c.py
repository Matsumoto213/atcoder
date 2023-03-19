def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_not_divisible(A, B, C, D):
    lcm_cd = lcm(C, D)  # CとDの最小公倍数を求める
    count_C = B // C - (A - 1) // C  # Cで割り切れる数の個数
    count_D = B // D - (A - 1) // D  # Dで割り切れる数の個数
    count_CD = B // lcm_cd - (A - 1) // lcm_cd  # CとDの両方で割り切れる数の個数
    count_not_CD = B - A + 1 - count_C - count_D + count_CD  # CでもDでも割り切れない数の個数
    return count_not_CD

A, B, C, D = map(int, input().split())
print(count_not_divisible(A, B, C, D))