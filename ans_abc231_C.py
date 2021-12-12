from bisect import bisect_left

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

for _ in range(Q):
    x = int(input())
    ind = bisect_left(A, x)
    print(N - ind)