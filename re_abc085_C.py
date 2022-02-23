N,Y = map(int, input().split())
ans = 0
a = -1
b = -1
c = -1

for x in range(N + 1):
    for y in range(N + 1 - x):
        z = N - x - y
        if z < 0:
            continue
        temp = (10000 * x) + (5000 * y) + (1000 * z)

        if temp == Y:
            a = x
            b = y
            c = z
            print(a,b,c)
            exit()
print(a,b,c)
