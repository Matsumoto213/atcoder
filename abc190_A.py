a,b,c = map(int, input().split())


while True:
    if a == 0 or b == 0:
        break
    if c == 0:
        a -= 1
        if a != 0:
            b -= 1
            if b == 0:
                print("Takahashi")
                break
        else:
            print("Aoki")
            break
    else:
        b -= 1
        if b != 0:
            a -= 1
            if a == 0:
                print("Aoki")
                break
        else:
            print("Takahashi")
            break