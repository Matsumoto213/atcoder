s = input()
l = []

for i in s:
    if i == "B":
        if len(l) == 0:
            pass
        else:
            del l[-1]
    elif i == "0":
        l.append('0')
    else:
        l.append('1')

print(''.join(l))
        