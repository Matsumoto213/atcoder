N = int(input())
p = list(map(int, input().split()))
A = [0] * N

for idx,i in enumerate(p):
    A[i - 1] = idx + 1

for i in A:
    print(i, end = " ")