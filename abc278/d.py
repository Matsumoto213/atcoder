N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
Q = int(input())

for _ in range(Q):
    x,*y = list(map(int, input().split()))
    if x == 1:
        temp = y[0]
        A = defaultdict(lambda:temp)
    elif x == 2:
        A[y[0] - 1] += y[1]
    elif x == 3:
        print(A[y[0] - 1])