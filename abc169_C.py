N = int(input())
A = list(map(int, input().split()))

ma = 10 ** 18
ans = 1
A.sort(reverse = True)

if 0 in A:
    print(0)
    exit()
    
for i in range(N):
    ans *= A[i]
    if ans > ma:
        print(-1)
        exit()
    
print(ans)