n,a,b = map(int, input().split())

cnt = 0
while True:
    dif = abs(b - a)
    if dif == 1 and cnt % 2 == 0:
        print("Borys")
        break
    a += 1
    cnt += 1
    dif = abs(b - a)

    if dif == 1 and cnt % 2 != 0:
        print("Alice")
        break
    else:
        b -= 1
        cnt += 1


    
