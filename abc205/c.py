a,b,c = map(int, input().split())

if c % 2 == 0:
    c = 2
else:
    c = 1
a_c = a ** c
b_c = b ** c
if a_c > b_c:
    print('>')
elif a_c < b_c:
    print('<')
else:
    print('=')