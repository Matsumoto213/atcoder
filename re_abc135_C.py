N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

for i in range(N):
    if A[i] < B[i]:
        ans += A[i]
        B[i] -= A[i]
        # まだ勇者が死んでいない場合
        if B[i] > 0: 
            if A[i + 1] < B[i]:
                ans += A[i + 1]
            elif A[i + 1] == B[i]:
                ans += A[i + 1]
            else:
                ans += B[i]
    elif A[i] == B[i]:
        ans += A[i]
    else:
        ans += B[i]
print(ans)
