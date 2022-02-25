x,y = map(int, input().split())

if x > 0 and x < y:
    print(y - x)
elif x > 0 and x > y:
    print(1 + abs(-(x) - y))
elif x < 0 and x > y:
    print(2 + abs(x - y))
elif x < 0 and x < y:
    print(abs(x - y))


