N = int(input())
A = list(map(int, input().split()))
mod = (10 ** 9) + 7
su = sum(A)

ans = 0
for i in range(len(A)):
    su -= A[i]
    ans += su * A[i]
    ans %= mod

print(ans)
    
    

