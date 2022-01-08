from math import dist
N = int(input())
x = []
y = []

for i in range(N):
    X,Y = map(int, input().split())
    x.append(X)
    y.append(Y)

ans = -10 ** 11
for i in range(N - 1):
    for j in range(i + 1, N):
        a = (x[i],y[i])
        b = (x[j],y[j])
        
        n = dist(a,b)
        ans = max(n,ans)
print(ans)