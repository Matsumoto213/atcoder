N,Y = map(int,input().split())
x = -1
y = -1
z = -1
for i in range(N + 1):
    for j in range(N + 1 - i):
        l = N - i - j
        temp = (10000 * i) + (5000 * j) + (1000 * l)
        if temp == Y:
            x = i
            y = j
            z = l
print(x,y,z)