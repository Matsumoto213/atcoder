a,b = map(int, input().split())

if a + b == 1:
    print(a,b)
else:
    temp = (a + b) / 1.4
    print(a / temp, b / temp)