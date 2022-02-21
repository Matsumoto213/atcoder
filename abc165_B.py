x = int(input())
hun = 100
time = 0
while True:
    if hun >= x:
        print(time)
        break

    hun += hun // 100
    time += 1