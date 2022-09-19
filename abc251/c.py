N = int(input())
L = {}
C = []
for i in range(N):
    s,t = input().split()
    t = int(t)
    C.append((s,t))
    if s not in L:
        L[s] = t
L = sorted(L.items(), key=lambda x:x[1], reverse = True)
print(C.index(L[0]) + 1)