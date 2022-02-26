from collections import Counter
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

L = Counter(A)
for i in range(M):
    if B[i] not in A or L[B[i]] == 0:
        print("No")
        exit()
    else:
        L[B[i]] -= 1
print('Yes')


