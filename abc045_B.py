a = list(input())
b = list(input())
c = list(input())
ans = ''
t = 0
while True:
    if len(a) == 0 and temp == 'a':
        ans = 'A'
        break
    elif len(b) == 0 and temp == 'b':
        ans = 'B'
        break
    elif len(c) == 0 and temp == 'c':
        ans = 'C'
        break

    if t == 0:
        temp = a[0]
        del a[0]
    else:
        if temp == 'a':
            temp = a[0]
            del a[0]
        elif temp == 'b':
            temp = b[0]
            del b[0]
        else:
            temp = c[0]
            del c[0]
    t += 1
print(ans)