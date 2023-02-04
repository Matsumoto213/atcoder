N,M,T = map(int, input().split())
cafe_time = []
for i in range(M):
    start,finish = map(int, input().split())
    for time in range(start + 1,finish + 1):
        cafe_time.append(time)
battery = N
for time in range(1,T + 1):
    if time in cafe_time:
        if battery + 1 < N:
            battery += 1
    else:
        battery -= 1
    if battery <= 0:
        print('No')
        exit()
print('Yes')