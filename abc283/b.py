N = int(input())
a = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    q,*query = map(int, input().split())
    if q == 1:
        a[query[0] - 1] = query[1]
    elif q == 2:
        print(a[query[0] - 1])
