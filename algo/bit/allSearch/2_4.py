a,b = map(int, input().split())

L = []
for i in range(1, max(a,b) + 1):
    if i % a == 0 and i % b == 0:
        L.append(i)
print(L[-1])