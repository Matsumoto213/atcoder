n, k, x = map(int, input().split())
a = [*map(int, input().split())]

a.sort(reverse=True)

for i in range(n):
  use = min(a[i] // x, k)
  k -= use
  a[i] -= use*x

a.sort(reverse=True)

for i in range(n):
  if k > 0:
    a[i] = 0
    k -= 1

print(sum(a))
