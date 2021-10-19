s = input()
n = int(input())

if len(s) == 1:
    print(int(s))

i = 0
cnt = 0
while True:
    if i == len(s):
        cnt += 1
        i = 0
    if cnt == n:
        break
    
    if s[i] == '1':
        i += 1

    elif s[i] == '2':
        s = s[:i] + '2' * 2 + s[:i] 
        i += 2

    elif s[i] == '3':
        s[i] = '3'* 3
        i += 3

    elif s[i] == '4':
        s[i] = '4'*4
        i += 4

    elif s[i] == '5':
        s[i] = '5'*5
        i += 5
    elif s[i] == '6':
        s[i] = '6'*6
        i += 6
    elif s[i] == '7':
        s[i] = '7'*7
        i += 7
    elif s[i] == '8':
        s[i] = '8'*8
        i += 8
    else:
        s[i] = '9'*9
        i += 2 
    i += 1

print(s[n - 1])
