def is_good_sequence(A, K):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    for i in range(n - K + 1):
        c = prefix_sum[i + K] - prefix_sum[i]
        if c % K == 0:
            c = c // K
        else:
            return False

    return True

N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    if is_good_sequence(A[l - 1:r], K):
        print("Yes")
    else:
        print("No")