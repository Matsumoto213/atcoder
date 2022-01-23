N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 10 ** 11 + 7
temp = A[0]
# 一番小さい数をどんどん引いていって乗り越えたところの差分を引く
for i in range(1,N):
    n = A[i] % temp
    if n != 0:
        tem = n - (temp - n)
    else:
        tem = temp
        
    ans = min(tem, ans)
    
    if ans == 1:
        print(1)
        exit(0)
print(ans)
    