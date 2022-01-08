N,x = map(int, input().split())
X = list(map(int, input().split()))
X.append(x)
X.sort()
temp = X[1] - X[0]

t = 1
while True:
    if t ==  N:
        print(temp)
        break
    for i in range(2, N + 1):
        tem = X[i] - X[i - 1]
        if tem % temp == 0:
            t += 1
        else:
            t = 1
            if temp % 2 == 0:
                temp // 2
            else:
                temp = 1

