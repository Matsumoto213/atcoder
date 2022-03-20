N = int(input())
T = input()
di = 'e'
x,y = 0,0
for i in T:
    if i == 'R':
        if di == 'e':
            di = 'n'
        elif di == 'n':
            di = 'w'
        elif di == 'w':
            di  = 's'
        else:
            di = 'e'
    else:
        if di == 'e':
            x += 1
        elif di == 'w':
            x -= 1
        elif di == 's':
            y += 1
        else:
            y -= 1

print(x,y)

