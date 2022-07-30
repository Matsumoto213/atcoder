N = int(input())
a = list(map(int, input().split()))
L = dict()

for i in range(N):
    L[a[i]] = i + 1

for i in range(N):
    print(L[i + 1],end = " ")