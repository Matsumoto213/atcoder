N = int(input())
T = [0]
X = [0]
Y = [0]
for i in range(N):
    t,x,y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

judge = True
for i in range(N):
    dt = T[i + 1] - T[i]
    dist = abs(X[i + 1] - X[i]) + abs(Y[i + 1] - Y[i])
    if dt < dist:
        judge = False
    # 偶数と奇数が一致する必要があるコードはこれを使う
    if dist % 2 != dt % 2:
        judge = False

print('Yes' if judge else 'No')