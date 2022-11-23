N,K = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(K):
    a = a[1:]
    a = a + [0]

print(*a)
