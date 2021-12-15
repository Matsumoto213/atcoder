import itertools
import math

N = int(input())
l = []
X = []
Y = []

for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(1, N + 1):
    l.append(i)

p = itertools.permutations(l, N)
n = math.factorial(N)
result = 0
print(X,Y)
for i in p:
    L = list(i)
    for j in range(1,N):
        result += math.sqrt((X[j - 1] - X[j]) ** 2) + math.sqrt(((Y[j - 1] - Y[j]) ** 2))
    print(result)
     
print(result / n)