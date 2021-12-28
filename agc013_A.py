N = int(input())
A = list(map(int, input().split()))

count = 1
if len(A) == 1:
    print(1)
    exit(0)

diff = A[1] - A[0]
for i in range(2,N):
    if A[i] - A[i - 1] == diff:
        pass
    else:
        if diff != 0:
            count += 1
            if i != N - 1:
                diff = A[i + 1] - A[i]
print(count)
