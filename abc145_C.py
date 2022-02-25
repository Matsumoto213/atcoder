import itertools
import math

N = int(input())
x = []
y = []
L = [i for i in range(1, N + 1)]

for i in range(N):
    X,Y = map(int, input().split())
    x.append(x)
    y.append(y)

temp = 0
for v in itertools.permutations(L,N):
    v = list(v)
    print(v)
    for i in range(len(v) - 1):
        print(v[i])
    #     temp += math.sqrt((x[v[i] - 1] - x[v[i + 1] - 1]) ** 2) + ((y[v[i] - 1] - y[v[i + 1] - 1]) ** 2)

# print(temp - len(v))
