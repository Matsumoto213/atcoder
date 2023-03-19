N,L = map(int, input().split())
l = []

for i in range(1, N + 1):
    l.append(L + i - 1)
li = sorted(l, key=abs)
print(sum(li[1:]))