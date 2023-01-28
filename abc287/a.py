N = int(input())
S = [input() for i in range(N)]
y = 0
n = 0
for i in range(N):
    if S[i] == 'For':
        y += 1
    else:
        n += 1

if y > n:
    print('Yes')
else:
    print('No')