# 最小公倍数
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
    
print(math.lcm(6, 4))
# 最大公約数
import math
print(math.gcd(6, 4))