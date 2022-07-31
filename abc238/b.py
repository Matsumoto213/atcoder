N = int(input())
A = list(map(int, input().split()))
B = [0]

temp = 0
for i in range(N):
    temp += A[i]
    if temp >= 360:
        temp = temp - 360
    B.append(temp)
B.sort()
ans = -10 ** 15 + 8
for i in range(N):
    temp = abs(abs(B[i + 1] - B[i]))
    ans = max(ans,temp)
print(max(360 - B[-1],ans))