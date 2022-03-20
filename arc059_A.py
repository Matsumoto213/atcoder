N = int(input())
A = list(map(int, input().split()))

mi = min(A)
ma = max(A)

ans = 10 ** 18

for i in range(mi, ma + 1):
    temp = 0
    for j in range(len(A)):
        temp += (A[j] - i) ** 2
    ans = min(ans, temp)

print(ans)
