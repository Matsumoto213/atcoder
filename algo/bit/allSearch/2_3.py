N = int(input())

ans = 0
for i in range(2,N + 1):
    if N % i == 0:
        ans += 1

if ans == 1:
    print('Yes')
else:
    print('No')