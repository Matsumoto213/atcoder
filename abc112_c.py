n = int(input())
x = []
y = []
h = []

for i in range(n):
    x[i],y[i],h[i] = map(int,input().split())
    x.append(x[i])
    y.append(x[i])
    h.append(h[i])

ok = 0

for cx in range(101):
    for cy in range(101):
        h = 1
        for i in range(n):
            H = h[i] + abs(cx - x[i]) + abs(cy - y[i])
            if H == h[i]:
                ok = 1
        for j in range(n):
            if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                ok = 0
            if ok == 0:
                print(cx, cy, H)
                break


            

