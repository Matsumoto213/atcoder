h,w = map(int, input().split())
total = [0] * (w + 1)
for i in range(h):
    a = list(map(int, input().split()))
    a.append(sum(a))
    print(*a)
    for j in range(w + 1):
        total[j] += a[j]
print(*total)