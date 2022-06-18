N,K = map(int, input().split())
A = list(map(int, input().split()))
X = []
Y = []
import math
ans = 10 ** 15 + 7
for _ in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i,j in zip(X,Y):
    print(i,j)
    