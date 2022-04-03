k,n = map(int, input().split())
A = list(map(int, input().split()))

ans = A[n - 1] - A[0]

for i in range(n):
    start = k - A[i]
    finish = A[i - 1]
    print(start,finish)
    ans = min(ans,start + finish)
print(ans)