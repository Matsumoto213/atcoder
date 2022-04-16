N = int(input())
A = list(map(int, input().split()))

all = N ** 3

# 偶数を数える
even = 0
for i in range(N):
    if A[i] % 2 == 0:
        even += 1

print(all - 2 ** even)