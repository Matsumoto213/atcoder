N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
q = int(input())

for _ in range(q):
    query,*query_x = map(int, input().split())
    if query == 1:
        temp = query_x[0]
        A = defaultdict(lambda:temp)
    elif query == 2:
        A[query_x[0] - 1] += query_x[1]
    elif query == 3:
        print(A[query_x[0] - 1])
    print(A)