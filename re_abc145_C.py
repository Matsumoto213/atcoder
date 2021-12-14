import itertools
import math

N = int(input())
l = []
A = []

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(1, N + 1):
    l.append(i)

p = itertools.permutations(l, N)
n = math.factorial(N)
result = 0


        
print(result / n)