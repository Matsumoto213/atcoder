N,K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = set(a)

for idx in range(K):
    if idx not in a:
        print(idx)
        exit()
print(K)