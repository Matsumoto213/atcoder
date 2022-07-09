import numpy as np
N = int(input())
x = list(map(int, input().split()))

x = [abs(i) for i in x]
print(sum(x))
print(sum([i**2 for i in x])**.5)
print(max(x))