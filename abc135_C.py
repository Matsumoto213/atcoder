n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = a[::-1]
b = b[::-1]

ans = 0

i = 0
j = 0

cnt = 0
while True:
    if a[n - 1] == 0 or b[n - 1] == 0:
        break
    dif = abs(i - j)
    if dif < 2:
        if a[i] < b[i]:
            b[j] = abs(a[i] - b[i])
            a[i] = 0
            cnt += b[j]
            i += 1
        else:
            a[i] = abs(a[i] - b[j])
            b[j] = 0
            cnt += a[i]
            j += 1
        print(a,b)
        print(i,j)
