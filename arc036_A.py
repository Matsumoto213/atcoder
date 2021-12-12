N,K = map(int, input().split())
T = []
for idx,i in enumerate(range(N)):
    sleep_time = int(input())
    T.append(sleep_time)
    
    if idx >= 2:
        time = sum(T[idx - 2:idx + 1])
    
        if time < K:
            print(idx + 1)
            exit(0)
print(-1)
        