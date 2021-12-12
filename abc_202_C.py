from collections import Counter
 
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
L = Counter(A)
ans = 0
for j in range(N):
    ans += L[B[C[j] - 1]]
print(ans)