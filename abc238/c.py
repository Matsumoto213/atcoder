N = int(input())
A = list(map(int, input().split()))
B = []

temp = 0
for i in range(N):
    temp += A[i]
    if temp >= 360:
        temp = temp - 360
    B.append(temp)


B.sort()
ans = - 10 ** 15 + 8

if N == 1:
    print(abs(360 - B[0]))
else:
    for i in range(N - 1):
        ans = max(ans, B[i + 1] - B[i])
    print(ans)