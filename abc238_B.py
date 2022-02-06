N = int(input())
A = list(map(int, input().split()))

x = [0]

for i in A:
    for m in range(len(x)):
        x[m] += i
        if x[m] >= 360:
            x[m] -= 360
    x.append(0)

x.sort()
ans = 0

for i in range(len(x) - 1):
    ans = max(ans, x[i + 1] - x[i])
ans = max(result, 360 - x[-1])
print(ans)