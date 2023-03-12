N = int(input())
A = list(map(int, input().split()))

C = [0] * 9

for i in range(N):
    C[A[i] - 1] += 1
print(C.index(max(C)) + 1)