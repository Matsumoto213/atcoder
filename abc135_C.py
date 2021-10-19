n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ans = 0

i = 0
j = 0

cnt = 0
while True:
    if a[n] == 0 or b[n - 1] == 0:
        break
    dif = abs(i - j)
    if dif <= 2:
        if i >= j:
            if a[i] < b[j]:
                b[j] = abs(a[i] - b[j])
                cnt += a[i]
                a[i] = 0
                i += 1
            elif a[i] == b[j]:
                cnt += a[i]
                a[i] = 0
                b[j] = 0
                i += 1
                j += 1
            else:
                a[i] = abs(a[i] - b[j])
                cnt += b[j]
                b[j] = 0
                j += 1
        else:
            i = j
print(cnt)

