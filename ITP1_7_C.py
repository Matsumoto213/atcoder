h,w = map(int, input().split())
L = []
for i in range(h):
    mass = list(map(int, input().split()))
    L.append(mass)

l = []
for i in range(h):
    for j in range(w + 1):
        # 右端の場合
        if j == w:
            temp = sum(L[i])
            print(temp,end = " ")
        else:
            print(L[i][j],end = " ")
    print()

ans = 0
for i in range(w):
    temp = 0
    for j in range(h):
        temp += L[j][i]
    ans += temp
    print(temp,end = " ")
print(ans)