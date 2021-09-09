x, y = map(int, input().split())

ans = 0

if x == y:
    ans = x
elif x == 0 and y == 1 or x == 1 and y == 0:
    ans = 2
elif x == 2 and y == 1 and x == 1 and y == 2:
    ans = 0
else:
    ans = 1