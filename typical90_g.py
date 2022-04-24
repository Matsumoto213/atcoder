N = int(input())
A = list(map(int,input().split()))
Q = int(input())
A.sort()
import bisect

for i in range(Q):
    n = int(input())
    temp = bisect.bisect_right(A,n)
    if temp == 0:
        print(A[temp] - n)
    elif temp == N:
        print(n - A[temp - 1])
    else:
        print(min(abs(A[temp] - n),abs(A[temp - 1] - n)))
