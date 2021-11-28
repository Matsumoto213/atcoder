N,K = map(int, input().split())
cnt = 0

while True:
    ans = abs(N - K)
    if ans > N:
        print(N)
        break
    else:
        N = min(N,ans) 
    cnt += 1
