n = int(input())
a = list(map(int, input().split()))

x = 0
for i in range(n):
    if a[i] % 2 == 0:
        x += 1
    print(3 ** n - 2 ** x)