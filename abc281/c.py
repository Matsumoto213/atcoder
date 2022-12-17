N,T = map(int,input().split())
A = list(map(int,input().split()))
 
#一周にどれくらい時間がかかるか求める
total_time = sum(A)
 
#与えられた時間をtotal_timeで割った余りを考える
now = T % total_time

for i in range(N):
    temp = now - A[i]
    if temp < 0:
        print(str(i+1) + " " + str(now))
        break
    else:
        now -= A[i]