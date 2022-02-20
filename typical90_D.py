H,W = map(int, input().split())

L = []

for i in range(H):
    mass = list(map(int, input().split()))
    L.append(mass)
ans = []

for i in range(H):
    temp = 0
    for j in range(H):
        temp += mass[i]
