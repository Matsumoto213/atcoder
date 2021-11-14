M,N,X = map(int, input().split())
ans = X
cnt = 0
for i in range(M):
    w = int(input())
    ans -= w
    if ans <= 0:
        ans = X
        N -= 1
    else:
        cnt += 1
    if N == 0:
        break
print(cnt)
     
    