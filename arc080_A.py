import math
N = int(input())
A = list(map(int, input().split()))

four = 0
two = 0
for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 4 == 0:
            four += 1
        else:
            two += 1

if two < 2:
    if four * 2 + 1 >= N:
        print("Yes")
    else: 
        print('No')
else:
    if four * 2 + two >= N:
        print('Yes')
    else:
        print('No')