a,b = map(int, input().split())
import math

# Python3.9以下は最小公倍数を求めるためにこの関数を使う
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
print(my_lcm(a,b))