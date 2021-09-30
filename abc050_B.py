n = int(input())
time = list(map(int, input().split()))
m = int(input())

for i in range(m):
    x,m = map(int, input().split())
    ans = sum(time) - time[x - 1] + m
    print(ans)