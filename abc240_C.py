N,X = map(int,input().split())
L = [0]
for i in range(N):
    a,b = map(int,input().split())
    l = []
    for j in L:
        l.append(j + a)
        l.append(j + b)
    L = list(set(l))

if X in L:
    print('Yes')
else:
    print('No')