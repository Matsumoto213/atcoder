N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = 0
for i in range(N):
    diff += abs(A[i] - B[i])

ans = K - diff
if ans < 0 or ans % 2 != 0:
    print('No')
else:
    print('Yes')
