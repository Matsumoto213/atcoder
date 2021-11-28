N = int(input())
X = list(map(int, input().split()))

X.sort()
a = X[0]
b = X[-1]
result = 10 ** 8

for i in range(a, b + 1):
    ans = 0
    for j in X:
        ans +=(j - i) ** 2
    result = min(result,ans)
print(result)