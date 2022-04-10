N = int(input())
ans = ''
L = []
for i in range(N):
    i += 1
    L.append(i)
    for j in range(len(L) - 1):
        L.append(L[j])
print(*L)