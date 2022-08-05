Y = int(input())

temp = Y % 4

if temp == 0:
    print(Y + 2)
elif temp == 1:
    print(Y + 1)
elif temp == 2:
    print(Y)
elif temp == 3:
    print(Y + 3)
