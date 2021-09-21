n = int(input())
d, x  = map(int, input().split())
A = [int(input()) for i in range(n)]
lst = [1] * n

count = len(A)
i = 0

while True:
    if i == len(A) - 1:
        break
    if lst[i] > d:
        i += 1
    else:
        count += 1
    lst[i] += A[i]

print(count + x)
