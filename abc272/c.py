N = int(input())
A = list(map(int, input().split()))
O = []
E = []

for i in range(N):
    if A[i] % 2 == 0:
        E.append(A[i])
    else:
        O.append(A[i])

E.sort(reverse = True)
O.sort(reverse = True)
if len(E) <= 1 and len(O) <= 1:
    print(-1)
else:
    if len(E) <= 1 and len(O) >= 2:
        print(O[0] + O[1])
    elif len(E) >= 2 and len(O) <= 1:
        print(E[0] + E[1])
    else:
        print(max(E[0] + E[1],O[0] + O[1]))