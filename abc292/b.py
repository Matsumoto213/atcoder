N,Q = map(int, input().split())
L = [0] * N
for i in range(Q):
    x,player = map(int, input().split())
    if x == 1:
        L[player - 1] += 1
    elif x == 2:
        L[player - 1] += 2
    elif x == 3:
        if L[player - 1] >= 2:
            print('Yes')
        else:
            print('No')
