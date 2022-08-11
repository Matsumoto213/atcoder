N,K = map(int, input().split())

A = []
for i in range(N):
    p = sum(list(map(int, input().split())))
    A.append(p)

L = sorted(A,reverse = True)
for a in A:
    temp = L[K - 1] - a
    if temp > 300:
        print('No')
    else:
        print('Yes')