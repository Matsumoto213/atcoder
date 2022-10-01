N = int(input())
temp = hex(N)

if len(temp[2:]) == 1:
    print('0'+ temp[2:].upper())
else:
    print(temp[2:].upper())