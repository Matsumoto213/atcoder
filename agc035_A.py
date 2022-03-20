N = int(input())
a = list(map(int, input().split()))

judge = True
for i in range(N):
    if a[i] != a[i - 1] ^ a[i - 2]:
        judge = False

print('Yes' if judge else 'No')