a = list(map(int, input().split()))

a.sort()
ans = a[2] - a[1] == a[1] - a[0]

print('Yes' if ans else 'No')