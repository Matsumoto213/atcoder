N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 200

ans = 0
for i in range(N):
    mo = A[i] % 200
    ans += cnt[mo]
    
    cnt[mo] += 1
print(ans)