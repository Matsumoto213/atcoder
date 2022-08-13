n,a,b = map(int, input().split())

white = '.'*b
brack = '#'*b

row1 = ''
row2 = ''


for i in range(2):
    for j in range(n * b // b):
        if i == 0:
            if j % 2 == 0:
                row1 += white
            else:
                row1 += brack
        else:
            if j % 2 == 0:
                row2 += brack
            else:
                row2 += white

temp = 1
for i in range(n * a):
    if i // a % 2 == 0:
        print(row1)
    else:
        print(row2)