N,M,T = map(int, input().split())
battery_all = N
before = 0
for i in range(M):
    a,b = map(int, input().split())
    N -= a - before

    if N <= 0:
        print('No')
        exit()
    N = min(N + b - a, battery_all)
    before = b

N -= T - before

if N <= 0:
    print('No')
else:
    print('Yes')