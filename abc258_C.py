N,Q = map(int, input().split())
S = list(input())
from collections import deque
S = deque(S)
for i in range(Q):
    query = input()
    t,x = int(query[0]),int(query[2])
    if t == 2:
        print(S[x - 1])
    else:
        temp = S[:x]
        print(temp)