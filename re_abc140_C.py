N = int(input())
B = list(map(int, input().split()))
A = [0] * N
A[0] = B[0]
j = 1

for i in range(1, N):
    if j == N - 1:
        A[i] = B[i - 1]
    else:
        A[i] = min(B[i], B[i -  1])
    j += 1
print(sum(A))

