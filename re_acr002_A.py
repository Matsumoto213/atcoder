a,b = map(int, input().split())
dif = a - (b) + 1
if a < 0 and b > 0:
    print('Zero')
elif a > 0 and b > 0:
    print('Positive')
elif a < 0 and b < 0:
    if dif % 2 == 0:
        print('Positive')
    else:
        print('Negative')