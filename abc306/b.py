def calculate_sum(A):
    return sum(A[i] * (2 ** i) for i in range(len(A)))

A = list(map(int, input().split()))
output = calculate_sum(A)
print(output)