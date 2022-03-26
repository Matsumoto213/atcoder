N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
import itertools

judge = True
for i in range(N - 1):
    if abs(A[i] - A[i + 1]) > K and abs(A[i] - B[i + 1]) > K and abs(B[i] - A[i + 1]) > K and abs(B[i] - B[i + 1]) > K:
        judge = False
print('Yes' if judge else 'No')