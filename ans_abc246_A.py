a,b = map(int, input().split())
import math
temp = math.sqrt(a ** 2 + b ** 2)
print(a / temp, b / temp)