N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
same = 0
for i in range(N):
    if A[i] == B[i]:
        same += 1
