N = int(input())
P = list(map(int, input().split()))

ans = 0
temp = N
while True:
    for i in range(N):
        if temp == i + 2:
            temp = P[i]
            ans += 1
            if temp == 1:
                print(ans)
                exit()