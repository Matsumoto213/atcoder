a,b,c = map(int, input().split())
count = 0

while True:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0 and count == 0:
        print(0)
        break
    a = a / 2
    b = b / 2
    c = c / 2
    k = a
    a += b
    b += c
    c += k
    count += 1

    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        print(count)
        break
    if count > 1000:
        print(-1)
        break
    
    

