K,N = map(int, input().split())
A = list(map(int, input().split()))

ans = A[N - 1] - A[0]

for i in range(1,N):
    i_to_start = K - A[i]
    start_to_i = A[i - 1]
    ans = min(ans,i_to_start + start_to_i)
print(ans)