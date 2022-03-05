N = int(input())
x = list(map(int, input().split()))
a = min(x)
b = max(x)

min_ = 10 ** 15

for i in range(a, b + 1):
    temp = 0
    for j in range(N):
        temp += (x[j] - i) ** 2
    min_ = min(temp,min_)
print(min_)