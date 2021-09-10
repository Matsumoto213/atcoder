import math
n = int(input("n: "))
count = 0

for i in range(10,0,-1):
    x = math.factorial(i)
    while n >= x:
        n -= x
        count += 1
print(count)

