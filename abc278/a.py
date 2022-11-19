# N = int(input())
N,K = map(int, input().split())
a = list(map(int, input().split()))
# a = [input() for _ in range(N)]

for _ in range(K):
    del a[0]
    a.append(0)

print(*a)