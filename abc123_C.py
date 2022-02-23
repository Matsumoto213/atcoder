N = int(input())
A = [int(input()) for _ in range(5)]
mi = 10 ** 15

for i in range(5):
    mi = min(mi,A[i])

ans = 4 + (N + mi - 1) / mi
print(int(ans))