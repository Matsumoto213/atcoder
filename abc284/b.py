T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for j in range(N):
        if A[j] % 2 != 0:
            ans += 1
    print(ans)