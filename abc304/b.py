N = int(input())

def approximate_number(N):
    if N < 10**3:
        return N
    elif N < 10**4:
        return N // 10 * 10
    elif N < 10**5:
        return N // 100 * 100
    elif N < 10**6:
        return N // 1000 * 1000
    elif N < 10**7:
        return N // 10**4 * 10**4
    elif N < 10**8:
        return N // 10**5 * 10**5
    else:
        return N // 10**6 * 10**6

# 近似値を出力する
print(approximate_number(N))
