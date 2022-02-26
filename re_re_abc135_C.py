N = int(input())
A = list(map(int, input().split()))
# Bが勇者
B = list(map(int, input().split()))
 
ans = 0
 
for i in range(N):
    # Bの勇者のほうが力が上の場合
    if B[i] >= A[i]:
        ans += min(B[i],A[i])
        B[i] -= min(B[i],A[i])
        ans += min(B[i],A[i + 1])
        A[i + 1] -= min(B[i],A[i + 1])
    # それ以外、つまり
    else:
        ans += min(B[i],A[i])
print(ans)