N = int(input())
A = list(map(int, input().split()))

def insert_numbers(N, A):
    B = [A[0]]
    for i in range(1, N):
        if abs(A[i] - A[i-1]) > 1:
            B.extend(list(range(min(A[i], A[i-1]) + 1, max(A[i], A[i-1]))[::-1 if A[i] < A[i-1] else 1]))
        B.append(A[i])
    return B

print(*insert_numbers(N,A))