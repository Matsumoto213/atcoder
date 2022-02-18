a,b,c,d = map(int, input().split())
temp = 0
time = 0

while True:
    if time == 10 ** 5:
        print(-1)
        break
    time += 1
    a += b
    temp += c

    if a <= temp * d:
        print(time)
        exit(0)