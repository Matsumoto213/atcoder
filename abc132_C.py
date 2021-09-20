n = int(input())
lst = list(map(int, input().split()))
lst.sort()

n = int(n / 2)
a = lst[n] - lst[n - 1]
print(a)