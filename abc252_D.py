N = int(input())
A = list(map(int, input()).split())
L = []
for i in range(10):
    mi = 10 ** 15
    for j in range(N):
        mi = min(A[j].index(i),mi)
    L.append(mi)
print(L)
