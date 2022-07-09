N = int(input())
A = list(map(int, input().split()))
C = dict()

for i in range(1,N + 1):
    C[i] = 0

for i in range(N - 1):
    C[A[i]] += 1

for value in C.values():
    print(value)