N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

import bisect
for _ in range(Q):
    rating = int(input())
    idx = bisect.bisect_left(A,rating)
    if idx == 0:
        print(abs(A[idx] - rating))
    elif idx == N:
        print(abs(A[idx - 1] - rating))
    else:
        print(min(abs(A[idx] - rating),abs(A[idx - 1] - rating)))