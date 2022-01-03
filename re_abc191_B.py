N,X = map(int, input().split())
A = list(map(int, input().split()))
L = []
for i in A:
    if i != X:
        L.append(i)
print(*L)