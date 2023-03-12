N = int(input())
A = list(map(int, input().split()))
C = [0] * 9

for i in range(N):
    C[A[i] - 1] += 1

for j in range(9):
    print(C[j])