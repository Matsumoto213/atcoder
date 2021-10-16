n = int(input())
p = list(map(int,input().split()))

count = 0
for i in range(n - 2):
    a = p[i:i + 3]
    if a[0] < a[1] and a[1] < a[2] or a[0] > a[1] and a[1] > a[2]:
        count += 1
print(count)

