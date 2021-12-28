import bisect
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
temp = 10 ** 9 + 7

for i in range(N):
    idx = bisect.bisect_left(B,A[i])
    if idx == 0:
        num = abs(B[idx] - A[i])
    elif idx == M:
        num = abs(B[idx - 1] - A[i])
    else:
        num = min(abs(B[idx] - A[i]),abs(B[idx - 1] - A[i]))
    
    temp = min(num,temp)
    
print(temp)