from itertools import product

def solve():
    ans = 0

    for pro in product((0, 1), repeat = len(n)):
        first = []
        second = []

        for i, b in enumerate(pro):
            if b == 1:
                first.append(n[i])

            else:
                second.append(n[i])
            
        if len(first) == 0 or len(second) == 0:
                continue
            
        print(first)
        print(second)

        first.sort(reverse = True)
        second.sort(reverse = True)

        a = int(''.join(first))
        b = int(''.join(second))

        ans = max(ans, a * b)
    return ans
n = '998244353'
print(solve())

