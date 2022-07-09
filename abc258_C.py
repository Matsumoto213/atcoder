N,Q = map(int, input().split())
S = list(input())
start = 0
for i in range(Q):
    t,x = map(int, input().split())
    if t == 1:
        start = (start - x) % N
    if t == 2:
        x -= 1
        print(S[(start + x) % N])
