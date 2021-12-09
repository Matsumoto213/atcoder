import math
N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
zero_count = A.count(0)

not_zero = N - zero_count
print(math.ceil(sum_A / not_zero))