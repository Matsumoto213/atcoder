

while True:
    h,w = map(int, input().split())
    if h == w == 0:
        exit()

    for i in range(h):
        for j in range(w):
            print('#', end = "")
        print()
    print()

