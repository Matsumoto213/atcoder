N,M,T = map(int, input().split())
A = list(map(int, input().split()))
xy = {}

for _ in range(M):
    x,y = map(int, input().split())
    xy[x] = y

position = 1
for i in range(N - 1):
    T -= A[i]
    if T <= 0:
        print('No')
        exit()
    else:
        position += 1
        if position in xy:
            T += xy[position]
print('Yes')