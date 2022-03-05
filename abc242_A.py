a,b,c,x = map(int, input().split())
if x <= a:
    print(1.00000000)
elif x <= b and x > a:
    temp = b - a
    print(c / temp)
elif x > b:
    print(0.00000000)

