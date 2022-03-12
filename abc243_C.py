N =int(input())
XY = []
for i in range(N):
    x,y = map(int, input().split())
    XY.append((x,y))

S = input()
r = []
l = []

for i in range(N):
    if S[i] == 'R':
        r.append(XY[i])
    else:
        l.append(XY[i])

l.sort(key = lambda x: x[1])
r.sort(key = lambda x: x[1])
for i in range(len(l)):
    a,b = l[i]
    for j in range(len(r)):
        c,d = r[j]
        if b == d:
            if a > c:
                print('Yes')
                exit(0)
print('No')