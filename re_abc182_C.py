N = input()

lenN = len(N)
min_ = 10 ** 11
for i in range(2 ** lenN):
    ans = ""
    erase = 0
    for j in range(lenN):
        # iを二進数にしてj番目が1かどうかを判断する
        if i & (1 << j):
            ans = ans + N[j] 
        else:
            erase += 1
    if len(ans) >= 1:
        ans = int(ans)
    else:
        ans = 0
  
    if ans % 3 == 0:
        min_ = min(erase,min_)

print(-1 if min_ == 10 ** 1 or min_ == len(N) else min_)