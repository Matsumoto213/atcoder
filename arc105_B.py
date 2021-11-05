N = int(input())
A = list(map(int, input().split()))
i = 0
while True:
    X = max(A)
    x = min(A)
    if len(set(A)) == 1:
        break
    if i == len(A):
        i = 0

    if A[i] == X:
        A[i] = X - x

    i += 1
print(A[N - 1])