from collections import defaultdict
N = int(input())
A = list(map(int, input(). split()))
B = list(map(int, input(). split()))
C = list(map(int, input(). split()))
 
D = defaultdict(int)
for i in A:
    D[i] += 1

ans = 0
for i in C:
    if B[i - 1] in D:
        ans += D[B[i-1]]

print(ans)