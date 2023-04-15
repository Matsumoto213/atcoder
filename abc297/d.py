def gcd(a, b):
    if b == 0:
        return a, 0
    else:
        d, count = gcd(b, a % b)
        return d, count + a // b

a, b = map(int, input().split())
d, count = gcd(a, b)
print(count - 1)